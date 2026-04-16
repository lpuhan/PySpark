class FirstVSCodeTest:
     tokenSize = 2048
     def __init__(self,tokenSize):
        print("LLMs class initialized with token size:", self.tokenSize)
     def openai(self):
        return "OpenAI API called",self.tokenSize 
     def azure(self):
        return "Azure API called",self.tokenSize
     def google(self):
        return "Google API called",self.tokenSize   

llm = FirstVSCodeTest(40000)
print(llm.openai())
print(llm.azure())
print(llm.google())




