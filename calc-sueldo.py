ingreso_mensual = input("Ingrese su ingreso mensual: ")
gasto_mensual = input("Ingrese su gasto mensual: ")

if int(ingreso_mensual) > 10000: 
    if int(ingreso_mensual) - gasto_mensual < 0:
        print("Estas en deficit")
    elif int(ingreso_mensual) - int(gasto_mensual) > 1000:
        print("Estas bien economicamente")
    else:
        print("Estas gastando demasiado dinero mensual")

elif int(ingreso_mensual) > 1000: 
    print("Estas bien economicamente como para vivir en Latinoamerica")
    
elif int(ingreso_mensual) > 500: 
    print("Estas bien economicamente como para vivir en Argentina")
    
elif int(ingreso_mensual) > 200: 
    print("Estas bien economicamente como para vivir en Venezuela")

else:
    print("Sos pobre")
