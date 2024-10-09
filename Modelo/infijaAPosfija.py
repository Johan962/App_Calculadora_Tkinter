from .stack import Stack

class InfijaAPosfija:
    def valPreced(self,s):
        if (s == "r"):
            return 5
        elif (s == "^"):
            return 4
        elif s == "*" or s == "/":
            return 3
        elif s == "+" or s == "-":
            return 2
        else:
            return 1
        
    def parentesisAbierto(self,s):
        if s == ")":
            return "("
        elif s == "]":
            return "["
        else:
            return "{"

    def formatearExpresion(self, expresion):
        cadena = []
        i = 0
        while i < len(expresion):
            if expresion[i] == " ":
                i += 1
                continue
            
            # Si es un dígito, formamos el número completo (puede ser de más de una cifra)
            if expresion[i].isdigit():
                num = ""
                # Reunir todos los dígitos que forman el número
                while i < len(expresion) and (expresion[i].isdigit() or expresion[i] == "."):
                    num += expresion[i]
                    i += 1
                cadena.append(num)  # Agregamos el número completo
            else:
                # Si no es un número (es un operador, paréntesis, etc.), lo agregamos directamente
                cadena.append(expresion[i])
                i += 1
        
        return cadena


    def infijaAPosfija(self, expresion):
        pila = Stack()
        expresion = expresion.strip()
        infijo = self.formatearExpresion(expresion)
        salida = ""
        
        i = 0  # Usamos el índice `i` explícitamente
        while i < len(infijo):
            s = infijo[i]
            
            if s == "+" or s == "-" or s == "*" or s == "/" or s == "^" or s == "r":
                if s == "r":  # Si encontramos el operador raíz cuadrada
                    # Aseguramos que hay un operando después de 'r'
                    if i + 1 < len(infijo) and (infijo[i + 1].isdigit() or infijo[i + 1].isalpha()):
                        # Agregamos el operando seguido de 'r'
                        salida = salida + infijo[i + 1] + " r "
                        i += 2  # Avanzamos el índice para saltar el operando ya procesado
                        continue  # Pasamos al siguiente ciclo, evitando procesar el operando nuevamente
                else:
                    while (not pila.is_empty() and self.valPreced(s) <= self.valPreced(pila.peek())):
                        top = pila.pop()
                        salida = salida + top + " "
                    pila.push(s)
            
            elif s == "(" or s == "[" or s == "{":
                pila.push(s)
            
            elif s == ")" or s == "]" or s == "}":
                while not pila.is_empty() and pila.peek() != self.parentesisAbierto(s):
                    top = pila.pop()
                    if top != "(" and top != "[" and top != "{":
                        salida = salida + top + " "
                pila.pop()
            
            else:  # Procesamos un operando
                salida = salida + s + " "
            
            i += 1  # Avanzamos al siguiente carácter
        
        while not pila.is_empty():
            salida = salida + pila.pop() + " "
            
        return salida.strip()
