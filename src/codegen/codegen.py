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
        sym = self._get_sym(o)

        # ----- 1) Determine variable type (infer if annotation missing) -----
        if node.type_annotation is not None:
            var_type = node.type_annotation
        else:
            # infer type from literal/expression WITHOUT emitting
            # simple inference: literals, arrayliteral, identifier, arrayaccess
            def infer_type(n):
                if isinstance(n, IntegerLiteral):
                    return IntType()
                if isinstance(n, FloatLiteral):
                    return FloatType()
                if isinstance(n, BooleanLiteral):
                    return BoolType()
                if isinstance(n, StringLiteral):
                    return StringType()
                if isinstance(n, ArrayLiteral):
                    elems = getattr(n, "elements", None) or getattr(n, "value", None)
                    if not elems:
                        raise IllegalOperandException("Cannot infer type of empty array literal")
                    # infer element type recursively
                    first_type = infer_type(elems[0]) if not isinstance(elems[0], Identifier) else \
                        (next((s.type for s in sym if s.name == elems[0].name), None) or self._get_frame(
                            o) and self.visit(elems[0], Access(Frame("<infer>", VoidType()), sym)[0]))
                    return ArrayType(first_type, len(elems))
                if isinstance(n, Identifier):
                    s = next((x for x in sym if x.name == n.name), None)
                    if not s:
                        raise IllegalOperandException(n.name)
                    return s.type
                if isinstance(n, ArrayAccess):
                    # infer array type then return element type
                    if isinstance(n.array, Identifier):
                        s = next((x for x in sym if x.name == n.array.name), None)
                        if not s:
                            raise IllegalOperandException(n.array.name)
                        arr_type = s.type
                    else:
                        # fallback: try to infer recursively
                        arr_type = infer_type(n.array)
                    if not isinstance(arr_type, ArrayType):
                        raise IllegalOperandException("Cannot index into non-array type")
                    return arr_type.element_type
                # fallback: as last resort, call visitor to get type (but this may emit)
                _, t = self.visit(n, Access(frame, sym))
                return t

            if node.value is None:
                raise IllegalOperandException(f"Cannot infer type for variable '{node.name}' without initializer")
            var_type = infer_type(node.value)

        # ----- 2) allocate local variable slot with known type -----
        idx = frame.get_new_index()
        self.emit.print_out(
            self.emit.emit_var(
                idx,
                node.name,
                var_type,
                frame.get_start_label(),
                frame.get_end_label(),
            )
        )

        # add symbol (so Assignment/initializer can find it)
        new_sym = [Symbol(node.name, var_type, Index(idx))] + o.sym

        # ----- 3) handle initializer (if any) -----
        if node.value is not None:
            # If initializer is ArrayLiteral we may handle specially (array creation + write_var)
            if isinstance(node.value, ArrayLiteral):
                code, typ = self.visit(node.value, Access(frame, new_sym))
                self.emit.print_out(code)
                self.emit.print_out(self.emit.emit_write_var(node.name, typ, idx, frame))
            else:
                # Use assignment visitor which expects variable symbol to exist
                self.visit(
                    Assignment(IdLValue(node.name), node.value),
                    SubBody(frame, new_sym),
                )

        return SubBody(
            frame,
            new_sym,
        )

    def visit_array_access(self, node: "ArrayAccess", o):
        frame = self._get_frame(o)
        sym = self._get_sym(o)

        # Lấy code cho mảng và chỉ số, nhưng KHÔNG IN
        arr_code, arr_type = self.visit(node.array, Access(frame, sym))
        idx_code, idx_type = self.visit(node.index, Access(frame, sym))

        # Xây dựng chuỗi code hoàn chỉnh
        full_code = arr_code + idx_code

        if not isinstance(arr_type, ArrayType):
            raise IllegalOperandException(f"Cannot index into non-array type: {arr_type}")

        # SỬA ĐỔI: Tách riêng logic cho IntType và BoolType
        inner_type = arr_type.element_type
        if isinstance(inner_type, IntType):
            full_code += "iaload\n"
        elif isinstance(inner_type, BoolType):
            full_code += "baload\n"  # Dùng baload cho mảng boolean
        elif isinstance(inner_type, FloatType):
            full_code += "faload\n"
        else:  # StringType, ArrayType
            full_code += "aaload\n"

        # Trả về chuỗi code và kiểu của phần tử
        return full_code, inner_type

    def visit_assignment(self, node: "Assignment", o: SubBody = None):
        frame = self._get_frame(o)
        sym = self._get_sym(o)

        # Xử lý gán cho phần tử mảng: a[i] = value
        if isinstance(node.lvalue, ArrayAccessLValue):
            # Bước 1: Lấy code cho các thành phần
            arr_code, arr_type = self.visit(node.lvalue.array, Access(frame, sym))
            idx_code, idx_type = self.visit(node.lvalue.index, Access(frame, sym))
            rhs_code, rhs_type = self.visit(node.value, Access(frame, sym))

            # SỬA ĐỔI: Thêm logic clone() ngay tại đây, giống như đã làm ở test_101
            if isinstance(rhs_type, ArrayType):
                array_descriptor = self.emit.get_jvm_type(rhs_type)
                rhs_code += f"\tinvokevirtual {array_descriptor}/clone()Ljava/lang/Object;\n"
                rhs_code += f"\tcheckcast {array_descriptor}\n"

            # Bước 2: In code ra theo đúng thứ tự: array_ref -> index -> value
            self.emit.print_out(arr_code)
            self.emit.print_out(idx_code)
            self.emit.print_out(rhs_code)

            # Bước 3: In lệnh store phù hợp
            elem_type = arr_type.element_type
            if isinstance(elem_type, IntType):
                self.emit.print_out("iastore\n")
            elif isinstance(elem_type, BoolType):
                self.emit.print_out("bastore\n")
            elif isinstance(elem_type, FloatType):
                self.emit.print_out("fastore\n")
            else:  # String, Array
                self.emit.print_out("aastore\n")

        # Xử lý gán cho biến thông thường: x = value
        else:
            rhs_code, rhs_type = self.visit(node.value, Access(frame, sym))

            # Logic clone() cho trường hợp let b = a; (đã có từ lần sửa trước)
            if isinstance(rhs_type, ArrayType):
                array_descriptor = self.emit.get_jvm_type(rhs_type)
                rhs_code += f"\tinvokevirtual {array_descriptor}/clone()Ljava/lang/Object;\n"
                rhs_code += f"\tcheckcast {array_descriptor}\n"

            # In code của vế phải
            self.emit.print_out(rhs_code)

            # Lấy và in code của vế trái (lệnh store)
            lhs_code, _ = self.visit(node.lvalue, Access(frame, sym))
            self.emit.print_out(lhs_code)

        return o

    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        frame = self._get_frame(o)
        sym = self._get_sym(o)

        # Sinh code cho điều kiện và IN ra ngay
        cond_code, _ = self.visit(node.condition, Access(frame, sym))
        self.emit.print_out(cond_code)

        end_label = frame.get_new_label()
        else_label = frame.get_new_label()

        self.emit.print_out(self.emit.emit_if_false(else_label, frame))

        # Then block
        self.visit(node.then_stmt, o)
        self.emit.print_out(self.emit.emit_goto(end_label, frame))

        self.emit.print_out(self.emit.emit_label(else_label, frame))

        # Elif/Else block (giả sử AST có cấu trúc elif_branches và else_stmt)
        if hasattr(node, 'elif_branches') and node.elif_branches:
            # Tương tự, cần visit và print code cho điều kiện của elif
            for condition, body in node.elif_branches:
                next_branch_label = frame.get_new_label()
                cond_code, _ = self.visit(condition, Access(frame, sym))
                self.emit.print_out(cond_code)
                self.emit.print_out(self.emit.emit_if_false(next_branch_label, frame))
                self.visit(body, o)
                self.emit.print_out(self.emit.emit_goto(end_label, frame))
                self.emit.print_out(self.emit.emit_label(next_branch_label, frame))

        if node.else_stmt:
            self.visit(node.else_stmt, o)

        self.emit.print_out(self.emit.emit_label(end_label, frame))
        return o

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        frame = self._get_frame(o)
        sym = self._get_sym(o)

        cond_label = frame.get_new_label()
        end_label = frame.get_new_label()

        prev_break_label = getattr(frame, "_break_label", None)
        prev_continue_label = getattr(frame, "_continue_label", None)
        frame._break_label = end_label
        frame._continue_label = cond_label

        self.emit.print_out(self.emit.emit_label(cond_label, frame))

        # Sinh code cho điều kiện và IN ra
        cond_code, _ = self.visit(node.condition, Access(frame, sym))
        self.emit.print_out(cond_code)

        self.emit.print_out(self.emit.emit_if_false(end_label, frame))

        self.visit(node.body, SubBody(frame, sym))

        self.emit.print_out(self.emit.emit_goto(cond_label, frame))
        self.emit.print_out(self.emit.emit_label(end_label, frame))

        frame._break_label = prev_break_label
        frame._continue_label = prev_continue_label

        return o

    # ✅ SỬA LỖI: Thay thế toàn bộ hàm visit_for_stmt bằng phiên bản cuối cùng này.
    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        frame = self._get_frame(o)
        sym = self._get_sym(o)

        # BƯỚC 1: Xử lý collection
        col_code, col_type = self.visit(node.iterable, Access(frame, sym))
        self.emit.print_out(col_code)

        arr_tmp_idx = frame.get_new_index()
        arr_tmp_name = f"__arr_for_{arr_tmp_idx}"
        self.emit.print_out(
            self.emit.emit_var(arr_tmp_idx, arr_tmp_name, col_type, frame.get_start_label(), frame.get_end_label()))
        self.emit.print_out(self.emit.emit_write_var(arr_tmp_name, col_type, arr_tmp_idx, frame))

        # BƯỚC 2: Tạo biến index tạm và khởi tạo bằng 0
        idx_tmp_idx = frame.get_new_index()
        idx_tmp_name = f"__idx_for_{idx_tmp_idx}"
        self.emit.print_out(
            self.emit.emit_var(idx_tmp_idx, idx_tmp_name, IntType(), frame.get_start_label(), frame.get_end_label()))
        self.emit.print_out(self.emit.emit_push_iconst(0, frame))
        self.emit.print_out(self.emit.emit_write_var(idx_tmp_name, IntType(), idx_tmp_idx, frame))

        # BƯỚC 3: Thiết lập các label và context cho break/continue
        start_label = frame.get_new_label()
        end_label = frame.get_new_label()
        continue_target_label = frame.get_new_label()

        prev_break = getattr(frame, "_break_label", None)
        prev_continue = getattr(frame, "_continue_label", None)
        frame._break_label = end_label
        frame._continue_label = continue_target_label

        # BƯỚC 4: Bắt đầu vòng lặp, kiểm tra điều kiện
        self.emit.print_out(self.emit.emit_label(start_label, frame))
        self.emit.print_out(self.emit.emit_read_var(idx_tmp_name, IntType(), idx_tmp_idx, frame))
        self.emit.print_out(self.emit.emit_read_var(arr_tmp_name, col_type, arr_tmp_idx, frame))

        # ✅ SỬA LỖI: Sinh bytecode trực tiếp thay vì gọi helper
        self.emit.print_out("arraylength\n")

        # ✅ SỬA LỖI: Sinh bytecode trực tiếp thay vì gọi helper
        self.emit.print_out(f"if_icmpge Label{end_label}\n")

        # BƯỚC 5: Lấy phần tử, gán cho biến lặp và thêm vào symbol table
        self.emit.print_out(self.emit.emit_read_var(arr_tmp_name, col_type, arr_tmp_idx, frame))
        self.emit.print_out(self.emit.emit_read_var(idx_tmp_name, IntType(), idx_tmp_idx, frame))

        elem_type = col_type.element_type
        if isinstance(elem_type, (IntType, BoolType)):
            self.emit.print_out("iaload\n")
        elif isinstance(elem_type, FloatType):
            self.emit.print_out("faload\n")
        else:  # String, Array, etc.
            self.emit.print_out("aaload\n")

        loop_var_name = node.variable
        loop_var_idx = frame.get_new_index()
        self.emit.print_out(
            self.emit.emit_var(loop_var_idx, loop_var_name, elem_type, frame.get_start_label(), frame.get_end_label()))
        self.emit.print_out(self.emit.emit_write_var(loop_var_name, elem_type, loop_var_idx, frame))

        body_sym = [Symbol(loop_var_name, elem_type, Index(loop_var_idx))] + sym

        # BƯỚC 6: Visit thân vòng lặp với symbol table đã cập nhật
        self.visit(node.body, SubBody(frame, body_sym))

        # BƯỚC 7: Cập nhật index và nhảy ngược lại
        self.emit.print_out(self.emit.emit_label(continue_target_label, frame))

        # ✅ SỬA LỖI: Sinh bytecode trực tiếp thay vì gọi helper
        self.emit.print_out(f"iinc {idx_tmp_idx} 1\n")

        self.emit.print_out(self.emit.emit_goto(start_label, frame))

        # BƯỚC 8: Kết thúc vòng lặp
        self.emit.print_out(self.emit.emit_label(end_label, frame))

        # Khôi phục context break/continue
        frame._break_label = prev_break
        frame._continue_label = prev_continue

        return o

    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        frame = self._get_frame(o)
        sym = self._get_sym(o)

        if node.value is None:
            # return không có giá trị => void
            self.emit.print_out(self.emit.emit_return(VoidType(), frame))
        else:
            # return có giá trị => generate code cho expression
            code, typ = self.visit(node.value, Access(frame, sym))
            # IN code của biểu thức ra tại đây
            self.emit.print_out(code)
            self.emit.print_out(self.emit.emit_return(typ, frame))

    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        frame = self._get_frame(o)
        # Dùng getattr để lấy nhãn một cách an toàn, trả về None nếu không có
        break_label = getattr(frame, "_break_label", None)

        if break_label is None:
            raise IllegalRuntimeException("break not in loop")

        self.emit.print_out(self.emit.emit_goto(break_label, frame))
        return o

    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        frame = self._get_frame(o)
        # Dùng getattr để lấy nhãn một cách an toàn
        continue_label = getattr(frame, "_continue_label", None)

        if continue_label is None:
            raise IllegalRuntimeException("continue not in loop")

        self.emit.print_out(self.emit.emit_goto(continue_label, frame))
        return o

    def visit_expr_stmt(self, node: "ExprStmt", o: SubBody = None):
        frame = self._get_frame(o)
        sym = self._get_sym(o)
        code, typ = self.visit(node.expr, Access(frame, sym))
        self.emit.print_out(code)

        # Nếu biểu thức trả về giá trị (không phải void), pop nó khỏi stack
        if not isinstance(typ, VoidType):
            self.emit.print_out(self.emit.emit_pop(frame))

        return o

    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        frame = self._get_frame(o)
        # Lấy bảng ký hiệu gốc của phạm vi cha
        original_sym = self._get_sym(o)

        # 1. Bắt đầu một phạm vi mới trong Frame
        frame.enter_scope(False)

        # Lấy các nhãn cho phạm vi mới này
        start_label = frame.get_start_label()
        end_label = frame.get_end_label()

        # 2. Sinh mã cho nhãn bắt đầu phạm vi
        self.emit.print_out(self.emit.emit_label(start_label, frame))

        # Tạo một môi trường mới cho phạm vi con, kế thừa các ký hiệu của cha
        # Sử dụng [:] hoặc .copy() để tạo một bản sao, tránh ảnh hưởng đến bảng ký hiệu gốc
        inner_env = SubBody(frame, original_sym[:])

        # 3. Duyệt qua các câu lệnh bên trong khối, cập nhật môi trường của phạm vi con
        for stmt in node.statements:
            inner_env = self.visit(stmt, inner_env)

        # 4. Sinh mã cho nhãn kết thúc phạm vi
        self.emit.print_out(self.emit.emit_label(end_label, frame))

        # 5. Kết thúc phạm vi trong Frame
        frame.exit_scope()

        # 6. QUAN TRỌNG: Trả về môi trường với bảng ký hiệu GỐC của phạm vi cha.
        #    Điều này sẽ loại bỏ tất cả các biến đã được khai báo bên trong khối.
        return SubBody(frame, original_sym)
    # Left-values

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
        """
        For lvalue read/write generation:
         - For read contexts, this function should produce code that pushes array element value and returns (code, elem_type)
         - For write contexts, visit_assignment handles storing, so this returns code that pushes arrayref and index (not storing).
        We'll implement as read: push arrref, index, then array load.
        """
        frame = self._get_frame(o)
        sym = self._get_sym(o)

        # assume node has attributes 'array' and 'index'
        ac, at = self.visit(node.array, Access(frame, sym))
        self.emit.print_out(ac)
        ic, it = self.visit(node.index, Access(frame, sym))
        self.emit.print_out(ic)
        elem_type = at.element_type if type(at) is ArrayType else at
        # emit array load
        code = self.emit.emit_aload(elem_type, frame)
        return code, elem_type

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