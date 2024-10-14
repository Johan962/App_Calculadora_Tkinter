from tkinter import Tk
from Modelo.modelo import Modelo
from Vista.vista import CalculadoraVista
from Controlador.controlador import CalculadoraControlador

# Inicialización de la aplicación
if __name__ == "__main__":
    # Crear la ventana principal de la aplicación
    ventana_principal = Tk()

    # Inicializar el modelo, vista y controlador
    modelo = Modelo()  # Crear una instancia del modelo que contiene la lógica de la calculadora
    controlador = CalculadoraControlador(modelo, None)  # Inicializar el controlador sin vista aún

    # Crear la vista de la calculadora, pasando la ventana principal y el controlador
    vista = CalculadoraVista(ventana_principal, controlador)
    
    # Asignar la vista al controlador después de crear la vista
    controlador.vista = vista  

    # Iniciar el bucle principal de la interfaz gráfica de usuario
    ventana_principal.mainloop()