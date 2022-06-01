from random import randint

    

personas = ["Laura", "Irene", "Clara",
            "Lorena", "Fran", "Jose", "Javi", "Raul"]
clases = ["Guerrero", "Hechicero", "Bárbaro", "Paladín",
        "Explorador", "Pícaro", "Tirador", "Clerigo"]

asignado = ["","","","","","","",""]

for i,clase in enumerate(clases):
    guardado = False
    while not guardado:
        posicion = randint(0, 7)
        if asignado[posicion] == "":
            asignado[posicion] = clase
            guardado = True

print("Se ha asignado:")
for i,alumno in enumerate(personas):
    print(f"{alumno} : {asignado[i]}")
print("\n--------------\n")