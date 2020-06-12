from model.model import Model 
from view.view import View
from datetime import *
from tkinter import *
from tkinter import messagebox


class Controller:

	def __init__(self):
		self.model = Model()
		self.view=View()

	def start(self):
		
		
		ventana = Tk()
		ventana.title ("Login")
		ventana.geometry ("350x150+500+250")
		ventana.iconbitmap("amigo.ico")
		Label(ventana, text = "Usuario:").pack()
		caja1 = Entry(ventana)
		caja1.pack()
		Label(ventana, text = "Contraseña:").pack()
		caja2 = Entry(ventana, show = "*")
		caja2.pack()

		def login():
			descripcion = caja1.get()
			password = caja2.get()
			adpass=self.model.read_a_pass(descripcion,password)
			if type(adpass) == tuple:
				ventana.destroy()
				self.view.start()
			else:
				messagebox.showinfo("Login","Contraseña incorrecta")
			
		Button (text = "Login", command = login).pack()

		
		ventana.mainloop()


		
	