pre = 0
ter = 0
cua = 0
qui = 0

est = int(input("Ingrese la edad del estudiante: "))

while est != -1:
    if est <= 8:
        pre += 1
    elif est <= 10:
        ter += 1
    elif est <= 13:
        cua += 1
    elif est <= 16:
        qui += 1
    else:
        print("edad no valida")

    est = int(input("Ingrese la edad del estudiante: "))

print(pre)
print(ter)
print(cua)
print(qui)
