from utils import Checker


def test_001():
    """Test a valid program that should pass all checks"""
    source = """
const PI: float = 3.14;
func main() -> void {
    let x: int = 5;
    let y = x + 1;
};
"""
    expected = "Static checking passed"
    # Just check that it doesn't return an error
    assert Checker(source).check_from_source() == expected

def test_002():
    """Test redeclared variable error"""
    source = """
func main() -> void {
    let x: int = 5;
    let x: int = 10;
};
"""
    expected = "Redeclared Variable: x"
    assert Checker(source).check_from_source() == expected

def test_003():
    """Test undeclared identifier error"""
    source = """
func main() -> void {
    let x = y + 1;
};
"""
    expected = "Undeclared Identifier: y"
    assert Checker(source).check_from_source() == expected

def test_004():
    """Test type mismatch error"""
    source = """
func main() -> void {
    let x: int = "hello";
};
"""
    expected = "Type Mismatch In Statement: VarDecl(x, int, StringLiteral('hello'))"
    assert Checker(source).check_from_source() == expected

def test_005():
    """Test no main function error"""
    source = """
func hello() -> void {
    let x: int = 5;
};
"""
    expected = "No Entry Point"
    assert Checker(source).check_from_source() == expected

def test_006():
    """Test break not in loop error"""
    source = """
func main() -> void {
    break;
};
"""
    expected = "Must In Loop: BreakStmt()"
    assert Checker(source).check_from_source() == expected

def test_007():
    """Test undeclared function error"""
    source = """
func foo() -> void {}
func main() -> void {
    foo();
    goo();
};
"""
    expected = "Undeclared Function: goo"
    assert Checker(source).check_from_source() == expected

def test_008():
    """Test undeclared function error with multiple calls"""
    source = """
func main() -> void {
    let x = input();
    let y = input1();
};
"""
    expected = "Undeclared Function: input1"
    assert Checker(source).check_from_source() == expected

def test_025():
    """Test redeclared parameter in function"""
    source = """
const a = 1;
func goo(a: int, b: string) -> void {}
func foo(c: int, b: string, c: float) -> void {}
func main() -> void {}
"""
    expected = "Redeclared Parameter: c"
    assert Checker(source).check_from_source() == expected

def test_030():
    """Test redeclared variable in inner block"""
    source = """
const a = 1;
func main() -> void {
    let a = 1;
    let b = 1;
    {
        let a = 2;
        let a = 1;
    }
};
"""
    expected = "Redeclared Variable: a"
    assert Checker(source).check_from_source() == expected

def test_032():
    """Test valid use of break and continue inside loops"""
    source = """
func main() -> void {
    while(true){
        break;
        let a = 1;
        for(a in [1]){
            break;
        }
        {
            continue;
        }
        break;
    }
};
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_049():
    """Test assignment to undeclared identifier"""
    source = """
func main() -> void {
    a = 1;
};
"""
    expected = "Undeclared Identifier: a"
    assert Checker(source).check_from_source() == expected

def test_052():
    """Test assignment to function name"""
    source = """
const foo = 1;
func main() -> void {
    main = 1;
};
"""
    expected = "Undeclared Identifier: main"
    assert Checker(source).check_from_source() == expected

def test_054():
    """Test recursive call to main (should be undeclared in its own body)"""
    source = """
func main() -> void {
    main();
};
"""
    expected = "Undeclared Function: main"
    assert Checker(source).check_from_source() == expected

def test_073():
    """Test type mismatch in reassignment with different literal types"""
    source = """
func main() -> void {
    let a = 1;
    a = 2;
    a = 1.0;
};
"""
    expected = "Type Mismatch In Statement: Assignment(IdLValue(\"a\"), FloatLiteral(1.0))"
    assert Checker(source).check_from_source() == expected