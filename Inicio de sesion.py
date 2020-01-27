usuario = input("ESTABLEZCA UN NOMBRE DE USUARIO: ")
contraseña = input("ESTABLEZCA UNA CONTRASEÑA: ")
contador = 0

for i in range(len(contraseña)):

	if contraseña[i] == " ":
		contador = 1

while len(contraseña) <8 or contador >0:
	print("CONTRASEÑA ERRONEA")
	print("ESTABLEZCA UNA CONTRASEÑA VALIDA, DEBE TENER MINIMO 8 CARACTERES Y NO PUEDE TENER ESPACIOS EN BLANCO: ")
	contraseña = input("VUELVA A INTENTARLO: ")
	
else:
	print("CONTRASEÑA CORRECTA")

validador_usuario = str(input("CUAL ES EL NOMBRE DE USUARIO: "))
validador_contraseña = input("CUAL ES LA CONTRASEÑA: ")

while str(contraseña.lower()) != validador_contraseña.lower() and str(usuario.lower()) != validador_usuario.lower():
	print("INICO DE SESION INCORRECTO " + "\n" + "REVISE SI LA INFORMACION ES CORRECTA")
	validador_usuario = str(input("CUAL ES EL NOMBRE DE USUARIO: "))
	validador_contraseña = input("CUAL ES LA CONTRASEÑA: ")
else:
	print("INICIO DE SESION CORRECTO")	
