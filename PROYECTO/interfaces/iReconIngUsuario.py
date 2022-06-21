import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox
from interfaces.iNdexPago import Pago


class ReconIniciar:
    def __init__(self, window, matricula):
        self.wind = window
        self.parametroMatricula = matricula
        self.wind.title("Alquila Ya")
        # Obtiene ancho del área de visualización.
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()
        # Establece ancho de la ventana.
        width = 800
        # Establece altura de la ventana.
        height = 600
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.wind.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.wind.resizable(0, 0)

        #Creacion del Frame
        frame = LabelFrame(self.wind)
        frame.place(relwidth=1, relheight=1)

        #Label
        tk.Label(frame, text="EN ESTA INTERFAZ RECONOCERIA EL ROSTRO").place(
            relx=0.40, rely=0.4)

        #Creacion de los Botones
        tk.Button(frame, text="Reconocimiento",
                  command=self.validarUsuario).place(relx=0.40, rely=0.60)

        #Crecion de Entry
        self.idCuil = tk.Entry(frame)
        self.idCuil.focus()
        self.idCuil.place(relx=0.50, rely=0.3)
        tk.Button(frame, text="Atras",
                   command=self.atras).place(relx=0.01, rely=0.9)

        window.mainloop()

    def atras(self):
        self.wind.withdraw()
        from interfaces.iPrimerPantalla import Ventana1
        obj=Ventana1(Tk())

    def validarUsuario(self):
        if (self.idCuil.get()):
            datoCuil =self.idCuil.get()
            if (self.searchEnAlquiler()):
                messagebox.showwarning(
                    "Usuario sin operacion", "Ya tiene un auto en alquiler")
                self.idCuil.focus()
            else:
                self.wind.withdraw()
                ventana = Pago(Tk(), datoCuil, self.parametroMatricula)
        else:
            messagebox.showwarning(
                "Error", "Los campos no pueden estar vacíos")
            self.idCuil.focus()

    def searchUsuario(self):
        db_name = "base_datos/databaseGeneral.sqlite3"
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        idCuil = self.idCuil.get()
        cur.execute(
            "SELECT Cuil FROM Usuarios WHERE Cuil=?", (idCuil,))
        datos = cur.fetchall()
        con.close()
        return datos

    def searchEnAlquiler(self):
        db_name = "base_datos/databaseGeneral.sqlite3"
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        idCuil = self.idCuil.get()
        cur.execute("SELECT IdCuil FROM Alquileres WHERE IdCuil=?", (idCuil,))
        datos = cur.fetchall()
        con.close()
        return datos
