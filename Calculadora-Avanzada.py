import math
try:
    f = open("calculadora.txt", "r")
except FileNotFoundError:
    pass

try:
    
    signo = input("Que vas ahacer?(+,-,/,x,^,sqrt) ")
    
    if signo == "sqrt":
        try:
            raiz = int(input("Que numero quieres hallar la raiz cuadrada? "))
            print(f"sqrt({raiz}) = {math.sqrt(raiz)}")

            f = open("calculadora.txt", "a")
            f.write(f"sqrt({raiz}) = {math.sqrt(raiz)}\n")
        except:
            print("Prueba un numero.")

    else:
        if signo == "+":
            try:
                primero = int(input("Que numero vas a escribir primero? "))
                segundo = int(input("Cual seria el segundo numero? "))
                print(f"{primero} + {segundo} = {primero + segundo}")

                f = open("calculadora.txt", "a")
                f.write(f"{primero} + {segundo} = {primero + segundo}\n")
            except:
                print("Prueba un numero.")

        if signo == "-":
            try:
                primero = int(input("Que numero vas a escribir primero? "))
                segundo = int(input("Cual seria el segundo numero? "))
                print(f"{primero} - {segundo} = {primero - segundo}")

                f = open("calculadora.txt", "a")
                f.write(f"{primero} - {segundo} = {primero - segundo}\n")
            except:
                print("Prueba un numero.")

        if signo == "/":
            try:
                primero = int(input("Que numero vas a escribir primero? "))
                segundo = int(input("Cual seria el segundo numero? "))
                print(f"{primero} / {segundo} = {primero / segundo}")

                f = open("calculadora.txt", "a")
                f.write(f"{primero} / {segundo} = {primero / segundo}\n")
            except:
                print("Prueba un numero.")

        if signo == "x":
            try:
                primero = int(input("Que numero vas a escribir primero? "))
                segundo = int(input("Cual seria el segundo numero? "))
                print(f"{primero} x {segundo} = {primero * segundo}")

                f = open("calculadora.txt", "a")
                f.write(f"{primero} x {segundo} = {primero * segundo}\n")
            except:
                print("Prueba un numero.")

        if signo == "^":
            try:
                primero = int(input("Que numero vas a escribir primero? "))
                segundo = int(input("Cual seria el segundo numero? "))
                print(f"{primero}^{segundo} = {primero ** segundo}")

                f = open("calculadora.txt", "a")
                f.write(f"{primero}^{segundo} = {primero ** segundo}\n")
            except:
                print("Prueba un numero.")
        
        else:
            print("Signo no encontrado.")
except:
    print("Error.")
    