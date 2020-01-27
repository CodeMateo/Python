import math
import sys

print("CALCULADORA SIMPLE")
print("OPCIONES:")
print("ESCRIBE '+' PARA SUMAR DOS NUMEROS")
print("ESCRIBE '-' PARA RESTAR DOS NUMEROS")
print("ESCRIBE '*' PARA MULTIPLICAR DOS NUMEROS")
print("ESCRIBE '/' PARA RESTAR DOS NUMEROS")
print("ESCRIBE 'R' PARA HACER LA RAIZ CUADRADA DE UN NUMERO")
print("ESCRIBE 'EC' PARA HACER UNA ECUACION DE 2º GRADO")
print("ESCRIBE 'S' PARA SALIR DEL PROGRAMA")


op = str(input(": "))

if op.upper() == "S":
	print("FIN DEL PROGRAMA")
	sys.exit()

elif op.upper() == "+":
	num1 = float(input("DIME EL PRIMER NUMERO:")) 
	num2 = float(input("DIME EL SEGUNDO NUMERO:")) 
	result = num1 + num2
	print(result)
	print("¿QUIERE HACER OTRA OPERACION?")
	again = str(input(" "))


elif op.upper() == "-":
	num1 = float(input("DIME EL PRIMER NUMERO:")) 
	num2 = float(input("DIME EL SEGUNDO NUMERO:")) 
	result = num1 - num2
	print(result)
	print("¿QUIERE HACER OTRA OPERACION?")
	again = str(input(" "))

elif op.upper() == "*":
	num1 = float(input("DIME EL PRIMER NUMERO:")) 
	num2 = float(input("DIME EL SEGUNDO NUMERO:")) 
	result = num1 * num2
	print(result)
	print("¿QUIERE HACER OTRA OPERACION?")
	again = str(input(" "))

elif op.upper() == "/":
	num1 = float(input("DIME EL PRIMER NUMERO:")) 
	num2 = float(input("DIME EL SEGUNDO NUMERO:")) 
	result = num1 / num2
	print(result)
	print("¿QUIERE HACER OTRA OPERACION?")
	again = str(input(" "))

elif op.upper() == "R":
	num1 = float(input("DIME UN NUMERO:")) 
	result = math.sqrt(num1)
	print(result)
	print("¿QUIERE HACER OTRA OPERACION?")
	again = str(input(" "))

elif op.upper() == "EC":
	a = float(input("DIME EL NUMERO QUE VA CON LA X^2: "))
	b = float(input("DIME EL NUMERO QUE VA CON LA X: "))
	c = float(input("DIME EL NUMERO QUE NO TIENE INCOGNITA: "))
	div = 0
	result = 0
	result1 = 0

	while a == 0 or b == 0 or c == 0:
		print("HA HABIDO UN ERROR, POR FAVOR VUELVE A INTRODUCIR LOS NUMEROS")
		a = int(input("DIME EL NUMERO QUE VA CON LA X^2: "))
		b = int(input("DIME EL NUMERO QUE VA CON LA X: "))
		c = int(input("DIME EL NUMERO QUE NO TIENE INCOGNITA: "))

	result = b**2 -4*a*c

	if result <= 0:
		print("NO SE PUEDE HACER LA RAIZ CUADRADA DE UN NUMERO NEGATIVO.")
		print("¿QUIERE HACER OTRA OPERACION?")
		again = str(input(" "))
	else:
		result = math.sqrt(result)
		result1 = result
		b = -b
		div = 2*a

		result = b + result
		result = result / div
		print("EL PRIMER RESULTADO ES: " + str(result))

		result1 = b - result1
		result1 = result1 / div
		print("EL SEGUNDO RESULTADO ES: " + str(result1))
		print("¿QUIERE HACER OTRA OPERACION?")
		again = str(input(" "))

else:
	print("COMANDO ERRONEO")
	print("FIN DEL PROGRAMA")
	sys.exit()

while again.upper() == "SI":
	print("")
	print("OPCIONES:")
	print("ESCRIBE '+' PARA SUMAR DOS NUMEROS")
	print("ESCRIBE '-' PARA RESTAR DOS NUMEROS")
	print("ESCRIBE '*' PARA MULTIPLICAR DOS NUMEROS")
	print("ESCRIBE '/' PARA RESTAR DOS NUMEROS")
	print("ESCRIBE 'R' PARA HACER LA RAIZ CUADRADA DE UN NUMERO")
	print("ESCRIBE 'EC' PARA HACER UNA ECUACION DE 2º GRADO")
	print("ESCRIBE 'S' PARA SALIR DEL PROGRAMA")

	op = str(input(": "))

	if op.upper() == "S":
		print("FIN DEL PROGRAMA")
		sys.exit()

	elif op.upper() == "+":
		num1 = float(input("DIME EL PRIMER NUMERO:")) 
		num2 = float(input("DIME EL SEGUNDO NUMERO:")) 
		result = num1 + num2
		print(result)
		print("¿QUIERE HACER OTRA OPERACION?")
		again = str(input(" "))


	elif op.upper() == "-":
		num1 = float(input("DIME EL PRIMER NUMERO:")) 
		num2 = float(input("DIME EL SEGUNDO NUMERO:")) 
		result = num1 - num2
		print(result)
		print("¿QUIERE HACER OTRA OPERACION?")
		again = str(input(" "))

	elif op.upper() == "*":
		num1 = float(input("DIME EL PRIMER NUMERO:")) 
		num2 = float(input("DIME EL SEGUNDO NUMERO:")) 
		result = num1 * num2
		print(result)
		print("¿QUIERE HACER OTRA OPERACION?")
		again = str(input(" "))

	elif op.upper() == "/":
		num1 = float(input("DIME EL PRIMER NUMERO:")) 
		num2 = float(input("DIME EL SEGUNDO NUMERO:")) 
		result = num1 / num2
		print(result)
		print("¿QUIERE HACER OTRA OPERACION?")
		again = str(input(" "))

	elif op.upper() == "R":
		num1 = float(input("DIME UN NUMERO:")) 
		result = math.sqrt(num1)
		print(result)
		print("¿QUIERE HACER OTRA OPERACION?")
		again = str(input(" "))

	elif op.upper() == "EC":
		a = float(input("DIME EL NUMERO QUE VA CON LA X^2: "))
		b = float(input("DIME EL NUMERO QUE VA CON LA X: "))
		c = float(input("DIME EL NUMERO QUE NO TIENE INCOGNITA: "))
		div = 0
		result = 0
		result1 = 0

		while a == 0 or b == 0 or c == 0:
			print("HA HABIDO UN ERROR, POR FAVOR VUELVE A INTRODUCIR LOS NUMEROS")
			a = int(input("DIME EL NUMERO QUE VA CON LA X^2: "))
			b = int(input("DIME EL NUMERO QUE VA CON LA X: "))
			c = int(input("DIME EL NUMERO QUE NO TIENE INCOGNITA: "))

		result = b**2 -4*a*c

		if result <= 0:
			print("NO SE PUEDE HACER LA RAIZ CUADRADA DE UN NUMERO NEGATIVO.")
		else:
			result = math.sqrt(result)
			result1 = result
			b = -b
			div = 2*a

			result = b + result
			result = result / div
			print("EL PRIMER RESULTADO ES: " + str(result))

			result1 = b - result1
			result1 = result1 / div
			print("EL SEGUNDO RESULTADO ES: " + str(result1))
			print("¿QUIERE HACER OTRA OPERACION?")
			again = str(input(" "))

	else:
		print("COMANDO ERRONEO")
		print("FIN DEL PROGRAMA")
		sys.exit()
		
print("FIN DEL PROGRAMA")
