import random 
import os
import time

#---------------------------------------------------------------------------------------------------------------------------------------#
def clean():
    os.system('clear' if os.name == "posix" else "cls")

########################
### Inicio del Juego ###
########################

while True: #while true que nos envuelve todo para poder cerrar el juego desde una pregunta despues de jugar
    clean()
#---------------------------------------------------------------------------------------------------------------------------------------#


#################
### variables ###
#################


    Game = False #valor para iniciar ó no iniciar el juego 
    usado = set() #caja para nuestros numeros adivinados 
    Dificultad = {"facil" : 70, "medio" : 100, "dificil" : 200, "hardcore" : 1000}

#---------------------------------------------------------------------------------------------------------------------------------------#


########################
### Mensaje de Inicio###
########################

    print("\n¡Bienvenido a Adivina el numero!\n\n")
    
        

#---------------------------------------------------------------------------------------------------------------------------------------#


 ##########################
 ### Pantañña de inicio ###
 ##########################

    while True:
        clean()


        print("¿Quieres jugar?\n")
        respuesta = input("\n ¿Sí o No?\n\n ·> ").lower().strip()

        if respuesta == "si":
            Game = True
            break
        elif respuesta == "no":
            print("a pinche bato ondeado alv, sakese\n\n Bye!!")
            Game = False
            break
        else:
            print("\n ¿Acaso no sabes responder a una simple pregunta?")
            time.sleep(2)

    if not Game:
        break   

    if Game == True:
        print("↓↓↓ Escoge tu Dificultad ↓↓↓\n\n")
        

        while True:
            clean()
            difi = input("→ Facil, Medio, Dificil ó Hardcore ←\n ·> ").lower().strip()

            if difi in Dificultad: # osea si lo que sale de Difi existe en Dificultad de ahi lo tomaremos
                MaxNum = Dificultad[difi]
                break
            else:
                print("No te entendí\n\n\n hint: recuerda usar las palabras: facil, medio dificil ó hardcore")
#---------------------------------------------------------------------------------------------------------------------------------------#
      

    ## sistema de vidas: 
        if MaxNum == 70:
            intentos = 7
            print("en serio? esto es para niños")
            time.sleep(2)
        elif MaxNum == 100:
            intentos = 7
            print("no te gusta la dificultad")
            time.sleep(2)
        elif MaxNum == 200:
            intentos = 6
            print("ojitooo ya casi vas por el camino del Jedi")
            time.sleep(2)
        else:
            intentos = 8
            print("mis respetos para uste' caballero")
            time.sleep(2)
#---------------------------------------------------------------------------------------------------------------------------------------#

 ########################
 ### logica del juego ###
 ########################
        
        secreto = random.randint(1, MaxNum)      

        while True:
            clean()
            
            print(f"adivina el numero del 1 al {MaxNum}\n")
            if usado:
                print(f"Ya pobaste: {sorted(usado)}\n")

            adivina = input(" ·> ")

            try:
                adivina = int(adivina)
            except ValueError:
                print(f"Aqui solamente jugamos con numeros\n intenta escribir un numero entero entre 1 y {MaxNum}")
                time.sleep(2)
                continue
            
            if adivina > secreto:
                print("Te pasaste\n sigue intentando")
                intentos -= 1
                print(f"Intentos restantes: {intentos}")
                time.sleep(3)
            elif adivina < secreto:
                print("te falto\n sigue intentando")
                intentos -= 1
                print(f"Intentos restantes: {intentos}")
                time.sleep(3)
            else:
                print(f"Muy bien lo conseguiste el numero es {secreto}\n\n    Gracias por jugar!")
                input("Presiona Enter para volver al menu")
                break
            
            
            if intentos == 0:
                print("te has quedado sin intentos")
                input("Presiona Enter para volver al menu")
                break
                