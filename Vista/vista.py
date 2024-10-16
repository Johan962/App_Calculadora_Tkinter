from tkinter import Text, Button, END, INSERT
from tkinter.messagebox import showwarning
import os

class CalculadoraVista:
    def __init__(self, ventana, controlador):
        #Crear el path absoluto
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, "../src/icons/icon.ico")
        self.controlador = controlador  # Guarda la referencia al controlador
        # Configura la ventana principal
        ventana.title("Calculadora")  # Establece el título de la ventana
        #ventana.iconbitmap(icon_path) # Descomentar para establecer un ícono
        # Configuración de la pantalla para mostrar la expresión
        self.pantalla = Text(ventana, state="disabled", width=20, height=3,
                             background="white", foreground="black", font=("Helvetica", 15))
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Configuración de la pantalla para mostrar el resultado
        self.pantalla_result = Text(ventana, state="disabled", width=18, height=2,
                             background="white", foreground="black", font=("Helvetica", 15))
        self.pantalla_result.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")
        # Configurar la ventana para que todas las columnas tengan el mismo peso
        for i in range(4):  # Asigna un peso igual a las 4 columnas
            ventana.grid_columnconfigure(i, weight=1)

        # Configurar las filas para que se expandan uniformemente (opcional)
        for i in range(9):  # Ajusta según el número total de filas que tienes
            ventana.grid_rowconfigure(i, weight=1)

        # Creación de botones de deshacer y rehacer
        self.botonU = self.crearBoton(u"\u2190", escribir=False, bg="#F39C12", fg="white")  # Botón para deshacer
        self.botonU.config(state="disabled")  # Inicialmente deshabilitado
        self.botonR = self.crearBoton(u"\u2192", escribir=False, bg="#F39C12", fg="white")  # Botón para rehacer
        self.botonR.config(state="disabled")  # Inicialmente deshabilitado

        # Creación de botones numéricos y de operación
        boton1 = self.crearBoton(7,fg="black", bg="#ECF0F1" )
        boton2 = self.crearBoton(8,fg="black", bg="#ECF0F1")
        boton3 = self.crearBoton(9,fg="black", bg="#ECF0F1")
        boton4 = self.crearBoton(u"\u232B", escribir=False, bg="#5DADE2", fg="white")  # Botón de borrar
        boton5 = self.crearBoton(4,fg="black", bg="#ECF0F1")
        boton6 = self.crearBoton(5,fg="black", bg="#ECF0F1")
        boton7 = self.crearBoton(6,fg="black", bg="#ECF0F1")
        boton8 = self.crearBoton("C", escribir=False, bg="#E74C3C", fg="white")  # Botón de limpiar
        boton9 = self.crearBoton(1,fg="black", bg="#ECF0F1")
        boton10 = self.crearBoton(2,fg="black", bg="#ECF0F1")
        boton11 = self.crearBoton(3,fg="black", bg="#ECF0F1")
        boton12 = self.crearBoton(u"\u00F7", bg="#2C3E50", fg="white")  # Botón de división
        boton13 = self.crearBoton(".", bg="#D5DBDB", fg="black")
        boton14 = self.crearBoton(0,fg="black", bg="#ECF0F1")
        boton15 = self.crearBoton("+", bg="#2C3E50", fg="white")
        boton16 = self.crearBoton("*", bg="#2C3E50", fg="white")
        boton17 = self.crearBoton("(", bg="#BDC3C7", fg="black")
        boton18 = self.crearBoton(")", bg="#BDC3C7", fg="black")
        boton19 = self.crearBoton(u"\u221A", bg="#2C3E50", fg="white")  # Botón de raíz
        boton20 = self.crearBoton("-", bg="#2C3E50", fg="white")
        boton21 = self.crearBoton("{", bg="#BDC3C7", fg="black")
        boton22 = self.crearBoton("}", bg="#BDC3C7", fg="black")
        boton23 = self.crearBoton("[", bg="#BDC3C7", fg="black")
        boton24 = self.crearBoton("^", bg="#2C3E50", fg="white")  # Botón de potencia
        boton25 = self.crearBoton("]", bg="#BDC3C7", fg="black")
        boton26 = self.crearBoton("=", escribir=False, bg="#4CAF50", fg="white" )  # Botón de igual
        
        # Lista de botones para facilitar su disposición en la cuadrícula
        botones = [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10,
                   boton11, boton12, boton13, boton14, boton15, boton16, boton17, boton18, 
                   boton19, boton20, boton21, boton22, boton23, boton24, boton25, boton26]
        contador = 0  # Contador para el manejo de la cuadrícula
        
        # Posiciona los botones en la cuadrícula
        self.botonU.grid(row=1, column=0, sticky="nsew", padx=5, pady=5) # Botón de deshacer
        self.botonR.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)  # Botón de rehacer    

        # Disposición de los botones en la cuadrícula
        for fila in range(2, 8):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)
                contador += 1
        botones[24].grid(row=8, column=2, sticky="nsew", padx=5, pady=5)  # Botón de potencia
        botones[25].grid(row=8, column=0, sticky="nsew", padx=5, pady=5, columnspan=2)  # Botón de igual que ocupa 2 columnas
        
        # Vincular el evento de teclado
        ventana.bind("<Key>", self.manejar_teclado)  # Asigna el método de manejo de teclado
        return

    def manejar_teclado(self, event):
        # Mapeo de teclas a sus respectivas funciones
        tecla = event.keysym  # Obtiene la tecla presionada
        if event.state & 0x0004:  # Verifica si Ctrl está presionado
            if tecla == 'z':
                self.controlador.click_boton(u"\u2190", escribir=False)  # Deshacer
            elif tecla == 'y':
                self.controlador.click_boton(u"\u2192", escribir=False)  # Rehacer
        else:
            if tecla in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                self.controlador.click_boton(tecla, escribir=True)  # Presionada una tecla numérica
            elif tecla in ['plus', 'minus', 'asterisk', 'slash']:
                operadores = {'plus': '+', 'minus': '-', 'asterisk': '*', 'slash': '/'}
                self.controlador.click_boton(operadores[tecla], escribir=True)  # Mapeo de operaciones
            elif tecla == 'equal' or tecla == "Return":
                self.controlador.click_boton('=', escribir=False)  # Presionada la tecla igual
            elif tecla == 'BackSpace':
                self.controlador.click_boton(u"\u232B", escribir=False)  # Mapeo al botón de borrar
            elif tecla == 'c':
                self.controlador.click_boton("C", escribir=False)  # 'C' para limpiar
            elif tecla == 'r':
                self.controlador.click_boton(u"\u221A", escribir=True)  # Raíz cuadrada (sqrt)
            elif tecla == 'asciicircum':
                self.controlador.click_boton("^", escribir=True)  # Potencia
            elif tecla == "parenleft":
                self.controlador.click_boton("(", escribir=True) #Abrir parentesis
            elif tecla == "parenright":
                self.controlador.click_boton(")", escribir=True) #Cerrar parentesis
            elif tecla == "braceleft":
                self.controlador.click_boton("{", escribir=True) #Abrir llaves
            elif tecla == "braceright":
                self.controlador.click_boton("}", escribir=True) #Cerrar llaves
            elif tecla == "bracketleft":
                self.controlador.click_boton("[", escribir=True) #Abrir corcehetes
            elif tecla == "bracketright":
                self.controlador.click_boton("]", escribir=True) #Cerrar corchetes                
            elif tecla == "period":
                self.controlador.click_boton(".", escribir=True) #Cerrar corchetes                
                
                
    def crearBoton(self, valor, escribir=True, ancho=5, alto=2, bg="lightgray", fg="black"):
        # Crea un botón cuadrado ajustando los valores de ancho y alto
        return Button(text=valor, width=ancho, height=alto, font=("Helvetica", 15),
                    bg=bg, fg=fg,
                    command=lambda: self.controlador.click_boton(valor, escribir))


    def mostrar_en_pantalla(self, valor):
        # Muestra el valor en la pantalla principal
        self.pantalla.configure(state="normal")  # Habilita la pantalla
        self.pantalla.insert(END, valor)  # Inserta el valor al final
        self.pantalla.configure(state="disabled")  # Deshabilita la pantalla para evitar ediciones

    def mostrar_en_pantalla_secundaria(self, valor):
        # Muestra el valor en la pantalla secundaria (resultado)
        self.pantalla_result.configure(state="normal")  # Habilita la pantalla de resultados
        self.pantalla_result.insert(END, valor)  # Inserta el valor al final
        self.pantalla_result.configure(state="disabled")  # Deshabilita la pantalla de resultados
    
    def limpiar_pantalla(self):
        # Limpia la pantalla principal
        self.pantalla.configure(state="normal")  # Habilita la pantalla
        self.pantalla.delete("1.0", END)  # Elimina todo el texto
        self.pantalla.configure(state="disabled")  # Deshabilita la pantalla

    def limpiar_pantalla_secundaria(self):
        # Limpia la pantalla secundaria
        self.pantalla_result.configure(state="normal")  # Habilita la pantalla de resultados
        self.pantalla_result.delete("1.0", END)  # Elimina todo el texto
        self.pantalla_result.configure(state="disabled")  # Deshabilita la pantalla de resultados

    def insertar_texto(self, text):
        # Inserta texto en la pantalla principal, reemplazando su contenido
        self.pantalla.configure(state="normal")  # Habilita la pantalla
        self.pantalla.delete('1.0', END)  # Elimina todo el texto
        self.pantalla.insert(INSERT, text)  # Inserta el nuevo texto
        self.pantalla.configure(state="disabled")  # Deshabilita la pantalla

    def eliminar_ultimo_pantalla(self):
        # Elimina el último carácter de la pantalla principal
        text = self.pantalla.get("1.0", END)  # Obtiene el texto actual
        if len(text) > 1:  # Para evitar eliminar más de lo necesario
            text = text[:-2]  # Borra solo el último carácter
            self.insertar_texto(text)  # Reemplaza el contenido de la pantalla con el texto modificado

    def obtener_texto_pantalla(self):
        # Devuelve el texto de la pantalla principal
        return self.pantalla.get("1.0", END)
    
    def obtener_texto_pantalla_secundaria(self):
        # Devuelve el texto de la pantalla secundaria
        return self.pantalla_result.get("1.0", END)
        
    def mostrar_advertencia(self, titulo, texto):
        # Muestra un cuadro de advertencia con un título y texto
        showwarning(titulo, texto)
        
    def deshabilitar_boton_redo(self):
        # Deshabilita el botón de rehacer
        self.botonR.config(state="disabled")
        
    def deshabilitar_boton_undo(self):
        # Deshabilita el botón de deshacer
        self.botonU.config(state="disabled")
        
    def habilitar_boton_redo(self):
        # Habilita el botón de rehacer
        self.botonR.config(state="normal")

    def habilitar_boton_undo(self):
        # Habilita el botón de deshacer
        self.botonU.config(state="normal")
