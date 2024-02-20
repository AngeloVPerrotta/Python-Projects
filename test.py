nombre = input("Ingresa tu nombre: ")
sexo = input("Ingresa tu sexo: ")

#creando una funcion con parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "Genia"
    elif (sexo == "hombre"):
        adjetivo = "Genio"
    else:
        adjetivo = 'Crack'

    print(f"Hola {nombre}, {adjetivo} de la vida ¿Como estas?")

saludar(f"{nombre}",f"{sexo}")