import os
from tkinter import*

pn = Tk()
pn.resizable(False, False)
pn.config(bg="white smoke")
pn.geometry("800x600")

texto = Label(pn, text="NOMBRE DE LA CARPETA: ")
texto.grid(row=1, column=1)
texto.config(bg="white smoke")

texto1 = Label(pn, text="RUTA: ")
texto1.grid(row=2, column=1)
texto1.config(bg="white smoke")

carpeta_nombre = StringVar()
carpeta = Entry(pn, textvariable=carpeta_nombre)
carpeta.grid(row=1, column=2)

ruta_nombre = StringVar()
ruta = Entry(pn, textvariable=ruta_nombre)
ruta.grid(row=2, column=2)

boton = Button(pn, text="OKEY")
boton.grid(row=3,column=2)

pn.mainloop()


#directorio = input("¿COMO SE LLAMARA EL DIRECTORIO?: ")
#ruta = "/Carpeta personal/Escritorio/Python"
#path = os.path.join(ruta, directorio) 
  
#os.mkdir(path) 
#print("Directory '%s' created" %directorio) 
























