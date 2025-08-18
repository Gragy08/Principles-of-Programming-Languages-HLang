from src.utils.nodes import *

from utils import CodeGenerator


# def test_001():
#     """Test basic print statement"""
#     ast = Program(
#         [],
#         [
#             FuncDecl(
#                 "main",
#                 [],
#                 VoidType(),
#                 [
#                     ExprStmt(
#                         FunctionCall(
#                             Identifier("print"), [StringLiteral("Hello World")]
#                         )
#                     )
#                 ],
#             )
#         ],
#     )
#     expected = "Hello World"
#     result = CodeGenerator().generate_and_run(ast)
#     assert result == expected

def test_001():
    source = """
func main() -> void {
    print("Hello World");
}
"""
    expected = "Hello World"
    assert CodeGenerator().generate_and_run(source) == expected
def test_002():
    source = """
func main() -> void {
    print(int2str(1));
}
"""
    expected = "1"
    assert CodeGenerator().generate_and_run(source) == expected
def test_009():
    source = """
func main() -> void {
    let i: float = 1.0 - 2;
    print(float2str(i));
}
"""
    expected = "-1.0"
    assert CodeGenerator().generate_and_run(source) == expected
def test_012():
    source = """
func main() -> void {
    let i: int = 3 / 2;
    print(int2str(i));
}
"""
    expected = "1"
    assert CodeGenerator().generate_and_run(source) == expected
    
def test_023():
    source = """
func main() -> void {
    print(bool2str("s1" != "s1"));
}
"""
    expected = "false"
    assert CodeGenerator().generate_and_run(source) == expected