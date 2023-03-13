import ast
import astpretty

class globalsVisitor(ast.NodeVisitor):
    def __init__(self):
        self.globals = set()

    def add_globals_from_subtree(self, node):
        for n in ast.walk(node):
            if type(n) is ast.Name:
                self.globals.add(n.id)

    def visitAssign(self, node):
        for target in node.targets:
            self.add_globals_from_subtree(t)

    def visitAugAssign(self, node):
        self.add_globals_from_subtree(node.target)

    def visitAnnAssign(self, node):
        self.add_globals_from_subtree(node.target)

    
    def generic_visit(self, node):
        astpretty.pprint(ast.parse(node))
        ast.NodeVisitor.generic_visit(self, node)

    def visit_FunctionDef(self, node): pass
    def visit_Lambda(self, node): pass
    def visit_AsyncFunctionDef(self, node): pass
    def visit_ClassDef(self, node): pass
    def visit_comprehension(self, node): pass


tree = ast.parse(source=(open("linterTest.py", "r").read()), filename='linterTest.py')

open("linterTest.py", "r").close()

visitor = globalsVisitor()
visitor.generic_visit(tree)
print(visitor.globals)
