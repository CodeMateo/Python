import os

directorio_actual = os.getcwd()
print("ESTE ES TU DIRECTORIO ACTUAL: " + directorio_actual)

directorio = input("NOMBRE CARPETA: ")
directorio_padre = "/home/nicolas/Escritorio/Python"
ruta = os.path.join(directorio_padre, directorio) 
 
os.mkdir(ruta) 
print("CARPETA " + directorio + "CREADA EN: " + directorio_padre) 

nombre_file = input("NOMBRE DEL ARCHIVO: ")
file = open(ruta + "/" + nombre_file, "w")
file.write("HOLA ESTO ES UNA PRUEBA")
file.close()
