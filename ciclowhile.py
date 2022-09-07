#CICLO MIENTRAS 

#DECLARAR UNA VARIABLE CENTINELA
#O VARIABLE DE CONTROL PARA EVALUAR
#LA EJECUCICÓN DE MI CICLO
i=0

suma = 0
resta = 0
multiplicacion = 0
raiz = 0
num = 0

#MENU DE OPCIONES
print("***MENU***")
print("1.Sumar 2 numeros")
print("2. restar 2 numeros")
print("3. encontrar la raiz cuadrada de un numero")
print("4. multiplicar 2 numeros")
print("5. Salir")

#programar la estructura del ciclo mientras
while(i!=5):
    i=int(input("Digite una opción del menú: "))

    if(i==1):
        print("")
    elif(i==2):
        print("",i)
    elif(i==3):
        print("")
    elif(i==4):
        print("")
    elif(i==5):
        break
    else:
        print("Digita una opción válida")
    
print("salimos del while")