from .stack import Stack
import re
class CheckExpresion:
    def isCorrectPaCoLla(self, expresion):
        # Verifica balance de paréntesis
        if not self.balance_parentesis(expresion):
            return 1
        
        # Verifica que los operadores estén bien posicionados
        if not self.validar_operadores(expresion):
            return 2

        # Verifica números decimales correctos
        if not self.validar_numeros_decimales(expresion):
            return 3

        # Verifica que la expresión no termine con un operador
        if not self.verificar_terminacion(expresion):
            return 4
        
        if not self.isCorrectUnaryOperators(expresion):
            return 5
        
        return 0

    def balance_parentesis(self, expresion):
        pila = Stack()
        for i in range(len(expresion)):
            c = expresion[i]
            
            if c == "(" or c == "[" or c == "{": #codigo cambiado
                pila.push(c)
            elif c == ")":
                if pila.is_empty() or pila.pop() != "(":
                    return False
            #codigo aumentado
            elif c == "]": 
                if pila.is_empty() or pila.pop() != "[":
                    return False
            elif c == "}":
                if pila.is_empty() or pila.pop() != "{":
                    return False
        if pila.is_empty():
            return True
        else:
            return False

    
    def isCorrectUnaryOperators(self, expression):
        # Reemplazar raíz cuadrada por símbolo "r" para simplificar validación
        expression = re.sub(u"\u221A", "r", expression)
        
        # Dividir la expresión en tokens (operadores y operandos)
        tokens = re.findall(r'[+\-*/(){}[\]r]|\d+|\.\d+', expression)
        
        for i, token in enumerate(tokens):
            if token == 'r':
                # Raíz cuadrada debe ir seguida de un número o una expresión válida
                if i + 1 >= len(tokens) or not re.match(r'[\d({[]', tokens[i + 1]):
                    return False
            
            elif token == '-':
                # Verificar si es un operador unario o binario
                if i == 0:  # Si es el primer token, es unario
                    continue
                elif tokens[i - 1] in "+-*/({[":  # Sigue a un operador binario o paréntesis de apertura
                    continue  # Es un unario válido
                elif tokens[i - 1].isdigit() or tokens[i - 1] in ')]}':  # Sigue a un número o paréntesis de cierre
                    continue  # Es un operador binario válido
                else:
                    return False  # No es un uso correcto de "-"
        
        return True
    
    def validar_operadores(self, expresion):
        # Verifica que los operadores binarios no estén al inicio o fin, ni estén consecutivos
        operadores = "+-*/"
        expresion = expresion.replace(" ", "")  # Eliminar espacios
        if expresion[0] in operadores or expresion[-1] in operadores:
            return False

        for i in range(1, len(expresion)):
            if expresion[i] in operadores and expresion[i-1] in operadores:
                return False
        return True

    def validar_numeros_decimales(self, expresion):
        # Expresión regular que permite solo un punto decimal por número, raíz cuadrada y potencias
        pattern = r'^\s*([-+]?(?:\d+(\.\d+)?|\.\d+)(\s*[\+\-\*/\^]\s*[-+]?(?:\d+(\.\d+)?|\.\d+))*|√\s*([-+]?(?:\d+(\.\d+)?|\.\d+))(\s*[\+\-\*/\^]\s*[-+]?(?:\d+(\.\d+)?|\.\d+))*\s*)$'
        return bool(re.match(pattern, expresion))

    
    def verificar_terminacion(self, expresion):
        # No debe terminar con un operador binario
        operadores = "+-*/"
        if expresion[-1] in operadores:
            return False
        return True

              
