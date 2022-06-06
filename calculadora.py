print("CALCULADORA\n")
num1 = float(input("ingrese un número: "))
num2 = float(input("ingrese un número: "))
print("s para sumar \nr para restar \nm para multiplicar \nd para dividir")
op = input("ingrese la operación: ")

if op == "s":
    suma = num1+num2
    print(suma)
elif op == "r":
    resta = num1-num2
    print(resta)
elif op == "m":
    mult = num1*num2
    print(mult)
elif op == "d":
    div = num1/num2
    print(div)
else:
    print("operacion no disponible")
print()
print("Fin del programa")
