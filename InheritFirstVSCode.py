# import FirstVSCodeTest as first
from FirstVSCodeTest import llm as first_llm
class InheritFirstVSCode:

    def __init__(self, name,tokenSize):
        self.name = name
        first_llm.__init__(tokenSize)

    def say_hello(self):
        return f"Hello, {self.name}!"
    
inherit = InheritFirstVSCode("Alice",15000)   
print(inherit.say_hello())
# llm = first.FirstVSCodeTest(40000)  
print(first_llm.openai())
print(first_llm.azure())      