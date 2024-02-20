frase = input("Decime una frase y calculo cuanto tardarias en decirla: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
if cantidad_de_palabras > 120: 
    print ("Tu texto es demasiado largo. Intenta algo mas corto.")

print(f'Ingresaste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Eminem lo diria en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos')