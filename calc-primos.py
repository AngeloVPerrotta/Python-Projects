#Creando una funcion que nos devuelva los numeros primos entre 0 y el argumento que le pasamos

def es_primo(num):
    for i in range (2,int(num)-1):
        if int(num)%i==0: return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(3,int(num)+1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos

resultado = primos_hasta(input("Ingrese el numero hasta cual desea obtener los numeros primos: "))
print(resultado)