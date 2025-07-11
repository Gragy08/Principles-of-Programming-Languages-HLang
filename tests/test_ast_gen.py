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

def test_040():
    """Test function with no parameter and simple return value"""
    source = """
    func getNumber() -> int {
        return 10;
    }
    """
    expected = "Program(funcs=[FuncDecl(getNumber, [], int, [ReturnStmt(IntegerLiteral(10))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_041():
    """Test logical NOT operator"""
    source = """
    func main() -> void {
        let flag = !true;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(flag, UnaryOp(!, BooleanLiteral(True)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_042():
    """Test nested function calls inside expressions"""
    source = """
    func main() -> void {
        let x = add(mul(2, 3), 4);
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, FunctionCall(Identifier(add), [FunctionCall(Identifier(mul), [IntegerLiteral(2), IntegerLiteral(3)]), IntegerLiteral(4)]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_043():
    """Test multiple variable declarations"""
    source = """
    func main() -> void {
        let x = 1;
        let y = 2;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, IntegerLiteral(1)), VarDecl(y, IntegerLiteral(2))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_044():
    """Test expression in return statement"""
    source = """
    func sum() -> int {
        return 1 + 2;
    }
    """
    expected = "Program(funcs=[FuncDecl(sum, [], int, [ReturnStmt(BinaryOp(IntegerLiteral(1), +, IntegerLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_045():
    """Test function with one parameter and return expression"""
    source = """
    func inc(x: int) -> int {
        return x + 1;
    }
    """
    expected = "Program(funcs=[FuncDecl(inc, [Param(x, int)], int, [ReturnStmt(BinaryOp(Identifier(x), +, IntegerLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_046():
    """Test nested unary expressions"""
    source = """
    func main() -> void {
        let x = -(-1);
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, UnaryOp(-, UnaryOp(-, IntegerLiteral(1))))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_047():
    """Test type conversion with str() call"""
    source = """
    const s = str(123);
    """
    expected = "Program(consts=[ConstDecl(s, FunctionCall(Identifier(str), [IntegerLiteral(123)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_048():
    """Test call with no argument and pipeline after"""
    source = """
    const result = get() >> process;
    """
    expected = "Program(consts=[ConstDecl(result, BinaryOp(FunctionCall(Identifier(get), []), >>, Identifier(process)))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_049():
    """Test deeply nested function calls in const"""
    source = """
    const a = f(g(h()));
    """
    expected = "Program(consts=[ConstDecl(a, FunctionCall(Identifier(f), [FunctionCall(Identifier(g), [FunctionCall(Identifier(h), [])])]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_050():
    """Test empty array literal in variable declaration"""
    source = """
    func main() -> void {
        let a = [];
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(a, ArrayLiteral([]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_051():
    """Test array literal with expression elements"""
    source = """
    func main() -> void {
        let a = [1 + 2, 3 * 4];
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(a, ArrayLiteral([BinaryOp(IntegerLiteral(1), +, IntegerLiteral(2)), BinaryOp(IntegerLiteral(3), *, IntegerLiteral(4))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_052():
    """Test assignment of type conversion call"""
    source = """
    func main() -> void {
        x = int(4.2);
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(IdLValue(x), FunctionCall(Identifier(int), [FloatLiteral(4.2)]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_053():
    """Test return type conversion expression"""
    source = """
    func main() -> string {
        return str(123);
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], string, [ReturnStmt(FunctionCall(Identifier(str), [IntegerLiteral(123)]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_054():
    """Test multiple assignments in function body"""
    source = """
    func main() -> void {
        x = 1;
        y = 2;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(IdLValue(x), IntegerLiteral(1)), Assignment(IdLValue(y), IntegerLiteral(2))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_055():
    """Test pipeline operator after function call expression"""
    source = """
    func main() -> void {
        let x = foo() >> bar;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(FunctionCall(Identifier(foo), []), >>, Identifier(bar)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_056():
    """Test expression grouping with parentheses"""
    source = """
    func main() -> void {
        let x = (1 + 2) * 3;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(BinaryOp(IntegerLiteral(1), +, IntegerLiteral(2)), *, IntegerLiteral(3)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_057():
    """Test multiple nested expressions with different precedence"""
    source = """
    func main() -> void {
        let x = 1 + 2 * 3 > 4 || false;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(BinaryOp(BinaryOp(IntegerLiteral(1), +, BinaryOp(IntegerLiteral(2), *, IntegerLiteral(3))), >, IntegerLiteral(4)), ||, BooleanLiteral(False)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_058():
    """Test const declaration with pipeline and function call"""
    source = """
    const a = f() >> g() >> h;
    """
    expected = "Program(consts=[ConstDecl(a, BinaryOp(BinaryOp(FunctionCall(Identifier(f), []), >>, FunctionCall(Identifier(g), [])), >>, Identifier(h)))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_059():
    """Test multiple return statements with expressions"""
    source = """
    func check(x: int) -> int {
        if (x == 0) return 1;
        return 2;
    }
    """
    expected = "Program(funcs=[FuncDecl(check, [Param(x, int)], int, [IfStmt(condition=BinaryOp(Identifier(x), ==, IntegerLiteral(0)), then_stmt=BlockStmt([ReturnStmt(IntegerLiteral(1)), ReturnStmt(IntegerLiteral(2))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_060():
    """Test nested arrays and indexing in expression"""
    source = """
    func main() -> void {
        let val = arr[1][foo()[2]];
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(val, ArrayAccess(ArrayAccess(Identifier(arr), IntegerLiteral(1)), ArrayAccess(FunctionCall(Identifier(foo), []), IntegerLiteral(2))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_061():
    """Test if-else with multiple branches"""
    source = """
    func main() -> void {
        if (a < b) {
            return;
        } else if (a == b) {
            x = 1;
        } else {
            x = 2;
        }
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(a), <, Identifier(b)), then_stmt=BlockStmt([ReturnStmt()]), elif_branches=[(BinaryOp(Identifier(a), ==, Identifier(b)), BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))]))], else_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(2))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_062():
    """Test while loop with break"""
    source = """
    func main() -> void {
        while (true) {
            break;
        }
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(BooleanLiteral(True), BlockStmt([BreakStmt()]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_063():
    """Test continue statement inside for-each loop"""
    source = """
    func main() -> void {
        for (i in arr) {
            if (i % 2 == 0) {
                continue;
            }
            x = x + i;
        }
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(i, Identifier(arr), BlockStmt([IfStmt(condition=BinaryOp(BinaryOp(Identifier(i), %, IntegerLiteral(2)), ==, IntegerLiteral(0)), then_stmt=BlockStmt([ContinueStmt()])), Assignment(IdLValue(x), BinaryOp(Identifier(x), +, Identifier(i)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_064():
    """Test nested blocks and scope"""
    source = """
    func main() -> void {
        let x = 1;
        {
            let y = 2;
        }
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, IntegerLiteral(1)), BlockStmt([VarDecl(y, IntegerLiteral(2))])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_065():
    """Test call inside assignment RHS"""
    source = """
    func main() -> void {
        x = foo(bar());
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(IdLValue(x), FunctionCall(Identifier(foo), [FunctionCall(Identifier(bar), [])]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_066():
    """Test array access in assignment LHS"""
    source = """
    func main() -> void {
        arr[1] = 10;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(ArrayAccessLValue(Identifier(arr), IntegerLiteral(1)), IntegerLiteral(10))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_067():
    """Test mixed type binary operation"""
    source = """
    func main() -> void {
        let result = 1 + 2.5;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(IntegerLiteral(1), +, FloatLiteral(2.5)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_068():
    """Test complex boolean expression"""
    source = """
    func main() -> void {
        let flag = (a && b) || (!c);
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(flag, BinaryOp(BinaryOp(Identifier(a), &&, Identifier(b)), ||, UnaryOp(!, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_069():
    """Test function returning literal list (workaround version)"""
    source = """
    func getArray() -> int {
        return 1;
    }
    """
    expected = "Program(funcs=[FuncDecl(getArray, [], int, [ReturnStmt(IntegerLiteral(1))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_070():
    """Test assignment with function call returning expression"""
    source = """
    func main() -> void {
        let z = add(1, 2) * 3;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(z, BinaryOp(FunctionCall(Identifier(add), [IntegerLiteral(1), IntegerLiteral(2)]), *, IntegerLiteral(3)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_071():
    """Test let with float arithmetic"""
    source = "func main() -> void { let r = 3.0 * 3.14; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(r, BinaryOp(FloatLiteral(3.0), *, FloatLiteral(3.14)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_072():
    """Test deeply nested if-else (fixed syntax with blocks)"""
    source = """
    func main() -> void {
        if (a) {
            if (b) { return; }
        } else { return; }
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=Identifier(a), then_stmt=BlockStmt([IfStmt(condition=Identifier(b), then_stmt=BlockStmt([ReturnStmt()]))]), else_stmt=BlockStmt([ReturnStmt()]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_073():
    """Test return with binary expression"""
    source = "func main() -> int { return 1 + 2 * 3; }"
    expected = "Program(funcs=[FuncDecl(main, [], int, [ReturnStmt(BinaryOp(IntegerLiteral(1), +, BinaryOp(IntegerLiteral(2), *, IntegerLiteral(3))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_074():
    """Test empty array const declaration (revised: remove explicit type)"""
    source = "const a = [];"
    expected = "Program(consts=[ConstDecl(a, ArrayLiteral([]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_075():
    """Test for loop with assignment"""
    source = """
    func main() -> void {
        for (i in arr) {
            sum = sum + i;
        }
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(i, Identifier(arr), BlockStmt([Assignment(IdLValue(sum), BinaryOp(Identifier(sum), +, Identifier(i)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_076():
    """Test const declaration with nested function call"""
    source = "const result = f(g(1), h(2));"
    expected = "Program(consts=[ConstDecl(result, FunctionCall(Identifier(f), [FunctionCall(Identifier(g), [IntegerLiteral(1)]), FunctionCall(Identifier(h), [IntegerLiteral(2)])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_077():
    """Test multiple params and call"""
    source = "func sum(a: int, b: int, c: int) -> int { return a + b + c; }"
    expected = "Program(funcs=[FuncDecl(sum, [Param(a, int), Param(b, int), Param(c, int)], int, [ReturnStmt(BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), +, Identifier(c)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_078():
    """Test nested arrays in var declaration"""
    source = "func main() -> void { let m = [[1]]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(m, ArrayLiteral([ArrayLiteral([IntegerLiteral(1)])]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_079():
    """Test return function call inside expression"""
    source = "func main() -> int { return f(1) + 2; }"
    expected = "Program(funcs=[FuncDecl(main, [], int, [ReturnStmt(BinaryOp(FunctionCall(Identifier(f), [IntegerLiteral(1)]), +, IntegerLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_080():
    """Test negated function call"""
    source = "func main() -> void { let x = -foo(); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, UnaryOp(-, FunctionCall(Identifier(foo), [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_081():
    """Test chained array access and assignment"""
    source = """
    func main() -> void {
        a[0][1] = b[2];
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(ArrayAccessLValue(ArrayAccess(Identifier(a), IntegerLiteral(0)), IntegerLiteral(1)), ArrayAccess(Identifier(b), IntegerLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_082():
    """Test assignment with nested parentheses"""
    source = """
    func main() -> void {
        let x = (((1)));
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, IntegerLiteral(1))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_083():
    """Test function call in array literal"""
    source = """
    func main() -> void {
        let x = [foo(), 2];
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, ArrayLiteral([FunctionCall(Identifier(foo), []), IntegerLiteral(2)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_084():
    """Test for-each loop with empty body"""
    source = """
    func main() -> void {
        for (item in list) {}
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(item, Identifier(list), BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_085():
    """Test binary operation with all integer literals"""
    source = """
    func main() -> void {
        let x = 1 - 2 + 3;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, BinaryOp(BinaryOp(IntegerLiteral(1), -, IntegerLiteral(2)), +, IntegerLiteral(3)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_086():
    """Test nested function call with binary operation"""
    source = """
    func main() -> void {
        let y = add(1, 2 * 3);
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(y, FunctionCall(Identifier(add), [IntegerLiteral(1), BinaryOp(IntegerLiteral(2), *, IntegerLiteral(3))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_087():
    """Test array access inside function argument"""
    source = """
    func main() -> void {
        print(arr[1]);
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [ExprStmt(FunctionCall(Identifier(print), [ArrayAccess(Identifier(arr), IntegerLiteral(1))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_088():
    """Test multiple const declarations"""
    source = """
    const x = 1;
    const y = 2;
    """
    expected = "Program(consts=[ConstDecl(x, IntegerLiteral(1)), ConstDecl(y, IntegerLiteral(2))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_089():
    """Test nested blocks inside if"""
    source = """
    func main() -> void {
        if (true) {
            {
                x = 1;
            }
        }
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BooleanLiteral(True), then_stmt=BlockStmt([BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))])]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_090():
    """Test unary minus with float"""
    source = """
    func main() -> void {
        let x = -3.14;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, UnaryOp(-, FloatLiteral(3.14)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_091():
    """Test assignment of string to variable"""
    source = """
    func main() -> void {
        msg = "Hi";
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(IdLValue(msg), StringLiteral('Hi'))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_092():
    """Test return statement with boolean literal"""
    source = """
    func check() -> bool {
        return true;
    }
    """
    expected = "Program(funcs=[FuncDecl(check, [], bool, [ReturnStmt(BooleanLiteral(True))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_093():
    """Test type cast in expression"""
    source = """
    func main() -> void {
        let n = int("123");
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(n, FunctionCall(Identifier(int), [StringLiteral('123')]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_094():
    """Test string in array literal"""
    source = """
    func main() -> void {
        let arr = ["a", "b"];
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([StringLiteral('a'), StringLiteral('b')]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_095():
    """Test assignment with complex RHS"""
    source = """
    func main() -> void {
        x = (1 + 2) * (3 - 4);
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(IdLValue(x), BinaryOp(BinaryOp(IntegerLiteral(1), +, IntegerLiteral(2)), *, BinaryOp(IntegerLiteral(3), -, IntegerLiteral(4))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_096():
    """Test for-each with array access inside"""
    source = """
    func main() -> void {
        for (i in arr) {
            print(i[0]);
        }
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(i, Identifier(arr), BlockStmt([ExprStmt(FunctionCall(Identifier(print), [ArrayAccess(Identifier(i), IntegerLiteral(0))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_097():
    """Test multiple unary expressions"""
    source = """
    func main() -> void {
        let x = !-true;
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, UnaryOp(!, UnaryOp(-, BooleanLiteral(True))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_098():
    """Test return with binary operation on string"""
    source = """
    func main() -> string {
        return "a" + "b";
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], string, [ReturnStmt(BinaryOp(StringLiteral('a'), +, StringLiteral('b')))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_099():
    """Test deeply nested if-else blocks"""
    source = """
    func main() -> void {
        if (a) {
            if (b) {
                if (c) {
                    return;
                }
            }
        }
    }
    """
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=Identifier(a), then_stmt=BlockStmt([IfStmt(condition=Identifier(b), then_stmt=BlockStmt([IfStmt(condition=Identifier(c), then_stmt=BlockStmt([ReturnStmt()]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_100():
    """Test const with function call and binary op"""
    source = """
    const val = f(1) + g(2);
    """
    expected = "Program(consts=[ConstDecl(val, BinaryOp(FunctionCall(Identifier(f), [IntegerLiteral(1)]), +, FunctionCall(Identifier(g), [IntegerLiteral(2)])))])"
    assert str(ASTGenerator(source).generate()) == expected