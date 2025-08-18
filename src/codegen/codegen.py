from ast import Sub
from typing import Any, List, Optional
from ..utils.visitor import ASTVisitor
from ..utils.nodes import *
from .emitter import Emitter
from .frame import Frame
from .error import IllegalOperandException, IllegalRuntimeException
from .io import IO_SYMBOL_LIST
from .utils import *
from functools import *


class CodeGenerator(ASTVisitor):
    def __init__(self):
        self.class_name = "HLang"
        self.emit = Emitter(self.class_name + ".j")
        # current_frame used as fallback when visitor call didn't pass Access/SubBody
        self.current_frame: Optional[Frame] = None

    # --- helper to get a safe frame from 'o' or fallback to current_frame ---
    def _get_frame(self, o: Any):
        if isinstance(o, (Access, SubBody)) and getattr(o, "frame", None) is not None:
            return o.frame
        if self.current_frame is not None:
            return self.current_frame
        raise IllegalRuntimeException("Frame is not available")

    # --- helper to get sym list safely ---
    def _get_sym(self, o: Any):
        if isinstance(o, (Access, SubBody)):
            return getattr(o, "sym", [])
        return []

    def visit_program(self, node: "Program", o: Any = None):
        # Prolog cho class
        self.emit.print_out(
            self.emit.emit_prolog(self.class_name, "java/lang/Object")
        )

        # Symbol table toàn cục khởi tạo từ IO
        symbols = list(IO_SYMBOL_LIST)  # copy
        self.global_inits = []

        # --- Pha 1: xử lý const và var ---
        env = SubBody(None, symbols)
        for decl in node.const_decls:
            if isinstance(decl, (ConstDecl, VarDecl)):
                env = self.visit(decl, env)
        symbols = env.sym

        # --- Pha 2: khai báo hàm (chỉ thêm symbol) ---
        for f in filter(lambda d: isinstance(d, FuncDecl), node.func_decls):
            fn_type = FunctionType([p.param_type for p in f.params], f.return_type)
            symbols.append(Symbol(f.name, fn_type, CName(self.class_name)))

        global_env = SubBody(None, symbols)

        # --- Pha 3: sinh <clinit> ---
        if self.global_inits:
            self._gen_clinit(symbols)

        # --- Pha 4: code các hàm ---
        for f in node.func_decls:
            if isinstance(f, FuncDecl):
                self.visit(f, global_env)

        # --- constructor mặc định ---
        ctor_decl = FuncDecl("<init>", [], VoidType(), [])
        self.generate_method(ctor_decl, SubBody(Frame("<init>", VoidType()), []))

        # Kết thúc class
        self.emit.emit_epilog()

        # Debug: in toàn bộ jasmin code
        print("=== GENERATED JASMIN CODE ===")
        with open(self.emit.filename, "r") as f:
            print(f.read())
        print("=== END JASMIN CODE ===")


    def _gen_clinit(self, symbols):
        """Sinh mã cho <clinit> dựa trên global_inits"""
        frame = Frame("<clinit>", VoidType())
        out = self.emit.print_out

        out(".method public static <clinit>()V\n")
        out("Label0:\n")

        for name, value, typ in self.global_inits:
            rc, _ = self.visit(value, Access(frame, symbols))
            out(rc)
            putstatic_code = self.emit.emit_put_static(f"{self.class_name}/{name}", typ, frame)
            out(putstatic_code if putstatic_code.endswith("\n") else putstatic_code + "\n")

        out("\treturn\nLabel1:\n")
        out(".limit stack 10\n.limit locals 0\n.end method\n")

    def generate_method(self, node: "FuncDecl", o: SubBody = None):
        frame = o.frame
        old_frame = self.current_frame
        self.current_frame = frame

        is_init, is_main = node.name == "<init>", node.name == "main"

        # Xác định tham số và kiểu trả về
        if is_main:
            param_types, return_type = [ArrayType(StringType(), 0)], VoidType()
        else:
            param_types = [p.param_type for p in node.params]
            return_type = node.return_type

        # Sinh method header
        method_type = FunctionType(param_types, return_type)
        self.emit.print_out(self.emit.emit_method(node.name, method_type, not is_init))

        frame.enter_scope(is_proc=True)
        start_lbl, end_lbl = frame.get_start_label(), frame.get_end_label()

        # Khai báo biến cho tham số
        if is_init:
            idx_this = frame.get_new_index()
            self.emit.print_out(
                self.emit.emit_var(idx_this, "this", ClassType(self.class_name), start_lbl, end_lbl)
            )
        elif is_main:
            args_idx = frame.get_new_index()
            self.emit.print_out(
                self.emit.emit_var(
                    args_idx, "args", ArrayType(StringType(), 0), start_lbl, end_lbl
                )
            )

        else:
            for prm in node.params:
                o = self.visit(prm, o)

        self.emit.print_out(self.emit.emit_label(start_lbl, frame))

        # Thân hàm
        if is_init:
            self.emit.print_out(self.emit.emit_read_var("this", ClassType(self.class_name), idx_this, frame))
            self.emit.print_out(self.emit.emit_invoke_special(frame))

        for stmt in node.body:
            o = self.visit(stmt, o)

        if isinstance(return_type, VoidType):
            self.emit.print_out(self.emit.emit_return(VoidType(), frame))

        # Đóng method
        self.emit.print_out(self.emit.emit_label(end_lbl, frame))
        self.emit.print_out(self.emit.emit_end_method(frame))
        frame.exit_scope()

        # Khôi phục frame cũ
        self.current_frame = old_frame

    def _infer_type_from_literal(self, node, sym_table):
        """Trả về instance của Type dựa trên literal/identifier/array access."""

        def _lookup_identifier(id_node):
            sym = next((s for s in sym_table if s.name == id_node.name), None)
            if not sym:
                raise IllegalOperandException(id_node.name)
            return sym.type

        match node:
            case IntegerLiteral():
                return IntType()
            case FloatLiteral():
                return FloatType()
            case BooleanLiteral():
                return BoolType()
            case StringLiteral():
                return StringType()
            case ArrayLiteral():
                # Lấy danh sách phần tử, có thể lưu trong .elements hoặc .value
                elems = getattr(node, "elements", None) or getattr(node, "value", None)
                if not elems:
                    raise IllegalOperandException("Cannot infer type of empty array literal")

                first = elems[0]
                if isinstance(first, Identifier):
                    elem_type = _lookup_identifier(first)
                else:
                    elem_type = self._infer_type_from_literal(first, sym_table)

                return ArrayType(elem_type, len(elems))

            case Identifier():
                return _lookup_identifier(node)

            case ArrayAccess():
                arr_type = (
                    _lookup_identifier(node.array)
                    if isinstance(node.array, Identifier)
                    else self._infer_type_from_literal(node.array, sym_table)
                )
                if not isinstance(arr_type, ArrayType):
                    raise IllegalOperandException("Cannot index into non-array")
                return arr_type.element_type

            case _:
                # fallback: gọi visit nhưng dùng frame đặc biệt chỉ để lấy type
                _, t = self.visit(node, Access(Frame("<infer>", VoidType()), sym_table))
                return t

    def visit_const_decl(self, node: "ConstDecl", o: Any = None):
        # Lấy bảng ký hiệu hiện tại
        symbols = self._get_sym(o)

        # Suy luận kiểu từ literal (chỉ phân tích, không sinh code)
        const_type = self._infer_type_from_literal(node.value, symbols)

        # Sinh code khai báo hằng (không gán giá trị ban đầu)
        decl = self.emit.emit_attribute(node.name, const_type, is_final=True, value=None)
        self.emit.print_out(decl)

        # Thêm vào symbol table
        symbols.append(Symbol(node.name, const_type, CName(self.class_name)))

        # Gom hằng lại để sau này khởi tạo trong <clinit>
        self.global_inits = getattr(self, "global_inits", [])
        self.global_inits.append((node.name, node.value, const_type))

        return SubBody(getattr(o, "frame", None), symbols)


    def visit_func_decl(self, node: "FuncDecl", o: SubBody = None):
        # Mỗi hàm sẽ có frame riêng
        func_frame = Frame(node.name, node.return_type)

        # Sinh code cho thân hàm
        self.generate_method(node, SubBody(func_frame, o.sym))

        # Lấy danh sách kiểu tham số
        param_types = [param.param_type for param in node.params]

        # Trả về SubBody chứa symbol mới thêm vào
        func_symbol = Symbol(
            node.name,
            FunctionType(param_types, node.return_type),
            CName(self.class_name),
        )
        return SubBody(None, [func_symbol] + o.sym)


    def visit_param(self, node: "Param", o: Any = None):
        frame = self._get_frame(o)

        # Cấp chỉ số cho biến cục bộ
        idx = frame.get_new_index()

        # Sinh code khai báo biến tham số
        var_decl = self.emit.emit_var(
            idx,
            node.name,
            node.param_type,
            frame.get_start_label(),
            frame.get_end_label(),
        )
        self.emit.print_out(var_decl)

        # Trả về SubBody với symbol mới
        param_symbol = Symbol(node.name, node.param_type, Index(idx))
        return SubBody(frame, [param_symbol] + o.sym)

    # Type system (simply return the node itself)
    def visit_int_type(self, node: "IntType", o: Any = None):
        return node

    def visit_float_type(self, node: "FloatType", o: Any = None):
        return node

    def visit_bool_type(self, node: "BoolType", o: Any = None):
        return node

    def visit_string_type(self, node: "StringType", o: Any = None):
        return node

    def visit_void_type(self, node: "VoidType", o: Any = None):
        return node

    def visit_array_type(self, node: "ArrayType", o: Any = None):
        return node

    # Statements
    def visit_var_decl(self, node: "VarDecl", o: SubBody = None):
        frame = self._get_frame(o)
        symbols = self._get_sym(o)

        # --- 1. Xác định kiểu biến ---
        if node.type_annotation:
            var_type = node.type_annotation
        else:
            if node.value is None:
                raise IllegalOperandException(
                    f"Cannot infer type for variable '{node.name}' without initializer"
                )

            def guess_type(expr):
                if isinstance(expr, IntegerLiteral):
                    return IntType()
                if isinstance(expr, FloatLiteral):
                    return FloatType()
                if isinstance(expr, BooleanLiteral):
                    return BoolType()
                if isinstance(expr, StringLiteral):
                    return StringType()
                if isinstance(expr, ArrayLiteral):
                    elements = getattr(expr, "elements", None) or getattr(expr, "value", None)
                    if not elements:
                        raise IllegalOperandException("Cannot infer type of empty array literal")

                    # xác định kiểu phần tử đầu tiên
                    first = elements[0]
                    if isinstance(first, Identifier):
                        sym = next((s.type for s in symbols if s.name == first.name), None)
                        elem_type = sym or self.visit(first, Access(Frame("<infer>", VoidType()), symbols))[1]
                    else:
                        elem_type = guess_type(first)

                    return ArrayType(elem_type, len(elements))
                if isinstance(expr, Identifier):
                    sym = next((s for s in symbols if s.name == expr.name), None)
                    if not sym:
                        raise IllegalOperandException(expr.name)
                    return sym.type
                if isinstance(expr, ArrayAccess):
                    arr_t = None
                    if isinstance(expr.array, Identifier):
                        sym = next((s for s in symbols if s.name == expr.array.name), None)
                        if not sym:
                            raise IllegalOperandException(expr.array.name)
                        arr_t = sym.type
                    else:
                        arr_t = guess_type(expr.array)
                    if not isinstance(arr_t, ArrayType):
                        raise IllegalOperandException("Cannot index into non-array type")
                    return arr_t.element_type

                # fallback: dùng visitor để lấy type (có thể phát sinh code)
                _, t = self.visit(expr, Access(frame, symbols))
                return t

            var_type = guess_type(node.value)

        # --- 2. Cấp slot cho biến ---
        idx = frame.get_new_index()
        var_decl = self.emit.emit_var(
            idx, node.name, var_type, frame.get_start_label(), frame.get_end_label()
        )
        self.emit.print_out(var_decl)

        # cập nhật symbol table
        new_symbols = [Symbol(node.name, var_type, Index(idx))] + symbols

        # --- 3. Xử lý initializer ---
        if node.value:
            if isinstance(node.value, ArrayLiteral):
                code, t = self.visit(node.value, Access(frame, new_symbols))
                self.emit.print_out(code)
                self.emit.print_out(self.emit.emit_write_var(node.name, t, idx, frame))
            else:
                self.visit(
                    Assignment(IdLValue(node.name), node.value),
                    SubBody(frame, new_symbols),
                )

        return SubBody(frame, new_symbols)

    def visit_array_access(self, node: "ArrayAccess", o):
        frame = self._get_frame(o)
        symbols = self._get_sym(o)

        # --- 1. Lấy code cho mảng & chỉ số (chưa in) ---
        array_code, array_type = self.visit(node.array, Access(frame, symbols))
        index_code, index_type = self.visit(node.index, Access(frame, symbols))

        code = array_code + index_code

        # --- 2. Kiểm tra kiểu ---
        if not isinstance(array_type, ArrayType):
            raise IllegalOperandException(f"Cannot index into non-array type: {array_type}")

        elem_type = array_type.element_type

        # --- 3. Sinh lệnh load phù hợp ---
        if isinstance(elem_type, IntType):
            code += "iaload\n"
        elif isinstance(elem_type, BoolType):
            code += "baload\n"
        elif isinstance(elem_type, FloatType):
            code += "faload\n"
        else:  # String hoặc mảng lồng
            code += "aaload\n"

        return code, elem_type

    def visit_assignment(self, node: "Assignment", o: SubBody = None):
        frame = self._get_frame(o)
        symbols = self._get_sym(o)

        # --- 1. Trường hợp gán cho phần tử mảng ---
        if isinstance(node.lvalue, ArrayAccessLValue):
            arr_code, arr_type = self.visit(node.lvalue.array, Access(frame, symbols))
            idx_code, idx_type = self.visit(node.lvalue.index, Access(frame, symbols))
            rhs_code, rhs_type = self.visit(node.value, Access(frame, symbols))

            # clone() nếu RHS là mảng
            if isinstance(rhs_type, ArrayType):
                desc = self.emit.get_jvm_type(rhs_type)
                rhs_code += f"\tinvokevirtual {desc}/clone()Ljava/lang/Object;\n"
                rhs_code += f"\tcheckcast {desc}\n"

            # In theo thứ tự array_ref → index → value
            self.emit.print_out(arr_code)
            self.emit.print_out(idx_code)
            self.emit.print_out(rhs_code)

            # Chọn store instruction
            etype = arr_type.element_type
            if isinstance(etype, IntType):
                self.emit.print_out("iastore\n")
            elif isinstance(etype, BoolType):
                self.emit.print_out("bastore\n")
            elif isinstance(etype, FloatType):
                self.emit.print_out("fastore\n")
            else:
                self.emit.print_out("aastore\n")

        # --- 2. Trường hợp gán cho biến thường ---
        else:
            rhs_code, rhs_type = self.visit(node.value, Access(frame, symbols))

            if isinstance(rhs_type, ArrayType):
                desc = self.emit.get_jvm_type(rhs_type)
                rhs_code += f"\tinvokevirtual {desc}/clone()Ljava/lang/Object;\n"
                rhs_code += f"\tcheckcast {desc}\n"

            self.emit.print_out(rhs_code)

            lhs_code, _ = self.visit(node.lvalue, Access(frame, symbols))
            self.emit.print_out(lhs_code)

        return o

    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        frame = self._get_frame(o)
        symbols = self._get_sym(o)

        # --- 1. Điều kiện chính ---
        cond_code, _ = self.visit(node.condition, Access(frame, symbols))
        self.emit.print_out(cond_code)

        end_lbl = frame.get_new_label()
        else_lbl = frame.get_new_label()

        self.emit.print_out(self.emit.emit_if_false(else_lbl, frame))

        # --- 2. Then ---
        self.visit(node.then_stmt, o)
        self.emit.print_out(self.emit.emit_goto(end_lbl, frame))

        # --- 3. Elif / Else ---
        self.emit.print_out(self.emit.emit_label(else_lbl, frame))

        if getattr(node, "elif_branches", None):
            for cond, body in node.elif_branches:
                next_lbl = frame.get_new_label()
                cond_code, _ = self.visit(cond, Access(frame, symbols))
                self.emit.print_out(cond_code)
                self.emit.print_out(self.emit.emit_if_false(next_lbl, frame))
                self.visit(body, o)
                self.emit.print_out(self.emit.emit_goto(end_lbl, frame))
                self.emit.print_out(self.emit.emit_label(next_lbl, frame))

        if node.else_stmt:
            self.visit(node.else_stmt, o)

        # --- 4. End label ---
        self.emit.print_out(self.emit.emit_label(end_lbl, frame))
        return o

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        frame = self._get_frame(o)
        symbols = self._get_sym(o)

        cond_lbl = frame.get_new_label()
        end_lbl = frame.get_new_label()

        # Lưu nhãn break/continue cũ
        old_break, old_continue = getattr(frame, "_break_label", None), getattr(frame, "_continue_label", None)
        frame._break_label, frame._continue_label = end_lbl, cond_lbl

        # --- 1. In nhãn điều kiện ---
        self.emit.print_out(self.emit.emit_label(cond_lbl, frame))

        # --- 2. Kiểm tra điều kiện ---
        cond_code, _ = self.visit(node.condition, Access(frame, symbols))
        self.emit.print_out(cond_code)
        self.emit.print_out(self.emit.emit_if_false(end_lbl, frame))

        # --- 3. Thân vòng lặp ---
        self.visit(node.body, SubBody(frame, symbols))
        self.emit.print_out(self.emit.emit_goto(cond_lbl, frame))

        # --- 4. End ---
        self.emit.print_out(self.emit.emit_label(end_lbl, frame))

        # Khôi phục break/continue cũ
        frame._break_label, frame._continue_label = old_break, old_continue

        return o

    # ✅ SỬA LỖI: Thay thế toàn bộ hàm visit_for_stmt bằng phiên bản cuối cùng này.
    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        frame = self._get_frame(o)
        sym = self._get_sym(o)

        full_code = ""

        # BƯỚC 1: Xử lý collection
        col_code, col_type = self.visit(node.iterable, Access(frame, sym))
        full_code += col_code

        arr_tmp_idx = frame.get_new_index()
        arr_tmp_name = f"__arr_for_{arr_tmp_idx}"
        full_code += self.emit.emit_var(arr_tmp_idx, arr_tmp_name, col_type, frame.get_start_label(), frame.get_end_label())
        full_code += self.emit.emit_write_var(arr_tmp_name, col_type, arr_tmp_idx, frame)

        # BƯỚC 2: Tạo biến index tạm và khởi tạo bằng 0
        idx_tmp_idx = frame.get_new_index()
        idx_tmp_name = f"__idx_for_{idx_tmp_idx}"
        full_code += self.emit.emit_var(idx_tmp_idx, idx_tmp_name, IntType(), frame.get_start_label(), frame.get_end_label())
        full_code += self.emit.emit_push_iconst(0, frame)
        full_code += self.emit.emit_write_var(idx_tmp_name, IntType(), idx_tmp_idx, frame)

        # BƯỚC 3: Thiết lập label break/continue
        start_label = frame.get_new_label()
        end_label = frame.get_new_label()
        continue_target_label = frame.get_new_label()

        prev_break = getattr(frame, "_break_label", None)
        prev_continue = getattr(frame, "_continue_label", None)
        frame._break_label = end_label
        frame._continue_label = continue_target_label

        # BƯỚC 4: Vòng lặp
        full_code += self.emit.emit_label(start_label, frame)
        full_code += self.emit.emit_read_var(idx_tmp_name, IntType(), idx_tmp_idx, frame)
        full_code += self.emit.emit_read_var(arr_tmp_name, col_type, arr_tmp_idx, frame)
        full_code += "arraylength\n"
        full_code += f"if_icmpge Label{end_label}\n"

        # BƯỚC 5: Lấy phần tử
        full_code += self.emit.emit_read_var(arr_tmp_name, col_type, arr_tmp_idx, frame)
        full_code += self.emit.emit_read_var(idx_tmp_name, IntType(), idx_tmp_idx, frame)

        elem_type = col_type.element_type
        if isinstance(elem_type, (IntType, BoolType)):
            full_code += "iaload\n"
        elif isinstance(elem_type, FloatType):
            full_code += "faload\n"
        else:
            full_code += "aaload\n"

        loop_var_name = node.variable
        loop_var_idx = frame.get_new_index()
        full_code += self.emit.emit_var(loop_var_idx, loop_var_name, elem_type, frame.get_start_label(), frame.get_end_label())
        full_code += self.emit.emit_write_var(loop_var_name, elem_type, loop_var_idx, frame)

        body_sym = [Symbol(loop_var_name, elem_type, Index(loop_var_idx))] + sym

        # In toàn bộ code setup trước body
        self.emit.print_out(full_code)

        # Visit thân vòng lặp
        self.visit(node.body, SubBody(frame, body_sym))

        # BƯỚC 7: Update index
        cont_code = ""
        cont_code += self.emit.emit_label(continue_target_label, frame)
        cont_code += f"iinc {idx_tmp_idx} 1\n"
        cont_code += self.emit.emit_goto(start_label, frame)
        cont_code += self.emit.emit_label(end_label, frame)

        self.emit.print_out(cont_code)

        # Restore
        frame._break_label = prev_break
        frame._continue_label = prev_continue

        return o


    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        frame = self._get_frame(o)
        sym = self._get_sym(o)

        full_code = ""
        if node.value is None:
            full_code += self.emit.emit_return(VoidType(), frame)
        else:
            code, typ = self.visit(node.value, Access(frame, sym))
            full_code += code
            full_code += self.emit.emit_return(typ, frame)

        self.emit.print_out(full_code)
        return o


    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        frame = self._get_frame(o)
        break_label = getattr(frame, "_break_label", None)

        if break_label is None:
            raise IllegalRuntimeException("break not in loop")

        code = self.emit.emit_goto(break_label, frame)
        self.emit.print_out(code)
        return o


    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        frame = self._get_frame(o)
        continue_label = getattr(frame, "_continue_label", None)

        if continue_label is None:
            raise IllegalRuntimeException("continue not in loop")

        code = self.emit.emit_goto(continue_label, frame)
        self.emit.print_out(code)
        return o

    def visit_expr_stmt(self, node: "ExprStmt", o: SubBody = None):
        frame = self._get_frame(o)
        sym = self._get_sym(o)

        code, typ = self.visit(node.expr, Access(frame, sym))
        full_code = code

        # Nếu biểu thức trả về giá trị (không phải void), pop nó khỏi stack
        if not isinstance(typ, VoidType):
            full_code += self.emit.emit_pop(frame)

        self.emit.print_out(full_code)
        return o


    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        frame = self._get_frame(o)
        original_sym = self._get_sym(o)

        # 1. Bắt đầu một phạm vi mới
        frame.enter_scope(False)
        start_label = frame.get_start_label()
        end_label = frame.get_end_label()

        full_code = ""
        # 2. Nhãn bắt đầu
        full_code += self.emit.emit_label(start_label, frame)

        # 3. Visit các câu lệnh bên trong khối
        inner_env = SubBody(frame, original_sym[:])
        for stmt in node.statements:
            inner_env = self.visit(stmt, inner_env)

        # 4. Nhãn kết thúc
        full_code += self.emit.emit_label(end_label, frame)

        # 5. Kết thúc phạm vi
        frame.exit_scope()

        # 6. In code và trả về môi trường gốc
        self.emit.print_out(full_code)
        return SubBody(frame, original_sym)


    def visit_id_lvalue(self, node: "IdLValue", o: Access = None):
        frame = self._get_frame(o)
        sym = next((s for s in o.sym if s.name == node.name), None)
        if not sym:
            raise IllegalOperandException(node.name)

        if isinstance(sym.value, Index):
            return self.emit.emit_write_var(sym.name, sym.type, sym.value.value, frame), sym.type
        elif isinstance(sym.value, CName):
            return self.emit.emit_put_static(f"{self.class_name}/{sym.name}", sym.type, frame), sym.type
        else:
            raise IllegalOperandException(node.name)


    def visit_array_access_lvalue(self, node: "ArrayAccessLValue", o: Any = None):
        frame = self._get_frame(o)
        sym = self._get_sym(o)

        # sinh code cho array và index
        ac, at = self.visit(node.array, Access(frame, sym))
        ic, it = self.visit(node.index, Access(frame, sym))

        elem_type = at.element_type if isinstance(at, ArrayType) else at

        # gom code
        full_code = ac + ic + self.emit.emit_aload(elem_type, frame)

        return full_code, elem_type

    # Expressions
    def _jvm_array_signature(self, arr_type):
        """
        Trả về JVM descriptor của một ArrayType.
        Ví dụ:
            ArrayType(IntType()) -> [I
            ArrayType(ArrayType(IntType())) -> [[I
            ArrayType(StringType()) -> [Ljava/lang/String;
        """
        if isinstance(arr_type, ArrayType):
            return "[" + self._jvm_array_signature(arr_type.element_type)
        elif isinstance(arr_type, IntType):
            return "I"
        elif isinstance(arr_type, FloatType):
            return "F"
        elif isinstance(arr_type, BoolType):
            return "Z"
        elif isinstance(arr_type, StringType):
            return "Ljava/lang/String;"
        else:
            raise IllegalOperandException(f"Unsupported array element type: {arr_type}")

    def visit_binary_op(self, node: "BinaryOp", o):
        frame = self._get_frame(o)
        sym = self._get_sym(o)
        op = node.operator


        if op == ">>":
            left_code, left_type = self.visit(node.left, Access(frame, sym))
            function_name = ""
            existing_args = []
            if isinstance(node.right, Identifier):
                function_name = node.right.name
                existing_args = []
            elif isinstance(node.right, FunctionCall):
                function_name = node.right.function.name
                existing_args = node.right.args
            else:
                raise IllegalOperandException(
                    f"Right operand of '>>' must be a function name or call, not {type(node.right)}")

            function_symbol = next((s for s in sym if s.name == function_name), None)
            if not function_symbol or not isinstance(function_symbol.type, FunctionType):
                raise IllegalOperandException(f"'{function_name}' is not a function.")

            # In code ra trực tiếp
            self.emit.print_out(left_code)
            for arg in existing_args:
                arg_code, _ = self.visit(arg, Access(frame, sym))
                self.emit.print_out(arg_code)
            self.emit.print_out(
                self.emit.emit_invoke_static(f"{self.class_name}/{function_name}", function_symbol.type, frame)
            )
            # Trả về chuỗi rỗng vì đã in xong
            return "", function_symbol.type.return_type

        if op in ["&&", "||"]:
            left_code, left_type = self.visit(node.left, Access(frame, sym))
            label_check = frame.get_new_label()
            label_false = frame.get_new_label()
            label_end = frame.get_new_label()

            self.emit.print_out(left_code)
            if op == "&&":
                self.emit.print_out(self.emit.emit_if_false(label_false, frame))
                right_code, _ = self.visit(node.right, Access(frame, sym))
                self.emit.print_out(right_code)
                self.emit.print_out(self.emit.emit_if_false(label_false, frame))
                self.emit.print_out(self.emit.emit_push_iconst(1, frame))
                self.emit.print_out(self.emit.emit_goto(label_end, frame))
            else:  # op == "||"
                self.emit.print_out(self.emit.emit_if_false(label_check, frame))
                self.emit.print_out(self.emit.emit_push_iconst(1, frame))
                self.emit.print_out(self.emit.emit_goto(label_end, frame))
                self.emit.print_out(self.emit.emit_label(label_check, frame))
                right_code, _ = self.visit(node.right, Access(frame, sym))
                self.emit.print_out(right_code)
                self.emit.print_out(self.emit.emit_if_false(label_false, frame))
                self.emit.print_out(self.emit.emit_push_iconst(1, frame))
                self.emit.print_out(self.emit.emit_goto(label_end, frame))

            self.emit.print_out(self.emit.emit_label(label_false, frame))
            self.emit.print_out(self.emit.emit_push_iconst(0, frame))
            self.emit.print_out(self.emit.emit_label(label_end, frame))
            # Trả về chuỗi rỗng vì đã in xong
            return "", BoolType()


        left_code, left_type = self.visit(node.left, Access(frame, sym))
        right_code, right_type = self.visit(node.right, Access(frame, sym))

        # Xử lý nối chuỗi
        if op == '+' and (isinstance(left_type, StringType) or isinstance(right_type, StringType)):
            def _to_string_code(code_str, in_type):
                if isinstance(in_type, StringType):
                    return code_str
                elif isinstance(in_type, IntType):
                    return code_str + "invokestatic io/int2str(I)Ljava/lang/String;\n"
                elif isinstance(in_type, FloatType):
                    return code_str + "invokestatic io/float2str(F)Ljava/lang/String;\n"
                elif isinstance(in_type, BoolType):
                    return code_str + "invokestatic io/bool2str(Z)Ljava/lang/String;\n"
                # Thêm các kiểu khác nếu cần
                return code_str

            str_left_code = _to_string_code(left_code, left_type)
            str_right_code = _to_string_code(right_code, right_type)

            return str_left_code + str_right_code + self.emit.emit_concat(frame), StringType()

        # Xử lý các toán tử số học và quan hệ
        result_type = left_type
        if isinstance(left_type, IntType) and isinstance(right_type, FloatType):
            left_code += self.emit.emit_i2f(frame)
            result_type = FloatType()
        elif isinstance(left_type, FloatType) and isinstance(right_type, IntType):
            right_code += self.emit.emit_i2f(frame)
            result_type = FloatType()
        elif isinstance(left_type, FloatType) and isinstance(right_type, FloatType):
            result_type = FloatType()

        # Nối code của hai vế lại với nhau
        full_code = left_code + right_code

        # Nối tiếp với code của toán tử
        if op in ['+', '-']:
            return full_code + self.emit.emit_add_op(op, result_type, frame), result_type
        elif op in ['*', '/']:
            return full_code + self.emit.emit_mul_op(op, result_type, frame), result_type
        elif op == '%':
            return full_code + self.emit.emit_mod(frame), IntType()
        elif op in ['==', '!=', '<', '<=', '>', '>=']:
            # Lưu ý: kiểu truyền vào emit_relational_op cần là kiểu đã được promote (result_type)
            return full_code + self.emit.emit_relational_op(op, result_type, frame), BoolType()

        raise IllegalOperandException(f"Unsupported operator: {op}")

    def visit_unary_op(self, node: "UnaryOp", o):
        frame = self._get_frame(o)
        sym = self._get_sym(o)
        expr_code, expr_type = self.visit(node.operand, Access(frame, sym))
        op = node.operator

        if op == "-":
            # Trả về code của toán hạng cùng với code phủ định
            return expr_code + self.emit.emit_neg(expr_type, frame), expr_type

        elif op == "+":
            # Dấu cộng không làm gì cả, chỉ cần trả về code của toán hạng
            return expr_code, expr_type

        elif op == "!":
            # Xây dựng chuỗi code cho toán tử NOT và trả về
            label_true = frame.get_new_label()
            label_end = frame.get_new_label()

            code = expr_code
            code += f"ifeq Label{label_true}\n"
            code += "iconst_0\n"  # true -> false
            code += f"goto Label{label_end}\n"
            code += f"Label{label_true}:\n"
            code += "iconst_1\n"  # false -> true
            code += f"Label{label_end}:\n"
            return code, BoolType()

        else:
            raise IllegalOperandException(f"Unsupported unary operator: {op}")

    def visit_function_call(self, node: "FunctionCall", o: Access = None):
        frame = self._get_frame(o)
        sym = self._get_sym(o)

        function_name = node.function.name

        if function_name == "len":
            if len(node.args) != 1:
                raise IllegalOperandException("len function requires exactly one argument")

            arg_code, arg_type = self.visit(node.args[0], Access(frame, sym))

            if not isinstance(arg_type, ArrayType):
                # allow also if symbol is an array reference (some implementations may accept)
                # but safest is to raise
                raise IllegalOperandException("len expects array argument")

            code = arg_code + "arraylength\n"
            return code, IntType()

        function_symbol = next(filter(lambda x: x.name == function_name, sym), False)

        if not function_symbol:
            function_symbol = next(filter(lambda x: x.name == function_name, IO_SYMBOL_LIST), False)

        if not function_symbol:
            raise IllegalOperandException(function_name)

        class_name = function_symbol.value.value if isinstance(function_symbol.value, CName) else self.class_name

        argument_codes = []
        for argument in node.args:
            ac, at = self.visit(argument, Access(frame, sym))
            argument_codes.append(ac)

        # infer return type
        ret_type = (
            function_symbol.type.return_type
            if hasattr(function_symbol.type, "return_type")
            else VoidType()
        )

        # return the concatenated argument code + invoke instruction
        invoke_code = self.emit.emit_invoke_static(class_name + "/" + function_name, function_symbol.type, frame)
        return ("".join(argument_codes) + invoke_code), ret_type

    def visit_array_literal(self, node: "ArrayLiteral", o: Any = None):
        frame = self._get_frame(o)
        sym = self._get_sym(o)

        # Bắt đầu với một chuỗi code rỗng
        code = ""

        elements = getattr(node, "elements", None) or getattr(node, "value", [])
        array_size = len(elements)

        if array_size == 0:
            raise IllegalOperandException("Cannot infer type from empty array literal in this context")

        # Xác định kiểu phần tử từ phần tử đầu tiên
        # Note: Lời gọi visit ở đây chỉ để lấy kiểu, code trả về sẽ không được dùng
        _, first_elem_type = self.visit(elements[0], Access(frame, sym))
        array_type = ArrayType(first_elem_type, array_size)

        # Thêm code để đẩy kích thước mảng lên stack
        code += self.emit.emit_push_iconst(array_size, frame)

        # Thêm code để tạo mảng mới, tương thích với Emitter của bạn
        if isinstance(first_elem_type, IntType):
            code += self.emit.emit_new_array("int")
        elif isinstance(first_elem_type, BoolType):
            code += self.emit.emit_new_array("boolean")
        elif isinstance(first_elem_type, FloatType):
            code += self.emit.emit_new_array("float")
        elif isinstance(first_elem_type, StringType):
            code += "anewarray java/lang/String\n"
        elif isinstance(first_elem_type, ArrayType):
            # Mảng đa chiều: dùng anewarray với descriptor của kiểu con
            descriptor = self.emit.get_jvm_type(first_elem_type)
            code += f"anewarray {descriptor}\n"
        else:
            raise IllegalOperandException(f"Unsupported array element type: {first_elem_type}")

        # Thêm code để gán giá trị cho từng phần tử
        for idx, elem in enumerate(elements):
            # Nhân bản tham chiếu mảng trên stack
            code += "dup\n"
            # Đẩy chỉ số
            code += self.emit.emit_push_iconst(idx, frame)
            # Lấy code của phần tử
            elem_code, elem_type = self.visit(elem, Access(frame, sym))
            code += elem_code

            # Thêm lệnh store phù hợp một cách thủ công
            if isinstance(elem_type, IntType):
                code += "iastore\n"
            elif isinstance(elem_type, BoolType):
                code += "bastore\n"
            elif isinstance(elem_type, FloatType):
                code += "fastore\n"
            elif isinstance(elem_type, (StringType, ArrayType)):
                code += "aastore\n"
            else:
                raise IllegalOperandException(f"Unsupported element type for array store: {elem_type}")

        # Trả về chuỗi code hoàn chỉnh và kiểu của mảng
        return code, array_type

    def visit_identifier(self, node: "Identifier", o: Any = None):
        frame = self._get_frame(o)
        sym = next((x for x in self._get_sym(o) if x.name == node.name), None)
        if not sym:
            raise IllegalOperandException(node.name)

        if isinstance(sym.value, Index):
            code = self.emit.emit_read_var(sym.name, sym.type, sym.value.value, frame)
            return code, sym.type
        elif isinstance(sym.value, CName):
            code = self.emit.emit_get_static(f"{self.class_name}/{sym.name}", sym.type, frame)
            return code, sym.type
        else:
            raise IllegalOperandException(node.name)

    # Literals

    def visit_integer_literal(self, node: "IntegerLiteral", o: Any = None):
        # push integer constant
        frame = self._get_frame(o)
        return self.emit.emit_push_iconst(node.value, frame), IntType()

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        # push float constant
        frame = self._get_frame(o)
        return self.emit.emit_push_fconst(str(node.value), frame), FloatType()

    def visit_boolean_literal(self, node: "BooleanLiteral", o: Any = None):
        frame = self._get_frame(o)
        return self.emit.emit_push_iconst("true" if node.value else "false", frame), BoolType()

    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        frame = self._get_frame(o)
        return (
            self.emit.emit_push_const('"' + node.value + '"', StringType(), frame),
            StringType(),
        )