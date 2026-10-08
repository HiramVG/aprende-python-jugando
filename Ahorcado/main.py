import random 
import os
#-------------------------------------------------------------------------------------------------------------------------------------------------#
### herramientas
def limpiar(): #usamos la info del SO para escribir un comando en automatico que limpie la pantalla
    os.system('clear' if os.name == 'posix' else 'cls')


### AScii Art del jugador

Player = [

"""
     •----•
     |    |
          |
          |
          |
          |
        ¯¯¯¯¯
""",
"""
     •----•
     |    |
     O    |
          |
          |
          |
        ¯¯¯¯¯
""",

"""
     •----•
     |    |
     O    |
     |    |
          |
          |
        ¯¯¯¯¯
""",


"""
     •----•
     |    |
     O    |
     |\   |
          |
          |
        ¯¯¯¯¯
""",

"""
     •----•
     |    |
     O    |
    /|\   |
          |
          |
        ¯¯¯¯¯
""",

"""
     •----•
     |    |
     O    |
    /|\   |
      \   |
          |
        ¯¯¯¯¯
""",


"""
     •----•
     |    |
     O    |
    /|\   |
    / \   |
          |
        ¯¯¯¯¯
"""   
   ]

while True: #bucle que envuelve todo pa reiniciarse (ultimo while true)
    limpiar()

#-------------------------------------------------------------------------------------------------------------------------------------------------#
    ### VARIABLES ###
    
    palabras = ["cheetos", "linterna", "cocina", "encendedor", "pasillo", "araña", "comezón", "computadora","cerveza", "celular", "biologia"]
    secreta = random.choice(palabras) # <-- elige una palabra de la lista
    tablero = ["_"] * len(secreta) #reemplaza la longitus secreta y pone un "_" por cáracter
    intentos = 6 
    
    jugar = False # si no inicia con True no permite ingresar al juego
    usadas = set() # cajita para letras usadas

#-------------------------------------------------------------------------------------------------------------------------------------------------#

    ### MENSAJE DE INICIO ###
    print("¿listo para jugar ahorcado?")

#-------------------------------------------------------------------------------------------------------------------------------------------------#

    ### LOGICA DEL JUEGO ###

    while True: #primer bucle

        respuesta = input("\n  si ó no? \n --> ").lower().strip() # .lower hacen todas minusculas y .strip quita espacios inecesarios

        if respuesta == "si":
            limpiar()
            print("¡comencemos!") 
            jugar = True 
            break #rompe el bucle while  (si es la ultima salida se cierra el programa)
        elif respuesta == "no":   # elif solo permite comparaciones no ordenes! 
            print("te dio miedo el ahorcado? (T-T)")
            jugar = False
            break
        else:
            print("intenta presionar decir 'si' ó 'no' ")

    
    if not jugar:
        print("¡¡Nos vemos!!")
        break

    if jugar == True:
        print(f"la palabra tiene {len(secreta)} letras \n Intentos: {intentos}")
        print(Player[0])
        print(f"\n\n\n {' '.join(tablero)}\n\n\n")


        while intentos > 0 and "_" in tablero:

            apuesta = input("\n\n\na, b, c, ... x, y ,z \n\n\n --- solo 1 letra --- \n").lower().strip() # apuesta tu suerte letra por letra
            limpiar()
            errores = 6 - intentos


            if len(apuesta) > 1: #si el input es mayor que uno regaña al jugador
                print(Player[errores])
                print(f"\n\n\n {' '.join(tablero)}\n\n\n")
                print("Solo teclea 1 letra por favor.")
            elif apuesta in usadas:
                print(Player[errores])
                print(f"\n\n\n {' '.join(tablero)}\n\n\n")
                print(f"ya usaste la {apuesta}, prueba otra letra\n\n Usadas: {', '.join(usadas)}") # por si no se acuerda el paciente con Alzheimer de lo que uso
            elif apuesta in secreta:
                usadas.add(apuesta)
                for posicion, letra_secreta in enumerate(secreta):
                    if letra_secreta == apuesta:
                        tablero[posicion] = apuesta
                print(f"Usaste la letra {apuesta} \n\n muy bien!!! sigues con {intentos} intentos.\n\n")
                print(Player[errores])
                print(f"\n\n\n {' '.join(tablero)}\n\n\n")
                if "_" not in tablero:
                    print(Player[errores])
                    print(f"\n\n¡Ganaste! Era {secreta}")
                    input("\n Presiona ENTER para volver al menu. . .")
                
            else:
                usadas.add(apuesta)
                intentos -= 1
                errores = 6 - intentos
                print(Player[errores])
                print(f"\n\n\n {' '.join(tablero)}\n Usadas: {', '.join(usadas)}")
                print("perdiste un intento\n")
                
                print(f"\n\n\nTe quedan {intentos} intentos.")
                if intentos == 0:
                    print(Player[errores])
                    print("\n\nlastima, perdiste tus intentos. Vuelve a intentarlo")
                    input("\n Presiona ENTER para volver a al menu. . .")

#-------------------------------------------------------------------------------------------------------------------------------------------------#

