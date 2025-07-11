from utils import ASTGenerator


def test_001():
    """Test basic constant declaration AST generation"""
    source = "const x: int = 42;"
    expected = "Program(consts=[ConstDecl(x, int, IntegerLiteral(42))])"
    # Just check that it doesn't return an error
    assert str(ASTGenerator(source).generate()) == expected


def test_002():
    """Test function declaration AST generation"""
    source = "func main() -> void {}"
    expected = "Program(funcs=[FuncDecl(main, [], void, [])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_003():
    """Test function with parameters AST generation"""
    source = "func add(a: int, b: int) -> int { return a + b; }"
    expected = "Program(funcs=[FuncDecl(add, [Param(a, int), Param(b, int)], int, [ReturnStmt(BinaryOp(Identifier(a), +, Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_004():
    """Test multiple declarations AST generation"""
    source = """const PI: float = 3.14;
    func square(x: int) -> int { return x * x; }"""
    expected = "Program(consts=[ConstDecl(PI, float, FloatLiteral(3.14))], funcs=[FuncDecl(square, [Param(x, int)], int, [ReturnStmt(BinaryOp(Identifier(x), *, Identifier(x)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_005():
    """Test variable declaration with type inference"""
    source = """func main() -> void { let name = "Alice"; }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(name, StringLiteral('Alice'))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_006():
    """Test if-else statement AST generation"""
    source = """func main() -> void { 
        if (x > 0) { 
            return x;
        } else { 
            return 0;
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([ReturnStmt(Identifier(x))]), else_stmt=BlockStmt([ReturnStmt(IntegerLiteral(0))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_007():
    """Test while loop AST generation"""
    source = """func main() -> void { 
        while (i < 10) { 
            i = i + 1; 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(BinaryOp(Identifier(i), <, IntegerLiteral(10)), BlockStmt([Assignment(IdLValue(i), BinaryOp(Identifier(i), +, IntegerLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_008():
    """Test array operations AST generation"""
    source = """func main() -> void { 
        let arr = [1, 2, 3];
        let first = arr[0];
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])), VarDecl(first, ArrayAccess(Identifier(arr), IntegerLiteral(0)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_009():
    """Test pipeline operator AST generation"""
    source = """func main() -> void { 
        let result = data >> process;
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(Identifier(data), >>, Identifier(process)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_010():
    """Test logical OR and pipeline operator precedence in const declarations"""
    source = """
        const a = 1 || 2;
        const a = 1 || 2 || 3;
        const a = 1 >> 2 || 3;
    """
    expected = "Program(consts=[" \
               "ConstDecl(a, BinaryOp(IntegerLiteral(1), ||, IntegerLiteral(2))), " \
               "ConstDecl(a, BinaryOp(BinaryOp(IntegerLiteral(1), ||, IntegerLiteral(2)), ||, IntegerLiteral(3))), " \
               "ConstDecl(a, BinaryOp(IntegerLiteral(1), >>, BinaryOp(IntegerLiteral(2), ||, IntegerLiteral(3))))" \
               "])"
    assert str(ASTGenerator(source).generate()) == expected


def test_011():
    """Test array operations AST generation (revised for consistency)"""
    source = """func main() -> void {
        let arr = [1, 2, 3];
        let first = arr[0];
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])), VarDecl(first, ArrayAccess(Identifier(arr), IntegerLiteral(0)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_012():
    """Test basic constant declaration AST generation"""
    source = "const x: int = 42;"
    expected = "Program(consts=[ConstDecl(x, int, IntegerLiteral(42))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_013():
    """Test function declaration AST generation"""
    source = "func main() -> void {}"
    expected = "Program(funcs=[FuncDecl(main, [], void, [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_014():
    """Test function with parameters AST generation"""
    source = "func add(a: int, b: int) -> int { return a + b; }"
    expected = "Program(funcs=[FuncDecl(add, [Param(a, int), Param(b, int)], int, [ReturnStmt(BinaryOp(Identifier(a), +, Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_015():
    """Test variable declaration with type inference"""
    source = """func main() -> void { let name = "Alice"; }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(name, StringLiteral('Alice'))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_016():
    """Test if-else statement AST generation"""
    source = """func main() -> void {
        if (x > 0) {
            return x;
        } else {
            return 0;
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([ReturnStmt(Identifier(x))]), else_stmt=BlockStmt([ReturnStmt(IntegerLiteral(0))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_017():
    """Test while loop AST generation"""
    source = """func main() -> void {
        while (i < 10) {
            i = i + 1;
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(BinaryOp(Identifier(i), <, IntegerLiteral(10)), BlockStmt([Assignment(IdLValue(i), BinaryOp(Identifier(i), +, IntegerLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_018():
    """Test nested function calls"""
    source = """
    func main() -> void {
        outer(inner(5));
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [ExprStmt(FunctionCall(Identifier(outer), [FunctionCall(Identifier(inner), [IntegerLiteral(5)])]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_019():
    """Test function call with multiple arguments"""
    source = "func test() -> void { print(1, true); }"
    expected = "Program(funcs=[FuncDecl(test, [], void, [ExprStmt(FunctionCall(Identifier(print), [IntegerLiteral(1), BooleanLiteral(True)]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_020():
    """Test nested if statements with else-if"""
    source = """
    func main() -> void {
        if (x == 0) {
            x = 1;
        } else if (x == 1) {
            x = 2;
        }
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), ==, IntegerLiteral(0)), then_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))]), elif_branches=[(BinaryOp(Identifier(x), ==, IntegerLiteral(1)), BlockStmt([Assignment(IdLValue(x), IntegerLiteral(2))]))])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_021():
    """Test array literal with mixed types"""
    source = """
    func main() -> void {
        let arr = [1, true, "hello"];
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), BooleanLiteral(True), StringLiteral('hello')]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_022():
    """Test function call with arguments"""
    source = "func test() -> void { print(1, true); }"
    expected = "Program(funcs=[FuncDecl(test, [], void, [ExprStmt(FunctionCall(Identifier(print), [IntegerLiteral(1), BooleanLiteral(True)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_023():
    """Test nested if statements with else if"""
    source = """
    func main() -> void {
        if (x == 0) {
            x = 1;
        } else if (x == 1) {
            x = 2;
        }
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), ==, IntegerLiteral(0)), then_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))]), elif_branches=[(BinaryOp(Identifier(x), ==, IntegerLiteral(1)), BlockStmt([Assignment(IdLValue(x), IntegerLiteral(2))]))])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_024():
    """Test array literal with mixed types"""
    source = """
    func main() -> void {
        let arr = [1, true, "hello"];
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), BooleanLiteral(True), StringLiteral('hello')]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_025():
    """Test unary operators"""
    source = """
    func main() -> void {
        let x = -5;
        let y = !true;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, UnaryOp(-, IntegerLiteral(5))), VarDecl(y, UnaryOp(!, BooleanLiteral(True)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_026():
    """Test complex binary expression"""
    source = """
    func main() -> void {
        let result = 5 + 3 * 2 - 1;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(BinaryOp(IntegerLiteral(5), +, BinaryOp(IntegerLiteral(3), *, IntegerLiteral(2))), -, IntegerLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_027():
    """Test function with array type parameter"""
    source = "func process(arr: [int; 5]) -> void {}"
    expected = "Program(funcs=[FuncDecl(process, [Param(arr, [int; 5])], void, [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_028():
    """Test nested array access"""
    source = """
    func main() -> void {
        let x = arr[1][2];
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, ArrayAccess(ArrayAccess(Identifier(arr), IntegerLiteral(1)), IntegerLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_029():
    """Test logical and relational expressions"""
    source = """
    func main() -> void {
        let result = x < 10 && y >= 5;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(BinaryOp(Identifier(x), <, IntegerLiteral(10)), &&, BinaryOp(Identifier(y), >=, IntegerLiteral(5))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_030():
    """Test constant declaration with string type"""
    source = 'const greeting: string = "Hello, World!";'
    expected = "Program(consts=[ConstDecl(greeting, string, StringLiteral('Hello, World!'))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_031():
    """Test function with multiple return statements"""
    source = """
    func main() -> int {
        if (x > 0) { return 1; }
        return 0;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], int, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([ReturnStmt(IntegerLiteral(1))])), ReturnStmt(IntegerLiteral(0))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_032():
    """Test empty block statement"""
    source = "func main() -> void {}"
    expected = "Program(funcs=[FuncDecl(main, [], void, [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_033():
    """Test assignment to array element"""
    source = """
    func main() -> void {
        arr[0] = 42;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(ArrayAccessLValue(Identifier(arr), IntegerLiteral(0)), IntegerLiteral(42))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_034():
    """Test chained pipeline operator in const declarations"""
    source = """
        const a = 1 >> 2;
        const a = 1 >> 2 >> 3;
    """
    expected = "Program(consts=[" \
               "ConstDecl(a, BinaryOp(IntegerLiteral(1), >>, IntegerLiteral(2))), " \
               "ConstDecl(a, BinaryOp(BinaryOp(IntegerLiteral(1), >>, IntegerLiteral(2)), >>, IntegerLiteral(3)))" \
               "])"
    assert str(ASTGenerator(source).generate()) == expected

def test_035():
    """Test function call expressions inside const declarations"""
    source = """
        const a = int(1);
        const a = float();
        const a = int() + float(1,2);
    """
    expected = "Program(consts=[" \
               "ConstDecl(a, FunctionCall(Identifier(int), [IntegerLiteral(1)])), " \
               "ConstDecl(a, FunctionCall(Identifier(float), [])), " \
               "ConstDecl(a, BinaryOp(FunctionCall(Identifier(int), []), +, FunctionCall(Identifier(float), [IntegerLiteral(1), IntegerLiteral(2)])))" \
               "])"
    assert str(ASTGenerator(source).generate()) == expected

def test_036():
    """Test break, continue and return statements"""
    source = """
        func foo() -> void {
            break;
            continue;
            return;
            return foo()[2];
        }
    """
    expected = "Program(funcs=[FuncDecl(foo, [], void, [" \
               "BreakStmt(), " \
               "ContinueStmt(), " \
               "ReturnStmt(), " \
               "ReturnStmt(ArrayAccess(FunctionCall(Identifier(foo), []), IntegerLiteral(2)))" \
               "])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_037():
    """Test complex nested array assignments and function calls"""
    source = """
        func foo() -> void {
            a = 1;
            a[2] = foo() >> a[2];
            a[a[2]][1+2] = 1;
        }
    """
    expected = "Program(funcs=[FuncDecl(foo, [], void, [" \
               "Assignment(IdLValue(a), IntegerLiteral(1)), " \
               "Assignment(ArrayAccessLValue(Identifier(a), IntegerLiteral(2)), BinaryOp(FunctionCall(Identifier(foo), []), >>, ArrayAccess(Identifier(a), IntegerLiteral(2)))), " \
               "Assignment(ArrayAccessLValue(ArrayAccess(Identifier(a), ArrayAccess(Identifier(a), IntegerLiteral(2))), BinaryOp(IntegerLiteral(1), +, IntegerLiteral(2))), IntegerLiteral(1))" \
               "])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_038():
    """Test nested empty and return blocks"""
    source = """
        func foo() -> void {
            {}
            {
                return;
            }
        }
    """
    expected = "Program(funcs=[FuncDecl(foo, [], void, [BlockStmt([]), BlockStmt([ReturnStmt()])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_039():
    """Test while and for loops including return inside block"""
    source = """
        func foo() -> void {
            while(1 + 2) {}
            for(a in array) {}
            for(a in array) {return;}
        }
    """
    expected = "Program(funcs=[FuncDecl(foo, [], void, [" \
               "WhileStmt(BinaryOp(IntegerLiteral(1), +, IntegerLiteral(2)), BlockStmt([])), " \
               "ForStmt(a, Identifier(array), BlockStmt([])), " \
               "ForStmt(a, Identifier(array), BlockStmt([ReturnStmt()]))" \
               "])])"
    assert str(ASTGenerator(source).generate()) == expected
