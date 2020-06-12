from tkinter import *
from model.model import Model 
from view.view import View 
from datetime import date
from tkinter import messagebox
from tkinter import ttk


ventana = Tk()
ventana.iconbitmap("amigo.ico")
miframe=Frame(ventana)
miframe.pack()
ventana.title ("Nota")
ventana.geometry ("550x450")
lblDatos=Label(miframe, text = "Datos:")
lblDatos.grid(row=0, column=0, sticky="e", padx=10, pady=10)

lblNom=Label(miframe, text = "Mesa:")
lblNom.grid(row=2, column=0, sticky="e", padx=10, pady=10)
comboMesa=ttk.Combobox(miframe)
comboMesa.grid(row=2, column=1, sticky="e", padx=10, pady=10)

lblNom=Label(miframe, text = "Mesero:")
lblNom.grid(row=3, column=0, sticky="e", padx=10, pady=10)
comboMesero=ttk.Combobox(miframe)
comboMesero.grid(row=3, column=1, sticky="e", padx=10, pady=10)

lblNom=Label(miframe, text = "Producto:")
lblNom.grid(row=4, column=0, sticky="e", padx=10, pady=10)
comboProducto=ttk.Combobox(miframe)
comboProducto.grid(row=4, column=1, sticky="e", padx=10, pady=10)

lblNom=Label(miframe, text = "Cantidad:")
lblNom.grid(row=5, column=0, sticky="e", padx=10, pady=10)
cajaCat=Entry(miframe)
cajaCat.grid(row=5, column=1, sticky="e", padx=10, pady=10)

def Ecat():
	descripcion= caja1.get()
	estatus=0
	fechacreacion=datetime.datetime.now()				
	idcat=int(combo.current())+1
	#editcat=self.model.create_ciudad(idcat, descripcion, estatus, fechacreacion)
	if editcat == True:
		ventana.destroy()
		messagebox.showinfo("Categoria","Se Agrego ciudad")	
	else:
		if editcat.errno == 1062:
			messagebox.showinfo("Categoria","La ciudad ya existe")
		else:
			messagebox.showinfo("Categoria","No se pudo agregar la ciudad")
								
botonNuevo=Button(miframe, text="Agregar",command=Ecat)
botonNuevo.grid(row=2, column=3, sticky="e", padx=10, pady=10)

botonAgregar=Button(miframe, text="Agregar",command=Ecat)
botonAgregar.grid(row=3, column=3, sticky="e", padx=10, pady=10)

botonActualizar=Button(miframe, text="Agregar",command=Ecat)
botonActualizar.grid(row=4, column=3, sticky="e", padx=10, pady=10)

botonPagar=Button(miframe, text="Agregar",command=Ecat)
botonPagar.grid(row=5, column=3, sticky="e", padx=10, pady=10)
ventana.mainloop()