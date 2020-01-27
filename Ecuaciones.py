import math

a = int(input("DIME EL NUMERO QUE VA CON LA X^2: "))
b = int(input("DIME EL NUMERO QUE VA CON LA X: "))
c = int(input("DIME EL NUMERO QUE NO TIENE INCOGNITA: "))
div = 0
result = 0
result1 = 0

#print("X^2 = " + str(a))
#print("X = " + str(b))
#print("NUMERO SIN INCOGNITA = " + str(c))
while a == 0 or b == 0 or c == 0:
	print("HA HABIDO UN ERROR, POR FAVOR VUELVE A INTRODUCIR LOS NUMEROS")
	a = int(input("DIME EL NUMERO QUE VA CON LA X^2: "))
	b = int(input("DIME EL NUMERO QUE VA CON LA X: "))
	c = int(input("DIME EL NUMERO QUE NO TIENE INCOGNITA: "))

result = b**2 -4*a*c
#print(result)

if result <= 0:
	print("NO SE PUEDE HACER LA RAIZ CUADRADA DE UN NUMERO NEGATIVO.")
else:
	result = math.sqrt(result)
	#print(result)
	result1 = result
	#print(result1)
	b = -b
	#print(b)
	div = 2*a
	#print(div)

	result = b + result
	result = result / div
	print("EL PRIMER RESULTADO ES: " + str(result))

	result1 = b - result1
	result1 = result1 / div
	print("EL SEGUNDO RESULTADO ES: " + str(result1))


