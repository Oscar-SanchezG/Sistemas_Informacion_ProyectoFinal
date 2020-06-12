from tkinter import *
from model.model import Model 
from datetime import date
from tkinter import messagebox
from tkinter import ttk
import datetime

class View:
	def __init__(self):
			self.model = Model()

	def start(self):
		
		
#--------------------Comandos---------------------------
		def salirAplicacion():
			valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicacion?")
			if valor == "yes":
				root.destroy()

		def acecadeNosotros():
			ventana = Tk()
			ventana.title (" Aceca de Nosotros")
			ventana.geometry ("350x150+500+250")
			ventana.iconbitmap("amigo.ico")
			Label(ventana, text = "Sistema de administacion para el Restaurante-Bar").pack()		
			Label(ventana, text = "Mariscos El amigo de Silao").pack()
			Label(ventana, text = "Proyecto creado para la materia:").pack()
			Label(ventana, text = "Sistemas de la Informacion").pack()
			Label(ventana, text = "Alumnos:").pack()
			Label(ventana, text = "Sanchez Gonzalez Oscar Eduardo").pack()
			Label(ventana, text = "Zuñiga Luis").pack()
			ventana.mainloop()
			

		def catNueva():			
			ventana = Tk()
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Categoria Nueva")
			ventana.geometry ("350x100")
			nlabel=Label(miframe, text = "Nombre nueva Categoria:")
			nlabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
			ventana.iconbitmap("amigo.ico")
			caja1 = Entry(miframe)
			caja1.grid(row=2, column=2, sticky="e", padx=10, pady=10)
			def Acat():
				descripcion= caja1.get()
				estatus=0
				fechacreacion=datetime.datetime.now()
				addcat=self.model.create_cat(descripcion, estatus, fechacreacion)
				if addcat == True:
					ventana.destroy()
					messagebox.showinfo("Categoria","Se agrego categoria")	
				else:
					if addcat == 1062:
						messagebox.showinfo("Categoria","La categoria ya existe")
					else:
						messagebox.showinfo("Categoria","No se pudo agregae categoria")
				
			botonAgragar=Button(miframe, text="agregar",command=Acat)
			botonAgragar.grid(row=3, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def catEditar():			
			ventana = Tk()
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Editar Categoria")
			ventana.geometry ("350x150")
			nlabel=Label(miframe, text = "Nombre de Categoria:")
			nlabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
			nlabel2=Label(miframe, text = "Nombre nuevo:")
			nlabel2.grid(row=3, column=1, sticky="e", padx=10, pady=10)
			ventana.iconbitmap("amigo.ico")
			caja1 = Entry(miframe)
			caja1.grid(row=3, column=2, sticky="e", padx=10, pady=10)
			combo=ttk.Combobox(miframe)
			combo.grid(row=2, column=2, sticky="e", padx=10, pady=10)
			valores=self.model.lectura_descripcion()
			combo['values']=valores
			combo.current(0)
			def Ecat():
				descripcion= caja1.get()
				estatus=0
				fechamodificacion=datetime.datetime.now()				
				idcat=int(combo.current())+1
				editcat=self.model.edit_cat(descripcion, fechamodificacion, idcat)
				if editcat == True:
					ventana.destroy()
					messagebox.showinfo("Categoria","Se Actualizo categoria")	
				else:
					if editcat == None:
						messagebox.showinfo("Categoria","La categoria no existe")
					else:
						messagebox.showinfo("Categoria","No se pudo Actualizar categoria")				
			botonAgragar=Button(miframe, text="Actualizar",command=Ecat)
			botonAgragar.grid(row=4, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def catActivar():			
			ventana = Tk()
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Activar Categoria")
			ventana.geometry ("350x150")
			nlabel=Label(miframe, text = "Nombre de Categoria:")
			nlabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
			ventana.iconbitmap("amigo.ico")
			combo=ttk.Combobox(miframe)
			combo.grid(row=2, column=2, sticky="e", padx=10, pady=10)
			valores=self.model.lectura_descripcion()
			combo['values']=valores
			combo.current(0)
			def Ecat():
				estatus=0
				fechamodificacion=datetime.datetime.now()				
				idcat=int(combo.current())+1
				editcat=self.model.estatus_cat(estatus, fechamodificacion, idcat)
				if editcat == True:
					ventana.destroy()
					messagebox.showinfo("Categoria","Se Activo categoria")	
				else:
					if editcat == None:
						messagebox.showinfo("Categoria","La categoria no existe")
					else:
						messagebox.showinfo("Categoria","No se pudo Activar categoria")				
			botonAgragar=Button(miframe, text="Activar",command=Ecat)
			botonAgragar.grid(row=4, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def catBaja():			
			ventana = Tk()
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Baja Categoria")
			ventana.geometry ("350x150")
			nlabel=Label(miframe, text = "Nombre de Categoria:")
			nlabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
			ventana.iconbitmap("amigo.ico")
			combo=ttk.Combobox(miframe)
			combo.grid(row=2, column=2, sticky="e", padx=10, pady=10)
			valores=self.model.lectura_descripcion()
			combo['values']=valores
			combo.current(0)
			def Ecat():
				estatus=99
				fechamodificacion=datetime.datetime.now()				
				idcat=int(combo.current())+1
				editcat=self.model.estatus_cat(estatus, fechamodificacion, idcat)
				if editcat == True:
					ventana.destroy()
					messagebox.showinfo("Categoria","Se dio de baja categoria")	
				else:
					if editcat == None:
						messagebox.showinfo("Categoria","La categoria no existe")
					else:
						messagebox.showinfo("Categoria","No se pudo dar de baja categoria")				
			botonAgragar=Button(miframe, text="Baja",command=Ecat)
			botonAgragar.grid(row=4, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def cddNueva():			
			ventana = Tk()
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Nueva Cuidad")
			ventana.geometry ("350x150")
			nlabel=Label(miframe, text = "Estado:")
			nlabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
			nlabel2=Label(miframe, text = "Ciudad:")
			nlabel2.grid(row=3, column=1, sticky="e", padx=10, pady=10)
			ventana.iconbitmap("amigo.ico")
			caja1 = Entry(miframe)
			caja1.grid(row=3, column=2, sticky="e", padx=10, pady=10)
			combo=ttk.Combobox(miframe)
			combo.grid(row=2, column=2, sticky="e", padx=10, pady=10)
			valores=self.model.lectura_estados()
			combo['values']=valores
			combo.current(0)
			def Ecat():
				descripcion= caja1.get()
				estatus=0
				fechacreacion=datetime.datetime.now()				
				idcat=int(combo.current())+1
				editcat=self.model.create_ciudad(idcat, descripcion, estatus, fechacreacion)
				if editcat == True:
					ventana.destroy()
					messagebox.showinfo("Categoria","Se Agrego ciudad")	
				else:
					if editcat.errno == 1062:
						messagebox.showinfo("Categoria","La ciudad ya existe")
					else:
						messagebox.showinfo("Categoria","No se pudo agregar la ciudad")
								
			botonAgragar=Button(miframe, text="Agregar",command=Ecat)
			botonAgragar.grid(row=4, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def mesaActivar():			
			ventana = Tk()
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Activar Categoria")
			ventana.geometry ("350x150")
			nlabel=Label(miframe, text = "Cantidad de mesas:")
			nlabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
			ventana.iconbitmap("amigo.ico")
			caja1 = Entry(miframe)
			caja1.grid(row=3, column=2, sticky="e", padx=10, pady=10)
			def Ecat():
				cantidad= caja1.get()
				estatus=0
				fechacreacion=datetime.datetime.now()				
				editcat=self.model.act_mesa(cantidad ,estatus, fechacreacion)
				if editcat == True:
					ventana.destroy()
					messagebox.showinfo("Mesas","Se Activo el numero de mesas")	
				else:
					if editcat == None:
						messagebox.showinfo("Mesas","No se pudo Actualizar")
					else:
						messagebox.showinfo("Mesas","No se pudo Actualizar el numero de mesas")				
			botonAgragar=Button(miframe, text="Actualizar",command=Ecat)
			botonAgragar.grid(row=4, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def cltNuevo():
			ventana = Tk()
			ventana.iconbitmap("amigo.ico")
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Nuevo Cliente")
			ventana.geometry ("550x450")


			lblDatos=Label(miframe, text = "Datos:")
			lblDatos.grid(row=0, column=0, sticky="e", padx=10, pady=10)
			lblRfc=Label(miframe, text = "R.F.C:")
			lblRfc.grid(row=1, column=0, sticky="e", padx=10, pady=10)
			cajaRfc = Entry(miframe)
			cajaRfc.grid(row=1, column=1, sticky="e", padx=10, pady=10)

			lblNom=Label(miframe, text = "Nombre:")
			lblNom.grid(row=2, column=0, sticky="e", padx=10, pady=10)
			cajaNom = Entry(miframe)
			cajaNom.grid(row=2, column=1, sticky="e", padx=10, pady=10)

			lblAP=Label(miframe, text = "Ap. Paterno:")
			lblAP.grid(row=3, column=0, sticky="e", padx=10, pady=10)
			cajaAP = Entry(miframe)
			cajaAP.grid(row=3, column=1, sticky="e", padx=10, pady=10)

			lblAM=Label(miframe, text = "Ap. Materno:")
			lblAM.grid(row=4, column=0, sticky="e", padx=10, pady=10)
			cajaAM = Entry(miframe)
			cajaAM.grid(row=4, column=1, sticky="e", padx=10, pady=10)

			lblTel=Label(miframe, text = "Telefono:")
			lblTel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

			lblTelF=Label(miframe, text = "Telefono Fijo:")
			lblTelF.grid(row=6, column=0, sticky="e", padx=10, pady=10)
			cajaTelF = Entry(miframe)
			cajaTelF.grid(row=6, column=1, sticky="e", padx=10, pady=10)

			lblTelM=Label(miframe, text = "Telefono movil:")
			lblTelM.grid(row=7, column=0, sticky="e", padx=10, pady=10)
			cajaTelM = Entry(miframe)
			cajaTelM.grid(row=7, column=1, sticky="e", padx=10, pady=10)

			lblEM=Label(miframe, text = "Email:")
			lblEM.grid(row=8, column=0, sticky="e", padx=10, pady=10)

			lblEM1=Label(miframe, text = "Email:")
			lblEM1.grid(row=9, column=0, sticky="e", padx=10, pady=10)
			cajaEM1 = Entry(miframe)
			cajaEM1.grid(row=9, column=1, sticky="e", padx=10, pady=10)

			lblEM2=Label(miframe, text = "Email 2:")
			lblEM2.grid(row=10, column=0, sticky="e", padx=10, pady=10)
			cajaEM2 = Entry(miframe)
			cajaEM2.grid(row=10, column=1, sticky="e", padx=10, pady=10)

			lblDOM=Label(miframe, text = "Domicilio:")
			lblDOM.grid(row=0, column=2, sticky="e", padx=10, pady=10)

			lblCalle=Label(miframe, text = "Calle:")
			lblCalle.grid(row=1, column=2, sticky="e", padx=10, pady=10)
			cajaCalle = Entry(miframe)
			cajaCalle.grid(row=1, column=3, sticky="e", padx=10, pady=10)

			lblNext=Label(miframe, text = "Num. Ext:")
			lblNext.grid(row=2, column=2, sticky="e", padx=10, pady=10)
			cajaNext = Entry(miframe)
			cajaNext.grid(row=2, column=3, sticky="e", padx=10, pady=10)

			lblNint=Label(miframe, text = "Num. Int:")
			lblNint.grid(row=3, column=2, sticky="e", padx=10, pady=10)
			cajaNint = Entry(miframe)
			cajaNint.grid(row=3, column=3, sticky="e", padx=10, pady=10)

			lblCol=Label(miframe, text = "Colonia:")
			lblCol.grid(row=4, column=2, sticky="e", padx=10, pady=10)
			cajaCol = Entry(miframe)
			cajaCol.grid(row=4, column=3, sticky="e", padx=10, pady=10)

			def callbackFunc(event):
				idce=int(comboEstado.current())+1
				valores=self.model.lectura_ciudades(idce)
				comboCiudad['values']=valores



			lblEstado=Label(miframe, text = "Estado:")
			lblEstado.grid(row=5, column=2, sticky="e", padx=10, pady=10)
			comboEstado=ttk.Combobox(miframe)
			comboEstado.grid(row=5, column=3, sticky="e", padx=10, pady=10)
			comboEstado.bind("<<ComboboxSelected>>", callbackFunc)

			lblCiudad=Label(miframe, text = "Ciudad:")
			lblCiudad.grid(row=6, column=2, sticky="e", padx=10, pady=10)
			comboCiudad=ttk.Combobox(miframe)
			comboCiudad.grid(row=6, column=3, sticky="e", padx=10, pady=10)

			lblRef=Label(miframe, text = "Referencia:")
			lblRef.grid(row=7, column=2, sticky="e", padx=10, pady=10)
			cajaRef = Entry(miframe)
			cajaRef.grid(row=7, column=3, sticky="e", padx=10, pady=10)

			lblLoc=Label(miframe, text = "Localidad:")
			lblLoc.grid(row=8, column=2, sticky="e", padx=10, pady=10)
			cajaLoc = Entry(miframe)
			cajaLoc.grid(row=8, column=3, sticky="e", padx=10, pady=10)

			lblCp=Label(miframe, text = "Codigo Postal:")
			lblCp.grid(row=9, column=2, sticky="e", padx=10, pady=10)
			cajaCp = Entry(miframe)
			cajaCp.grid(row=9, column=3, sticky="e", padx=10, pady=10)


			valores=self.model.lectura_estados()
			comboEstado['values']=valores
			comboEstado.current(0)


			def Ecat():		
				idc=int(comboCiudad.current())+1
				rfc=cajaRfc.get()
				nombre=cajaNom.get()
				paterno=cajaAP.get()
				materno=cajaAM.get()
				calle=cajaCalle.get()
				numint=cajaNint.get()
				numext=cajaNext.get()
				colonia=cajaCol.get()
				cp=cajaCp.get()
				referencia=cajaRef.get()
				localidad=cajaLoc.get()
				telfijo=cajaTelF.get()
				telmovil=cajaTelM.get()
				email=cajaEM1.get()
				email2=cajaEM2.get()
				estatus=0
				fechacreacion=datetime.datetime.now()
				editcat=self.model.add_cliente(idc, rfc, nombre, paterno, materno, calle, numint, numext, colonia, cp, referencia, localidad, telfijo, telmovil, email, email2, estatus, fechacreacion)
				if editcat == True:
					ventana.destroy()
					messagebox.showinfo("Ciente","Se Agrego el Cliente")	
				else:
					messagebox.showinfo("Ciente","No se agrego el Cliente")
				return
											
			botonAgragar=Button(miframe, text="Agregar",command=Ecat)
			botonAgragar.grid(row=10, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def cltEditar():
			ventana = Tk()
			ventana.iconbitmap("amigo.ico")
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Actualizar Cliente")
			ventana.geometry ("550x600")

			lblDatos=Label(miframe, text = "Datos:")
			lblDatos.grid(row=0, column=0, sticky="e", padx=10, pady=10)
			lblRfc=Label(miframe, text = "R.F.C:")
			lblRfc.grid(row=1, column=0, sticky="e", padx=10, pady=10)
			cajaRFC=Entry(miframe)
			cajaRFC.grid(row=1, column=1, sticky="e", padx=10, pady=10)

			lblNom=Label(miframe, text = "Nombre:")
			lblNom.grid(row=2, column=0, sticky="e", padx=10, pady=10)
			cajaNombre=Entry(miframe)
			cajaNombre.grid(row=2, column=1, sticky="e", padx=10, pady=10)

			lblAP=Label(miframe, text = "Ap. Paterno:")
			lblAP.grid(row=3, column=0, sticky="e", padx=10, pady=10)
			cajaAP = Entry(miframe)
			cajaAP.grid(row=3, column=1, sticky="e", padx=10, pady=10)

			lblAM=Label(miframe, text = "Ap. Materno:")
			lblAM.grid(row=4, column=0, sticky="e", padx=10, pady=10)
			cajaAM = Entry(miframe)
			cajaAM.grid(row=4, column=1, sticky="e", padx=10, pady=10)

			lblTel=Label(miframe, text = "Telefono:")
			lblTel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

			lblTelF=Label(miframe, text = "Telefono Fijo:")
			lblTelF.grid(row=6, column=0, sticky="e", padx=10, pady=10)
			cajaTelF = Entry(miframe)
			cajaTelF.grid(row=6, column=1, sticky="e", padx=10, pady=10)

			lblTelM=Label(miframe, text = "Telefono movil:")
			lblTelM.grid(row=7, column=0, sticky="e", padx=10, pady=10)
			cajaTelM = Entry(miframe)
			cajaTelM.grid(row=7, column=1, sticky="e", padx=10, pady=10)

			lblEM=Label(miframe, text = "Email:")
			lblEM.grid(row=8, column=0, sticky="e", padx=10, pady=10)

			lblEM1=Label(miframe, text = "Email:")
			lblEM1.grid(row=9, column=0, sticky="e", padx=10, pady=10)
			cajaEM1 = Entry(miframe)
			cajaEM1.grid(row=9, column=1, sticky="e", padx=10, pady=10)

			lblEM2=Label(miframe, text = "Email 2:")
			lblEM2.grid(row=10, column=0, sticky="e", padx=10, pady=10)
			cajaEM2 = Entry(miframe)
			cajaEM2.grid(row=10, column=1, sticky="e", padx=10, pady=10)

			lblDOM=Label(miframe, text = "Domicilio:")
			lblDOM.grid(row=0, column=2, sticky="e", padx=10, pady=10)

			lblCalle=Label(miframe, text = "Calle:")
			lblCalle.grid(row=1, column=2, sticky="e", padx=10, pady=10)
			cajaCalle = Entry(miframe)
			cajaCalle.grid(row=1, column=3, sticky="e", padx=10, pady=10)

			lblNext=Label(miframe, text = "Num. Ext:")
			lblNext.grid(row=2, column=2, sticky="e", padx=10, pady=10)
			cajaNext = Entry(miframe)
			cajaNext.grid(row=2, column=3, sticky="e", padx=10, pady=10)

			lblNint=Label(miframe, text = "Num. Int:")
			lblNint.grid(row=3, column=2, sticky="e", padx=10, pady=10)
			cajaNint = Entry(miframe)
			cajaNint.grid(row=3, column=3, sticky="e", padx=10, pady=10)

			lblCol=Label(miframe, text = "Colonia:")
			lblCol.grid(row=4, column=2, sticky="e", padx=10, pady=10)
			cajaCol = Entry(miframe)
			cajaCol.grid(row=4, column=3, sticky="e", padx=10, pady=10)

			def callbackFunc(event):
				idce=int(comboEstado.current())+1
				valores=self.model.lectura_ciudades(idce)
				comboCiudad['values']=valores

			lblEstado=Label(miframe, text = "Estado:")
			lblEstado.grid(row=5, column=2, sticky="e", padx=10, pady=10)
			comboEstado=ttk.Combobox(miframe)
			comboEstado.grid(row=5, column=3, sticky="e", padx=10, pady=10)
			comboEstado.bind("<<ComboboxSelected>>", callbackFunc)

			lblCiudad=Label(miframe, text = "Ciudad:")
			lblCiudad.grid(row=6, column=2, sticky="e", padx=10, pady=10)
			comboCiudad=ttk.Combobox(miframe)
			comboCiudad.grid(row=6, column=3, sticky="e", padx=10, pady=10)

			lblRef=Label(miframe, text = "Referencia:")
			lblRef.grid(row=7, column=2, sticky="e", padx=10, pady=10)
			cajaRef = Entry(miframe)
			cajaRef.grid(row=7, column=3, sticky="e", padx=10, pady=10)

			lblLoc=Label(miframe, text = "Localidad:")
			lblLoc.grid(row=8, column=2, sticky="e", padx=10, pady=10)
			cajaLoc = Entry(miframe)
			cajaLoc.grid(row=8, column=3, sticky="e", padx=10, pady=10)

			lblCp=Label(miframe, text = "Codigo Postal:")
			lblCp.grid(row=9, column=2, sticky="e", padx=10, pady=10)
			cajaCp = Entry(miframe)
			cajaCp.grid(row=9, column=3, sticky="e", padx=10, pady=10)

			def callbackFunc(event):
				idce=int(comboRFC.current())+1
				valores=self.model.lectura_rfc(idce)
				cajaRFC.insert(0, valores)
				valores=self.model.lectura_nombre(idce)
				cajaNombre.insert(0, valores)
				valores=self.model.lectura_apaterno(idce)
				cajaAP.insert(0, valores)
				valores=self.model.lectura_amaterno(idce)
				cajaAM.insert(0, valores)
				valores=self.model.lectura_calle(idce)
				cajaCalle.insert(0, valores)
				valores=self.model.lectura_numint(idce)
				cajaNint.insert(0, valores)
				valores=self.model.lectura_numext(idce)
				cajaNext.insert(0, valores)
				valores=self.model.lectura_colonia(idce)
				cajaCol.insert(0, valores)
				valores=self.model.lectura_cp(idce)
				cajaCp.insert(0, valores)
				valores=self.model.lectura_referencia(idce)
				cajaRef.insert(0, valores)
				valores=self.model.lectura_localidad(idce)
				cajaLoc.insert(0, valores)
				valores=self.model.lectura_telfijo(idce)
				cajaTelF.insert(0, valores)
				valores=self.model.lectura_telmovil(idce)
				cajaTelM.insert(0, valores)
				valores=self.model.lectura_email(idce)
				cajaEM1.insert(0, valores)
				valores=self.model.lectura_email2(idce)
				cajaEM2.insert(0, valores)
				comboEstado.current(10)

			def callbackFunc2(event):
				idce=int(comboNombre.current())+1
				valores=self.model.lectura_rfc(idce)
				cajaRFC.insert(0, valores)
				valores=self.model.lectura_nombre(idce)
				cajaNombre.insert(0, valores)
				valores=self.model.lectura_apaterno(idce)
				cajaAP.insert(0, valores)
				valores=self.model.lectura_amaterno(idce)
				cajaAM.insert(0, valores)
				valores=self.model.lectura_calle(idce)
				cajaCalle.insert(0, valores)
				valores=self.model.lectura_numint(idce)
				cajaNint.insert(0, valores)
				valores=self.model.lectura_numext(idce)
				cajaNext.insert(0, valores)
				valores=self.model.lectura_colonia(idce)
				cajaCol.insert(0, valores)
				valores=self.model.lectura_cp(idce)
				cajaCp.insert(0, valores)
				valores=self.model.lectura_referencia(idce)
				cajaRef.insert(0, valores)
				valores=self.model.lectura_localidad(idce)
				cajaLoc.insert(0, valores)
				valores=self.model.lectura_telfijo(idce)
				cajaTelF.insert(0, valores)
				valores=self.model.lectura_telmovil(idce)
				cajaTelM.insert(0, valores)
				valores=self.model.lectura_email(idce)
				cajaEM1.insert(0, valores)
				valores=self.model.lectura_email2(idce)
				cajaEM2.insert(0, valores)
				comboEstado.current(10)
				
			lblDatos=Label(miframe, text = "Seleccionar cliente:")
			lblDatos.grid(row=11, column=0, sticky="e", padx=10, pady=10)
			lblRfc=Label(miframe, text = "R.F.C:")
			lblRfc.grid(row=12, column=0, sticky="e", padx=10, pady=10)
			comboRFC=ttk.Combobox(miframe)
			comboRFC.grid(row=12, column=1, sticky="e", padx=10, pady=10)
			comboRFC.bind("<<ComboboxSelected>>", callbackFunc)
			
			lblNom=Label(miframe, text = "Nombre:")
			lblNom.grid(row=12, column=2, sticky="e", padx=10, pady=10)
			comboNombre=ttk.Combobox(miframe)
			comboNombre.grid(row=12, column=3, sticky="e", padx=10, pady=10)
			comboNombre.bind("<<ComboboxSelected>>", callbackFunc2)


			valores=self.model.lectura_clientes_rfc()
			comboRFC['values']=valores
			comboRFC.current(0)

			valores=self.model.lectura_clientes_nombre()
			comboNombre['values']=valores
			comboNombre.current(0)

			valores=self.model.lectura_estados()
			comboEstado['values']=valores
			comboEstado.current(0)

			def Ecat():		
				idc=int(comboCiudad.current())+1
				idcl=int(comboRFC.current())+1
				rfc=cajaRFC.get()
				nombre=cajaNombre.get()
				paterno=cajaAP.get()
				materno=cajaAM.get()
				calle=cajaCalle.get()
				numint=cajaNint.get()
				numext=cajaNext.get()
				colonia=cajaCol.get()
				cp=cajaCp.get()
				referencia=cajaRef.get()
				localidad=cajaLoc.get()
				telfijo=cajaTelF.get()
				telmovil=cajaTelM.get()
				email=cajaEM1.get()
				email2=cajaEM2.get()
				estatus=0
				fechacreacion=datetime.datetime.now()
				editcat=self.model.up_cliente(idcl, idc, rfc, nombre, paterno, materno, calle, numint, numext, colonia, cp, referencia, localidad, telfijo, telmovil, email, email2, estatus, fechacreacion)
				if editcat == True:
					ventana.destroy()
					messagebox.showinfo("Ciente","Se Actualizo el Cliente")	
				else:
					messagebox.showinfo("Ciente","No se Actualizo el Cliente")
				return
											
			botonAgragar=Button(miframe, text="Actulizar",command=Ecat)
			botonAgragar.grid(row=10, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def cliBaja():			
			ventana = Tk()
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Baja Cliente")
			ventana.geometry ("350x150")
			nlabel=Label(miframe, text = "Nombre de Cliente:")
			nlabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
			ventana.iconbitmap("amigo.ico")
			combo=ttk.Combobox(miframe)
			combo.grid(row=2, column=2, sticky="e", padx=10, pady=10)
			valores=self.model.lectura_clientes_nombre()
			combo['values']=valores
			combo.current(0)
			def Ecat():
				estatus=99
				fechamodificacion=datetime.datetime.now()				
				idcat=int(combo.current())+1
				editcat=self.model.estatus_cli(estatus, fechamodificacion, idcat)
				if editcat == True:
					ventana.destroy()
					messagebox.showinfo("Categoria","Se dio de baja cliente")	
				else:
					if editcat == None:
						messagebox.showinfo("Categoria","el cliente no existe")
					else:
						messagebox.showinfo("Categoria","No se pudo dar de baja el cliente")				
			botonAgragar=Button(miframe, text="Baja",command=Ecat)
			botonAgragar.grid(row=4, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def meseroNuevo():			
			ventana = Tk()
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Mesero Nuevo")
			ventana.geometry ("350x100")
			nlabel=Label(miframe, text = "Nombre nuevo Mesero:")
			nlabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
			ventana.iconbitmap("amigo.ico")
			caja1 = Entry(miframe)
			caja1.grid(row=2, column=2, sticky="e", padx=10, pady=10)
			def Acat():
				descripcion= caja1.get()
				estatus=0
				fechacreacion=datetime.datetime.now()
				addcat=self.model.create_mesero(descripcion, estatus, fechacreacion)
				if addcat == True:
					ventana.destroy()
					messagebox.showinfo("Mesero","Se agrego mesero")	
				else:
					if addcat == 1062:
						messagebox.showinfo("Mesero","El mesero ya existe")
					else:
						messagebox.showinfo("Mesero","No se pudo agregar mesero")
				
			botonAgragar=Button(miframe, text="agregar",command=Acat)
			botonAgragar.grid(row=3, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def meseroEditar():			
			ventana = Tk()
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Editar Mesero")
			ventana.geometry ("350x150")
			nlabel=Label(miframe, text = "Nombre de Categoria:")
			nlabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
			nlabel2=Label(miframe, text = "Nombre nuevo:")
			nlabel2.grid(row=3, column=1, sticky="e", padx=10, pady=10)
			ventana.iconbitmap("amigo.ico")
			caja1 = Entry(miframe)
			caja1.grid(row=3, column=2, sticky="e", padx=10, pady=10)
			combo=ttk.Combobox(miframe)
			combo.grid(row=2, column=2, sticky="e", padx=10, pady=10)
			valores=self.model.lectura_mesero()
			combo['values']=valores
			combo.current(0)
			def Ecat():
				descripcion= caja1.get()
				estatus=0
				fechamodificacion=datetime.datetime.now()				
				idcat=int(combo.current())+1
				editcat=self.model.edit_mesero(descripcion, fechamodificacion, idcat)
				if editcat == True:
					ventana.destroy()
					messagebox.showinfo("Mesero","Se Actualizo Mesero")	
				else:
					if editcat == None:
						messagebox.showinfo("Mesero","El mesero no existe")
					else:
						messagebox.showinfo("Mesero","No se pudo Actualizar mesero")				
			botonAgragar=Button(miframe, text="Actualizar",command=Ecat)
			botonAgragar.grid(row=4, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def meseroActivar():			
			ventana = Tk()
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Activar Mesero")
			ventana.geometry ("350x150")
			nlabel=Label(miframe, text = "Nombre de Categoria:")
			nlabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
			ventana.iconbitmap("amigo.ico")
			combo=ttk.Combobox(miframe)
			combo.grid(row=2, column=2, sticky="e", padx=10, pady=10)
			valores=self.model.lectura_mesero_baja()
			combo['values']=valores
			combo.current(0)
			def Ecat():
				estatus=0
				fechamodificacion=datetime.datetime.now()				
				idcat=int(combo.current())+1
				editcat=self.model.estatus_mesero(estatus, fechamodificacion, idcat)
				if editcat == True:
					ventana.destroy()
					messagebox.showinfo("Mesero","Se Activo mesero")	
				else:
					if editcat == None:
						messagebox.showinfo("Mesero","El mesero no existe")
					else:
						messagebox.showinfo("Mesero","No se pudo Activar Mesero")				
			botonAgragar=Button(miframe, text="Activar",command=Ecat)
			botonAgragar.grid(row=4, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def meseroBaja():			
			ventana = Tk()
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Baja Mesero")
			ventana.geometry ("350x150")
			nlabel=Label(miframe, text = "Nombre de Mesero:")
			nlabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
			ventana.iconbitmap("amigo.ico")
			combo=ttk.Combobox(miframe)
			combo.grid(row=2, column=2, sticky="e", padx=10, pady=10)
			valores=self.model.lectura_mesero_baja()
			combo['values']=valores
			combo.current(0)
			def Ecat():
				estatus=99
				fechamodificacion=datetime.datetime.now()				
				idcat=int(combo.current())+1
				editcat=self.model.estatus_mesero(estatus, fechamodificacion, idcat)
				if editcat == True:
					ventana.destroy()
					messagebox.showinfo("Mesero","Se dio de baja mesero")	
				else:
					if editcat == None:
						messagebox.showinfo("Mesero","El mesero no existe")
					else:
						messagebox.showinfo("Mesero","No se pudo dar de baja mesero")				
			botonAgragar=Button(miframe, text="Baja",command=Ecat)
			botonAgragar.grid(row=4, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def addProducto():			
			ventana = Tk()
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Agregar Producto")
			ventana.geometry ("350x350")
			nlabel=Label(miframe, text = "Categoria:")
			nlabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
			ventana.iconbitmap("amigo.ico")
			combo=ttk.Combobox(miframe)
			combo.grid(row=2, column=2, sticky="e", padx=10, pady=10)
			valores=self.model.lectura_descripcion_alta()
			combo['values']=valores
			combo.current(0)
			nlabel=Label(miframe, text = "Nombre:")
			nlabel.grid(row=3, column=1, sticky="e", padx=10, pady=10)
			cajaNombre=Entry(miframe)
			cajaNombre.grid(row=3, column=2, sticky="e", padx=10, pady=10)
			nlabel=Label(miframe, text = "Precio:")
			nlabel.grid(row=4, column=1, sticky="e", padx=10, pady=10)
			cajaPrecio=Entry(miframe)
			cajaPrecio.grid(row=4, column=2, sticky="e", padx=10, pady=10)
			nlabel=Label(miframe, text = "IVA:")
			nlabel.grid(row=5, column=1, sticky="e", padx=10, pady=10)
			cajaIva=Entry(miframe)
			cajaIva.grid(row=5, column=2, sticky="e", padx=10, pady=10)
			nlabel=Label(miframe, text = "Total:")
			nlabel.grid(row=6, column=1, sticky="e", padx=10, pady=10)
			cajaTotal=Entry(miframe)
			cajaTotal.grid(row=6, column=2, sticky="e", padx=10, pady=10)


			def Ecat():
				descripcion=cajaNombre.get()
				precio=cajaPrecio.get()
				iva=cajaIva.get()
				total=cajaTotal.get()

				estatus=0
				fechacreacion=datetime.datetime.now()				
				name=combo.get()
				idcat=2
				#idcat=self.model.lectura_descripcion_box(name)

				editcat=self.model.create_producto(idcat, descripcion, precio, iva, total, estatus, fechacreacion)
				if editcat == True:
					ventana.destroy()
					messagebox.showinfo("Producto","Se Agrego Producto")	
				else:
					if editcat == None:
						messagebox.showinfo("Producto","El Producto no existe")
					else:
						messagebox.showinfo("Producto","No se pudo Agregar el Producto")				
			botonAgragar=Button(miframe, text="Agregar",command=Ecat)
			botonAgragar.grid(row=7, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def productoActivar():			
			ventana = Tk()
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Activar Producto")
			ventana.geometry ("350x150")
			nlabel=Label(miframe, text = "Nombre de Producto:")
			nlabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
			ventana.iconbitmap("amigo.ico")
			combo=ttk.Combobox(miframe)
			combo.grid(row=2, column=2, sticky="e", padx=10, pady=10)
			valores=self.model.lectura_producto()
			combo['values']=valores
			combo.current(0)
			def Ecat():
				estatus=0
				fechamodificacion=datetime.datetime.now()				
				idcat=int(combo.current())+1
				editcat=self.model.estatus_producto(estatus, fechamodificacion, idcat)
				if editcat == True:
					ventana.destroy()
					messagebox.showinfo("Producto","Se Activo Producto")	
				else:
					if editcat == None:
						messagebox.showinfo("Producto","El Producto no existe")
					else:
						messagebox.showinfo("Producto","No se pudo Activar Producto")				
			botonAgragar=Button(miframe, text="Activar",command=Ecat)
			botonAgragar.grid(row=4, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def productoBaja():			
			ventana = Tk()
			miframe=Frame(ventana)
			miframe.pack()
			ventana.title ("Baja Producto")
			ventana.geometry ("350x150")
			nlabel=Label(miframe, text = "Nombre de Producto:")
			nlabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
			ventana.iconbitmap("amigo.ico")
			combo=ttk.Combobox(miframe)
			combo.grid(row=2, column=2, sticky="e", padx=10, pady=10)
			valores=self.model.lectura_producto()
			combo['values']=valores
			combo.current(0)
			def Ecat():
				estatus=99
				fechamodificacion=datetime.datetime.now()				
				idcat=int(combo.current())+1
				editcat=self.model.estatus_producto(estatus, fechamodificacion, idcat)
				if editcat == True:
					ventana.destroy()
					messagebox.showinfo("Producto","Se dio de baja Producto")	
				else:
					if editcat == None:
						messagebox.showinfo("Producto","El mesero no Producto")
					else:
						messagebox.showinfo("Mesero","No se pudo dar de baja Producto")				
			botonAgragar=Button(miframe, text="Baja",command=Ecat)
			botonAgragar.grid(row=4, column=2, sticky="e", padx=10, pady=10)
			ventana.mainloop()

		def nota():
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
			comboMesa=ttk.Combobox(miframe, values=["1","2","3","4","5","6","7","8","9","10"])
			comboMesa.grid(row=2, column=1, sticky="e", padx=10, pady=10)


			lblNom=Label(miframe, text = "Mesero:")
			lblNom.grid(row=3, column=0, sticky="e", padx=10, pady=10)
			comboMesero=ttk.Combobox(miframe)
			comboMesero.grid(row=3, column=1, sticky="e", padx=10, pady=10)
			valores=self.model.lectura_mesero()
			comboMesero['values']=valores
			comboMesero.current(0)



			lblNom=Label(miframe, text = "Producto:")
			lblNom.grid(row=4, column=0, sticky="e", padx=10, pady=10)
			comboProducto=ttk.Combobox(miframe)
			comboProducto.grid(row=4, column=1, sticky="e", padx=10, pady=10)
			valores=self.model.lectura_producto()
			comboProducto['values']=valores
			comboProducto.current(0)

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
											
			botonNuevo=Button(miframe, text="Nueva",command=Ecat)
			botonNuevo.grid(row=2, column=3, sticky="e", padx=10, pady=10)

			botonAgregar=Button(miframe, text="Agregar",command=Ecat)
			botonAgregar.grid(row=3, column=3, sticky="e", padx=10, pady=10)

			botonActualizar=Button(miframe, text="Imprimir",command=Ecat)
			botonActualizar.grid(row=4, column=3, sticky="e", padx=10, pady=10)

			botonPagar=Button(miframe, text="Agregar",command=Ecat)
			botonPagar.grid(row=5, column=3, sticky="e", padx=10, pady=10)
			ventana.mainloop()

#--------------------Comandos---------------------------			

		root=Tk()
		root.title("Restaurante-Bar Maricos El amigo de Silao S.A de C.V")

		barraMenu=Menu(root)
		root.config(menu=barraMenu, width=300, height=300)
		root.iconbitmap("amigo.ico")
		root.geometry("750x350")
		root.resizable(False, False)

		categoriaMenu=Menu(barraMenu, tearoff=0)
		categoriaMenu.add_command(label="Nueva", command=catNueva)
		categoriaMenu.add_command(label="Actualizar", command=catEditar)
		categoriaMenu.add_command(label="Activar", command=catActivar)
		categoriaMenu.add_command(label="Baja", command=catBaja)

		ciudadMenu=Menu(barraMenu, tearoff=0)
		ciudadMenu.add_command(label="Nueva", command=cddNueva)

		clienteMenu=Menu(barraMenu, tearoff=0)
		clienteMenu.add_command(label="Nuevo", command=cltNuevo)
		clienteMenu.add_command(label="Actualizar", command=cltEditar)
		clienteMenu.add_command(label="Baja", command=cliBaja)


		mesasMenu=Menu(barraMenu, tearoff=0)
		mesasMenu.add_command(label="Actulizar Numero", command=mesaActivar)

		meseroMenu=Menu(barraMenu, tearoff=0)
		meseroMenu.add_command(label="Nuevo", command=meseroNuevo)
		meseroMenu.add_command(label="Actualizar", command=meseroEditar)
		meseroMenu.add_command(label="Activar", command=meseroActivar)
		meseroMenu.add_command(label="Baja", command=meseroBaja)

		notaMenu=Menu(barraMenu, tearoff=0)
		notaMenu.add_command(label="Nueva", command=nota)
		notaMenu.add_command(label="Cancelar")
		notaMenu.add_command(label="Pagar")

		productoMenu=Menu(barraMenu, tearoff=0)
		productoMenu.add_command(label="Nuevo", command=addProducto)
		productoMenu.add_command(label="Actualizar")
		productoMenu.add_command(label="Activar", command=productoActivar)
		productoMenu.add_command(label="Baja", command=productoBaja)

		reporteMenu=Menu(barraMenu, tearoff=0)
		reporteMenu.add_command(label="Facturas")
		reporteMenu.add_command(label="Movimientos")
		reporteMenu.add_command(label="Notas")

		acercadeMenu=Menu(barraMenu, tearoff=0)
		acercadeMenu.add_command(label="Licencia", command=acecadeNosotros)


		salirMenu=Menu(barraMenu, tearoff=0)
		salirMenu.add_command(label="Salir",command=salirAplicacion)

		barraMenu.add_cascade(label="Categoria", menu=categoriaMenu)
		barraMenu.add_cascade(label="Ciudad", menu=ciudadMenu)
		barraMenu.add_cascade(label="Cliente", menu=clienteMenu)

		barraMenu.add_cascade(label="Mesas", menu=mesasMenu)
		barraMenu.add_cascade(label="Mesero", menu=meseroMenu)
		barraMenu.add_cascade(label="Nota", menu=notaMenu)
		barraMenu.add_cascade(label="Producto", menu=productoMenu)
		barraMenu.add_cascade(label="Reportes", menu=reporteMenu)
		barraMenu.add_cascade(label="Acerca de...", menu=acercadeMenu)
		
		barraMenu.add_cascade(label="Salir", menu=salirMenu)

		root.mainloop()


	


			
