#Sumar valores
nombre = input("Ingresa tu nombre: ")

def suma(nombre,*numeros):
    return f"{nombre}, la suma de los numeros del codigo es: {sum(numeros)}"

resultado = suma(f"{nombre}",1,2,3,4,5,3)
print(resultado) 
