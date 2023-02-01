import sys
print("Instituto de Médicina General.")
print("")
print("Para conocer el Indice de Masa Corporal introduce los siguientes datos:")
print("")    



nombre = input("Nombre(S): ")
primerApellido = input("Apellido Paterno: ")
segundoApellido = input("Apellido Materno: ")
edad = int(input("Edad: "))

def main():
    peso = input("Peso: ")
    if peso.isnumeric():
        peso=int(peso)
    else:
        print("Se requiere un dato numerico")
        sys.exit(-1)

    estatura = input("Estatura en cm:")
    if estatura.isnumeric():
        estatura=int(estatura)
    else:
        print("Se requiere un dato numerico")
        sys.exit(-1)


    multiplicacion = estatura * estatura
    division = peso / multiplicacion
    imc = division * 10000

    print("")

    print("Sr(a). " + (nombre) + " " + (primerApellido) + " " + (segundoApellido) + ", tu indice de masa corporal es de: ")
    print("%.2f" %imc)
    print("")

    print("""En esta tabla identifica la posicion en la que te encuentras:
        Menor a 18.9 = Peso bajo
        18.50 a 24.99 = Peso normal
        25.00 a 29.99 = sobrepeso
        30.00 a 34.99 = obesidad leve
        35.00 a 39.99 = Obesidad media
        Mayor a 40.00 = obesidad morbida
    
    ¡Gracias por utilizar nuestra plataforma!""")

if __name__== "__main__":
    main()