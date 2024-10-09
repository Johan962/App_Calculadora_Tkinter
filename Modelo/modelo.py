from .infijaAPosfija import InfijaAPosfija
from .evaluarExpresion import EvaluarExpresion
from .undoRedo import UndoRedo
from .checkExpression import CheckExpresion
import re

class Modelo:
    def __init__(self):
        # Inicialización de variables que almacenan el estado de la calculadora
        self.expresion_anterior = ""  # Almacena la expresión anterior para la funcionalidad de deshacer
        self.expresion_result = ""  # Almacena el resultado de la expresión
        self.expresion = ""  # Almacena la expresión actual que el usuario está ingresando
        self.undo_redo = UndoRedo()  # Instancia del manejo de operaciones de deshacer y rehacer
    
    def agregar_operacion(self, valor):
        # Agrega un nuevo valor a la expresión actual
        self.expresion += str(valor)  # Concatenar el valor a la expresión
        self.undo_redo.inputChar(str(valor))  # Agregar el valor al stack de deshacer/rehacer
        self.expresion_anterior = ""  # Reiniciar la expresión anterior al agregar nueva
        self.expresion_result = ""  # Limpiar el resultado al modificar la expresión

    def redo_is_empty(self):
        # Verifica si el stack de rehacer está vacío
        return self.undo_redo.Redo.is_empty()  # Devuelve True si está vacío, de lo contrario False
        
    def redo_operacion(self):
        # Realiza la operación de rehacer
        if self.undo_redo.redo():  # Intenta rehacer la última operación
            self.expresion = self.undo_redo.show()  # Actualiza la expresión con el resultado del rehacer
            return True  # Retorna True si se realizó con éxito
        else:
            return False  # Retorna False si no se puede rehacer
        
    def undo_operacion(self):
        # Realiza la operación de deshacer
        if self.undo_redo.undo():  # Intenta deshacer la última operación
            self.expresion = self.undo_redo.show()  # Actualiza la expresión con el resultado del deshacer
            return True  # Retorna True si se realizó con éxito
        else:
            return False  # Retorna False si no se puede deshacer
    
    def borrar_operacion(self):
        # Borra la expresión actual y guarda la expresión anterior
        self.expresion_anterior = self.expresion  # Guarda la expresión actual antes de borrarla
        self.expresion = ""  # Limpia la expresión actual
        self.undo_redo.make_empty()  # Vacía el stack de deshacer/rehacer
    
    def check_expression(self):
        # Verifica si la expresión actual es válida
        expresion = CheckExpresion()  # Crea una instancia de la clase de validación de expresiones
        if expresion.isCorrectPaCoLla(self.expresion) != 0:  # Verifica si hay errores en la expresión
            return expresion.isCorrectPaCoLla(self.expresion)  # Devuelve el código de error si hay uno
        return 0  # Retorna 0 si la expresión es válida
        
    def calcular_resultado(self):
        # Calcula el resultado de la expresión actual
        try:
            # Reemplaza caracteres especiales con sus equivalentes
            self.expresion = re.sub(u"\u00F7", "/", self.expresion)  # Reemplaza el símbolo de división
            self.expresion = re.sub(u"\u221A", "r", self.expresion)  # Reemplaza el símbolo de raíz
            Infija_posfija = InfijaAPosfija()  # Crea una instancia para convertir expresiones infijas a postfijas
            expresion1 = Infija_posfija.infijaAPosfija(self.expresion)  # Convierte la expresión a notación postfija
            evaluar = EvaluarExpresion()  # Crea una instancia para evaluar la expresión postfija
            resultado = evaluar.evalPostfija(expresion1)  # Evalúa la expresión postfija
            return resultado  # Devuelve el resultado
        except:
            return False  # Retorna False si ocurre un error en el cálculo
        
    def borrar_ultimo(self):
        # Borra el último carácter de la expresión actual
        if len(self.expresion) > 0:  # Solo si la expresión no está vacía
            self.undo_redo.undo()  # Llama a la operación de deshacer para actualizar el estado
            self.expresion = self.expresion[:-1]  # Elimina el último carácter de la expresión

    def recuperar_texto_secundario(self):
        # Recupera el resultado almacenado
        return self.expresion_result  # Devuelve el resultado de la expresión
    
    def guardar_texto_secundario(self, texto):
        # Guarda el resultado en la variable correspondiente
        self.expresion_result = texto  # Actualiza el resultado con el nuevo texto
