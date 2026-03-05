while True : 
    print ("Elige la operacion a realizar")
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Salir")
    operacion = input("Operacion: ")
    if operacion == "5": 
        print("Gracias por usar la calculadora, suerte en tus ejercicios")
        break 
    num1= float(input("Escribe el primer numero: "))
    num2= float(input("Escribe el segundo numero: ")) 
    if operacion == "1":
        resultado = num1+num2 
        print("Resultado: ", resultado )
    elif operacion == "2":
        resultado = num1-num2 
        print("Resultado: ", resultado )
    elif operacion == "3":
        resultado = num1*num2 
        print("Resultado: ", resultado )
    elif operacion == "4":
        if num2!=0:
            resultado = num1 / num2
            print("Resultado: ", resultado)
        else:
            print("Error en la operacion, Operacion invalida")
    else: 
        print("Operacion no disponible")