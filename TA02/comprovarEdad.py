edad = int(input("Introduce tu edad: "))

if edad < 0:
    print("Edad no válida")
elif edad < 18:
    print("Eres menor de edad")
elif edad < 65:
    print("Eres mayor de edad")
else:
    print("Eres viejito")

print("Programa Finalizado")