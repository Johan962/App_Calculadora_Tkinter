from .stack import Stack
class EvaluarExpresion:
    def evalPostfija(self, expresion):
        pila = Stack()    
        expresion = expresion.strip()
        expresion = expresion.split(" ")
        for i in range(len(expresion)):
            s = expresion[i]
            if s == "+":
                opnd2 = pila.pop()    
                opnd1 = pila.pop()    
                pila.push(opnd1 + opnd2)
            elif s == "-":
                opnd2 = pila.pop()    
                opnd1 = pila.pop()    
                pila.push(opnd1 - opnd2)
                
        ###CODIGO ANIADIDO
            elif s == "*":
                opnd2 = pila.pop()    
                opnd1 = pila.pop()    
                pila.push(opnd1 * opnd2)            
            elif s == "/":
                opnd2 = pila.pop()    
                opnd1 = pila.pop()    
                pila.push(opnd1 / opnd2)     
            elif s == "^":
                opnd2 = pila.pop()
                opnd1 = pila.pop()
                pila.push(opnd1**opnd2)       
            elif s == "r":
                opnd1 = pila.pop()    
                pila.push(opnd1**0.5)                        
            else:
                pila.push(float(s))
        return pila.peek()
