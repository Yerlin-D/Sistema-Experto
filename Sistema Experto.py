import tkinter as tk
from tkinter import ttk

def verificar_problema_lavadora():
    lavadora_estado = selected_problem.get()
    if lavadora_estado == 'No enciende':
        label_result.config(text="Verifique si está conectada a una fuente de energía correctamente")
    elif lavadora_estado == 'Hace ruido':
        label_result.config(text="Puede haber un problema con el motor o los rodamientos")
    elif lavadora_estado == 'No desagua':
        label_result.config(text="Verifique si hay una obstrucción en la manguera de desagüe")
    elif lavadora_estado == 'No se llena de agua':
        label_result.config(text="Verifique si está el grifo de agua abierto correctamente")
    elif lavadora_estado == 'Vibra excesivamente':
        label_result.config(text="Verifique si está correctamente nivelada la lavadora")
    elif lavadora_estado == 'Gotea agua':
        label_result.config(text="Verifique si hay una fuga en la manguera de suministro de agua")
    elif lavadora_estado == 'No completa ciclo':
        label_result.config(text="Puede haber un problema con el temporizador o la programación")
    elif lavadora_estado == 'Huele a quemado':
        label_result.config(text="Podría haber un problema con el cableado interno o algún componente quemado")
    elif lavadora_estado == 'Muestra errores':
        label_result.config(text="Verifiqque: ¿Cuál es el código de error específico y qué indica el manual de usuario?")
    elif lavadora_estado == 'No calienta agua':
        label_result.config(text="Podría haber un problema con el calentador de agua o el termostato")
    elif lavadora_estado == 'Problemas con el detergente':
        label_result.config(text="Verifique si el dispensador de detergente está obstruido o dañado")
    elif lavadora_estado == 'No gira':
        label_result.config(text="Podría haber un problema con la correa de transmisión o el embrague")
    elif lavadora_estado == 'Se apaga':
        label_result.config(text="Verifique si está sobrecargada la lavadora")
    elif lavadora_estado == 'Manchas en la ropa':
        label_result.config(text="¿Está el tambor sucio o hay algún residuo acumulado?")
    elif lavadora_estado == 'Zumbido sin accion':
        label_result.config(text="Podría haber un problema con el motor o el capacitor")
    elif lavadora_estado == 'No inicia ciclo':
        label_result.config(text="Verifique si la puerta está cerrada correctamente")
    elif lavadora_estado == 'No avanza':
        label_result.config(text="Podría haber un problema con el sensor de nivel de agua")
    elif lavadora_estado == 'Corrosión herrumbre':
        label_result.config(text="¿Está la lavadora expuesta a la humedad excesiva?, en caso que sí, esto podria estar causando el herrumbre")
    elif lavadora_estado == 'Espuma excesiva':
        label_result.config(text="Verifique si está utilizando la cantidad correcta de detergente")
    elif lavadora_estado == 'Golpeteo al girar':
        label_result.config(text="Puede haber un objeto extraño atascado en el tambor")
    else:
        label_result.config(text="No se reconoce el problema ingresado.")

# Crear ventana
root = tk.Tk()
root.title("Problemas de Lavadora")

root.configure(bg='#e0e0e0')

# Crear y agregar etiquetas
label_problem = ttk.Label(root, text="Problema de la Lavadora:")
label_problem.grid(row=0, column=0, padx=10, pady=5, sticky="w")

label_result = ttk.Label(root, text="" )
label_result.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Lista de problemas
problems = ['No enciende', 'Hace ruido', 'No desagua', 'No se llena de agua', 'Vibra excesivamente', 'Gotea agua', 
            'No completa ciclo', 'Huele a quemado', 'Muestra errores', 'No calienta agua', 'Problemas con el detergente',
            'No gira', 'Se apaga', 'Mancha en la ropa', 'Zumbido sin accion', 'No inicia ciclo', 'No avanza', 
            'Corrosión herrumbre', 'Espuma excesiva', 'Golpeteo al girar']

# Variable para almacenar la selección del usuario
selected_problem = tk.StringVar()

# Crear y agregar menú desplegable
combo_problem = ttk.Combobox(root, textvariable=selected_problem, values=problems)
combo_problem.grid(row=0, column=1, padx=50, pady=10)
combo_problem.current(0)  # Establecer el valor predeterminado

# Botón de verificación
btn_check = ttk.Button(root, text="Verificar", command=verificar_problema_lavadora)
btn_check.grid(row=1, column=0, columnspan=2, padx=50, pady=10)

root.mainloop()
