edad = 19

a = int(input("Qué edad tengo ="))

while a < 19:
    print("Un poco más")
    a = int(input("Qué edad tengo?"))
if a > 19:
    print("Un poco menos")
    a = int(input("Qué edad tengo?"))
if a == 19:
    print(f"Correcto tengo {a} años ")