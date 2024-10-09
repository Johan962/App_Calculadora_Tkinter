class Stack:
    def __init__(self):
        self.elementos = []
        
    def push(self,dato):
        self.elementos.append(dato)
        
    def pop(self):
        return self.elementos.pop()
    
    def peek(self):
        return self.elementos[-1]
    
    def is_empty(self):
        return len(self.elementos) == 0
    
    def dump(self):
        text = ""
        for item in self.elementos:
            text += f"{item}\n"
        return text
    
    def size(self):
        return len(self.elementos)
    
    def get(self,i):
        return self.elementos[i]
    
    def makeEmpty(self):
        self.elementos = []
        return self.elementos

    #CODIGO ANIADIDO
    def getItems(self):        
        return self.elementos