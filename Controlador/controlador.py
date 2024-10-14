class CalculadoraControlador:
    def __init__(self, modelo, vista):
        # Inicializa el controlador con el modelo y la vista
        self.modelo = modelo
        self.vista = vista

    def click_boton(self, texto, escribir):
        if not escribir:
            # Manejo de acciones cuando no se está escribiendo un número o un operador
            if texto == "=":
                # Obtener la expresión actual de la pantalla
                text = self.vista.obtener_texto_pantalla()
                self.modelo.expresion = text
                
                # Verificar si la expresión es válida
                if self.modelo.check_expression() == 0:
                    # Si la expresión es válida, calcular el resultado
                    resultado = self.modelo.calcular_resultado()
                    if resultado:
                        # Limpiar la pantalla secundaria y mostrar el resultado
                        self.vista.limpiar_pantalla_secundaria()
                        self.vista.mostrar_en_pantalla_secundaria(resultado)
                else:
                    # Si la expresión no es válida, mostrar advertencia correspondiente
                    opcion = self.modelo.check_expression()
                    if opcion == 1:
                        self.vista.mostrar_advertencia("Expresión Inválida", 
                            "EXPRESIÓN INVÁLIDA!!! Verifica si los paréntesis, corchetes o llaves están bien puestas")
                    elif opcion == 2:
                        self.vista.mostrar_advertencia("Expresión Inválida", 
                            "EXPRESIÓN INVÁLIDA!!! Operadores binarios mal colocados")
                    elif opcion == 3:
                        self.vista.mostrar_advertencia("Expresión Inválida", 
                            "EXPRESIÓN INVÁLIDA!!! Números decimales mal puestos")
                    elif opcion == 4:
                        self.vista.mostrar_advertencia("Expresión Inválida", 
                            "EXPRESIÓN INVÁLIDA!!! Operadores mal puestos, consecutivos o están al inicio o fin")
                    elif opcion == 5:
                        self.vista.mostrar_advertencia("Expresión Inválida", 
                            "EXPRESIÓN INVÁLIDA!!! Operadores unarios mal puestos")
                        
            elif texto == u"\u232B":
                # Manejo de la operación de retroceso (BackSpace)
                self.vista.habilitar_boton_redo()
                self.modelo.borrar_ultimo()  # Borrar el último carácter de la expresión
                self.vista.eliminar_ultimo_pantalla()  # Actualizar la pantalla visual

                # Si la expresión está vacía, deshabilitar el botón de deshacer (Undo)
                if self.modelo.expresion == "":
                    self.vista.deshabilitar_boton_undo()
                    
            elif texto == "C":
                # Manejo de la operación de limpiar (Clear)
                texto_secundario = self.vista.obtener_texto_pantalla_secundaria()
                self.modelo.guardar_texto_secundario(texto_secundario)  # Guardar el texto secundario
                self.modelo.expresion_anterior = self.vista.obtener_texto_pantalla()  # Guardar la expresión anterior
                self.modelo.borrar_operacion()  # Borrar la operación actual
                self.vista.limpiar_pantalla()  # Limpiar la pantalla principal
                self.vista.limpiar_pantalla_secundaria()  # Limpiar la pantalla secundaria
                self.vista.habilitar_boton_undo()  # Habilitar botón de deshacer
                self.vista.deshabilitar_boton_redo()  # Deshabilitar botón de rehacer

            elif texto == u"\u2190":  # Operación de Undo
                if self.modelo.expresion_anterior != "":
                    # Recuperar la expresión anterior
                    self.modelo.expresion = self.modelo.expresion_anterior
                    
                    # Mostrar la expresión restaurada en la pantalla principal
                    self.vista.limpiar_pantalla()
                    self.vista.mostrar_en_pantalla(self.modelo.expresion)

                    # Mostrar el resultado anterior en la pantalla secundaria
                    self.vista.limpiar_pantalla_secundaria()
                    self.vista.mostrar_en_pantalla_secundaria(self.modelo.expresion_result)

                    # Reiniciar el stack de undo_redo y agregar cada carácter de la expresión
                    self.modelo.undo_redo.make_empty()  # Vaciar el stack
                    i = 0
                    for char in self.modelo.expresion:
                        i += 1
                        print(i)
                        if char is not " ":
                            self.modelo.undo_redo.inputChar(char)  # Agregar cada carácter al stack de undo_redo
                    self.modelo.expresion_anterior = ""

                else:
                    # Operación normal de undo
                    self.modelo.undo_operacion()  # Realizar la operación de deshacer
                    if self.modelo.expresion == "":
                        self.vista.deshabilitar_boton_undo()  # Deshabilitar si la expresión está vacía
                    self.vista.habilitar_boton_redo()  # Habilitar botón de rehacer
                    self.vista.limpiar_pantalla()
                    self.vista.mostrar_en_pantalla(self.modelo.expresion)

            elif texto == u"\u2192":
                # Manejo de la operación de Rehacer (Redo)
                self.modelo.redo_operacion()  # Realizar la operación de rehacer
                self.vista.habilitar_boton_undo()  # Habilitar botón de deshacer
                if self.modelo.redo_is_empty():
                    self.vista.deshabilitar_boton_redo()  # Deshabilitar si el stack de rehacer está vacío
                self.vista.limpiar_pantalla()
                self.vista.mostrar_en_pantalla(self.modelo.expresion)
        else:
            # Manejo de operaciones cuando se está escribiendo un número u operador
            self.vista.habilitar_boton_undo()  # Habilitar el botón de deshacer
            self.modelo.agregar_operacion(texto)  # Agregar la operación al modelo
            self.vista.deshabilitar_boton_redo()  # Deshabilitar botón de rehacer
            self.vista.mostrar_en_pantalla(texto)  # Mostrar el texto en la pantalla