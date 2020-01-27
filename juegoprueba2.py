def juego():
	NombreJugador = input("¡HOLA!, POR FAVOR, INTRODUZCA SU NOMBRE: ")

	while len(NombreJugador) == 0:
		print("HA HABIDO UN ERROR, TIENES QUE INTRODUCIR UN NOMBRE.")
		NombreJugador = input("¡HOLA!, POR FAVOR, INTRODUZCA SU NOMBRE CORRECTAMENTE: ")

	print("-¿?: ¡HOLA! " + NombreJugador + " TE ACABAS DE DESPERTAR DE UN SUEÑO MUY PROFUNDO.")
	print("-" + NombreJugador + ": ¿DON...DONDE ESTOY?")
	print("-¿?: ESTAS EN UN REFUGIO. EL MUNDO A SIDO DESTRUIDO POR ALIENIGENAS MALVADOS.")
	print("-" + NombreJugador + (": ¡ME CAGO EN LA PUTA, DONDE ESTA MI CASA!"))
	print("-¿?: SEGURAMENTE ESTE DESTRUIDA, COMO TODO LO DEMAS. EN ESTE REFUGIO SOLO ESTAMOS TU Y YO, Y ES IMPOSIBLE SALIR FUERA." + "\n" + "LOS ALIENIGENAS TE MATARIAN.")
	print("-" + NombreJugador + ": ¡NO PUEDE SER, AHORA QUE HAGO, ESTABA ACABANDO MI PAGINA DE CHISTES!")
	print("-¿?: PO DESPIDETE DE ELLA")
	print("-" + NombreJugador + ": BUENO HARE OTRA, ¿COMO TE LLAMAS?")

	NombreAmigo = input("-¿?: ME LLAMO: ")

	while len(NombreAmigo) == 0:
		print("¡HOLA " + NombreJugador + "! HA HABIDO UN ERROR AL INTRODUCIR EL NOMBRE DE SU COMPAÑERO.")
		NombreAmigo = input("POR FAVOR, INTRODUZCA EL NOMBRE DE SU COMPAÑERO: ")

	print("-" + NombreJugador + ": QUE NOMBRE MAS FEO JAJAJAJAJA.")
	print("-" + NombreAmigo + ": PO ANDA QUE EL TUYO JAJAJAJAJA.")
	print("-" + NombreAmigo + ": BUENO DEJEMONOS DE TONTERIAS, TENEMOS QUE REPOBLAR LA TIERRA.")
	print("-" + NombreJugador + ": ANTES TENDREMOS QUE SALIR DE AQUI NO.")
	print("-" + NombreAmigo + ": TE HE DICHO ANTES QUE NO PODEMOS SALIR DE AQUI, LOS ALIENIGENAS NOS MATARAN.")
	print("-MAQUINA: " + NombreJugador + " ,¿QUE QUIERES HACER:?" + "\n" + "A: SALIR DEL REFUGIO B: QUEDARTE DENTRO DEL REFUGIO")

	op = str(input(""))
	op = op.upper()

	if op == "A":
		print("LOS ALIENIGENAS TE HAN COMIDO UNA PIERNA Y NO PUEDES MOVERTE, TE QUEDA POCO TIEMPO DE VIDA ")
		print("TU COMPAÑERO " + NombreAmigo + " TE HA ABANDONADO Y NO PUEDES SOBREVIVIR SIN EL. HAS MUERTO")

	elif op == "B":
		print("BIEN HECHO " + NombreJugador + " AQUI ESTARAS ASALVO")
		print(NombreAmigo + " ESTE REFUGIO ES BASTANTE GRANDE, " + NombreJugador + " ¿VIENES A EXPLORAR?")
		print("A: SALIR A EXPLORAR B: QUEDARTE PARADO")
		op = str(input(""))
		op = op.upper()

		if op == "A":
			print(NombreAmigo + " ¡MIRA " + NombreJugador + " , UN TESORO!")
			print("¿QUIERES HABRIRLO? A: ABRES EL COFRE B: LO DEJAS CERRADO")

		elif op == "B":
			

	else:
		print("NO HAS ESCOJIDO LA OPCION CORRECTA, FIN DEL PROGRAMA.")



juego()







	
