"""
Expedientes Médicos COVID19 - Árbol Binario de Búsqueda (ABB)
Seminario de Solución de Problemas de Algoritmia
Created By: Isaac Eduardo Sánchez Campos
Código: 211172172
"""

import tkinter as tk
import sys
import os
from tkinter import ttk
from tkinter.ttk import *
import random
from random import shuffle
from tkinter import messagebox as mb

class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree():
    def __init__(self):
        self.root = None

    def insert(self, a, value):
        if a == None:
            a = Node(value)
        else:
            d = a.value
            if value < d:
                a.left = self.insert(a.left, value)
            else:
                a.right = self.insert(a.right, value)
        return a

    def search(self, value, a):
        if a == None:
            return None
        else:
            if value == a.value:
                return a.value
            else:
                if value < a.value:
                    return self.search(value, a.left)
                else:
                    return self.search(value, a.right)

tree = Tree()

class Application:

    def __init__(self):
        self.window=tk.Tk()
        self.agregar_menu()
        self.window.title("Expedientes")
        self.canvas=tk.Canvas(self.window, width=800, height=400, background="white")
        self.name_label=tk.Label(self.window,text="Nombre:")
        self.name_label.grid(column=0, row=0)
        self.name=tk.StringVar()
        self.name_input=tk.Entry(self.window, width=50, textvariable=self.name)
        self.name_input.grid(column=1, row=0)

        self.age_label=tk.Label(self.window,text="Edad:")
        self.age_label.grid(column=0, row=2)
        self.age=tk.StringVar()
        self.age_input=tk.Entry(self.window, width=50, textvariable=self.age)
        self.age_input.grid(column=1, row=2)

        self.covid_label=tk.Label(self.window,text="COVID-19:")
        self.covid_label.grid(column=0, row=4)
        self.covid=tk.StringVar()
        self.covid_input=tk.Entry(self.window, width=50, textvariable=self.covid)
        self.covid_input.grid(column=1, row=4)

        self.background_label=tk.Label(self.window,text="Antecedentes:")
        self.background_label.grid(column=0, row=6)
        self.background=tk.StringVar()
        self.background_input=tk.Entry(self.window, width=50, textvariable=self.background)
        self.background_input.grid(column=1, row=6)

        self.add_button=tk.Button(self.window, text="Ingresar", command=self.register)
        self.add_button.grid(column=1, row=8)
        self.window.mainloop()

    def agregar_menu(self):
        self.topbar_menu = tk.Menu(self.window)
        self.window.config(menu=self.topbar_menu)
        self.options = tk.Menu(self.topbar_menu, tearoff=0)
        self.options.add_command(label="Buscar Expediente", command=self.configure)
        self.options.add_command(label="Cargar Expedientes", command=self.upload)
        self.topbar_menu.add_cascade(label="Buscar", menu=self.options)

    def configure(self):
        title = SearchBox(self.window)
        s = title.show()
        value = s
        print(value)
        search_result = tree.search(value, tree.root)
        print(search_result)
        if tree.search(value, tree.root) == None:
            mb.showinfo("Alerta", "No existe expendiente con ese nombre.")
        else:
            mb.showinfo("Alerta", "Búsqueda realizada correctamente." + "\nNodo encontrado: " + str(tree.search(value, tree.root)))

    def upload(self):
        mb.showinfo("Alerta", "Expedientes cargados con exito.")

    def register(self):
        name = self.name.get()
        age = self.age.get()
        covid = self.covid.get()
        background = self.background.get()

        file_name = name + ".txt"
        user_file = open(file_name, "w")

        new_age = age + "\n"
        new_covid = covid + "\n"
        new_backgroud = background + "\n"

        user_file.write(new_age)
        user_file.write(new_covid)
        user_file.write(new_backgroud)

        # Inserta el nombre del paciente que es el nombre del archivo del expediente
        tree.root = tree.insert(tree.root, name)

        mb.showinfo("Alerta", "Paciente registrado con exito.")

class SearchBox:

    def __init__(self, main_window):
        self.window_title=tk.Toplevel(main_window)
        self.window_label_name=ttk.Label(self.window_title, text="Nombre:")
        self.window_label_name.grid(column=0, row=0, padx=5, pady=5)
        self.search_name=tk.StringVar()
        self.window_search_name=ttk.Entry(self.window_title, textvariable=self.search_name)
        self.window_search_name.grid(column=1, row=0, padx=5, pady=5)
        self.window_search_name.focus()
        self.window_button=ttk.Button(self.window_title, text="Buscar", command=self.confirm)
        self.window_button.grid(column=1, row=2, padx=5, pady=5)
        self.window_title.protocol("WM_DELETE_WINDOW", self.confirm)
        self.window_title.resizable(0,0)
        self.window_title.grab_set()

    def show(self):
        self.window_title.wait_window()
        return (self.search_name.get())

    def confirm(self):
        self.window_title.destroy()

application = Application()

