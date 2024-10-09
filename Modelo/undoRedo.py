from .stack import Stack
class UndoRedo:
    def __init__(self):
        self.Undo = Stack()
        self.Redo = Stack()
    
    def inputChar(self,c):
        self.Undo.push(c)
        self.Redo.makeEmpty()
        
    def undo(self):
        if self.Undo.is_empty():
            print("undo: (pila Undo vacia)")
            return False
        else:
            X = self.Undo.pop()
            self.Redo.push(X)
            return True
    def redo(self):
        if self.Redo.is_empty():
            print("redo: (pila Redo vacia)")
            return False
        else:
            X = self.Redo.pop()
            self.Undo.push(X)
            return True
    def show(self):
        values = ""
        for i in range(self.Undo.size()):
            values += self.Undo.get(i)
        return values
    def simulate(self, L):
        N = len(L)
        for i in range(N):
            if L[i] == "undo":
                self.undo()
            elif L[i] == "redo":
                self.redo()
            else:
                self.inputChar(L[i].strip())
            
        result = self.show()    
        self.Undo.makeEmpty()
        return result
    
    def make_empty(self):
        self.Undo.makeEmpty()
        self.Redo.makeEmpty()
        
