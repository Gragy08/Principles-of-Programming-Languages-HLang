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
    """Test type mismatch with reassignment of different type"""
    source = """
    func main() -> void {
        let a = 1;
        a = 2;
        a = 1.0;
    }
    """
    expected = "Type Mismatch In Statement: Assignment(IdLValue(a), FloatLiteral(1.0))"
    assert Checker(source).check_from_source() == expected

def test_075():
    source = """
    func TIEN() -> void {return;return 1;}
    func main() -> void {}
    """
    expected = "Type Mismatch In Statement: ReturnStmt(IntegerLiteral(1))"
    assert Checker(source).check_from_source() == expected

def test_079():
    source = """
    func TIEN(a: int) -> void {
        let i = a;
        let j: int = a;
        a = 1;
    }
    func main() -> void {}
    """
    expected = "Type Mismatch In Statement: Assignment(IdLValue(a), IntegerLiteral(1))"
    assert Checker(source).check_from_source() == expected

def test_086():
    source = """
    const array = [[1], [2]];
    func main() -> void {
        for (a in array) {
            a = [2];
            a = [1,2];
        }
    }
    """
    expected = "Type Mismatch In Statement: Assignment(IdLValue(a), ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]))"
    assert Checker(source).check_from_source() == expected

def test_094():
    """Test return value in void function"""
    source = """
    func main() -> void {
        return 1;
    }
    """
    expected = "Type Mismatch In Statement: ReturnStmt(IntegerLiteral(1))"
    assert Checker(source).check_from_source() == expected

def test_097():
    """Test assign function to variable (should fail: cannot assign function value)"""
    source = """
    func foo() -> int {return 1;}
    func main() -> void {
        let a = foo;
    }
    """
    expected = "Undeclared Identifier: foo"
    assert Checker(source).check_from_source() == expected

def test_102():
    """Test type mismatch when assigning float expression to int variable"""
    source = """
    func main() -> void {
        let a: float = 1 - 1.0;
        let b: float = 1.0 + 1;
        let c: float = 1.0 + 1.0;
        let d: int = 1.0 - 1;
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(d, int, BinaryOp(FloatLiteral(1.0), -, IntegerLiteral(1)))"
    assert Checker(source).check_from_source() == expected

def test_104():
    source = """
func main() -> void {
    let a: int = 1 % 2;
    let b: float = 1 % 2;
}
"""
    expected = "Type Mismatch In Statement: VarDecl(b, float, BinaryOp(IntegerLiteral(1), %, IntegerLiteral(2)))"
    assert Checker(source).check_from_source() == str(expected)

def test_106():
    source = """
func main() -> void {
    let a: bool = 1 == 1;
    let b: bool = 1.0 != 1.0;
    let c: bool = 1 == 1.0;
    let d: bool = 1.0 != 1;
    let e: bool = "a" != "b";
    let f: bool = true == false;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == str(expected)

def test_109():
    source = """
func main() -> void {
    let a: bool = 1 >= 1;
    let b: bool = 1.0 <= 1.0;
    let c: bool = 1 > 1.0;
    let d: bool = 1.0 < 1;
    let e: bool = "a" <= "b";
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == str(expected)

def test_112():
    source = """
func main() -> void {
    let a: int = true < false;
}
"""
    expected = "Type Mismatch In Expression: BinaryOp(BooleanLiteral(True), <, BooleanLiteral(False))"
    assert Checker(source).check_from_source() == str(expected)

def test_116():
    source = """
func main() -> void {
    let a: int = -+-+1;
    let b: float = -+-+1.0;
    let c: float = -1;
}
"""
    expected = "Type Mismatch In Statement: VarDecl(c, float, UnaryOp(-, IntegerLiteral(1)))"
    assert Checker(source).check_from_source() == str(expected)

def test_119():
    source = """
func main() -> void {
    let a: bool = !!true;
    let b: int = !!true;
}
"""
    expected = "Type Mismatch In Statement: VarDecl(b, int, UnaryOp(!, UnaryOp(!, BooleanLiteral(True))))"
    assert Checker(source).check_from_source() == str(expected)

def test_121():
    source = """
func main() -> void {
    let a = [1, 1.0];
}
"""
    expected = "Type Mismatch In Expression: ArrayLiteral([IntegerLiteral(1), FloatLiteral(1.0)])"
    assert Checker(source).check_from_source() == str(expected)

def test_126():
    source = """
func main() -> void {
    let a: [int; 1] = [];
}
"""
    expected = "Type Mismatch In Statement: VarDecl(a, ArrayType(int, 1), ArrayLiteral([]))"
    assert Checker(source).check_from_source() == str(expected)