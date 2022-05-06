import random

palabras = ["nadar", "odiar", "poner", "salir", "queso", "sabio", "robar", "tirar", "tener" "padre", "madre", "coche", "jugar",
"sudar", "amiga", "amigo", "asado", "comer", "dudar", "estar", "firma", "feria", "gafas", "haber", "joder", "lamer", "metro",
"mirar", "tonta", "tonto",  "adios"]
acierto = 0

def escribir(palabraElegida):
    return input("Escribe tu palabra de 5 letras: ")

def elegirPalabra(palabras):
    numeroRandom = random.randint(0, len(palabras))
    return palabras[numeroRandom]
    
def comprobar(palabraEscrita, palabraElegida):
    acierto = 0
    for i in range(len(palabraElegida)):
        esta = False;
        if (palabraElegida[i] == palabraEscrita[i]):
            esta = True
            acierto += 1
            print("Letra", palabraEscrita[i], "en la posicion", i + 1, "esta perfecta")
        if (esta == False):
            for j in range(len(palabraElegida)):
                if (palabraEscrita[i] == palabraElegida[j]):
                    esta = True
                    print("Letra", palabraEscrita[i], "en la posicion", i + 1, "esta mal puesta")
        if (esta == False):
            print("Letra", palabraEscrita[i], "en la posicion", i + 1, "no esta")
    return(acierto)

palabraElegida = elegirPalabra(palabras)
while acierto != len(palabraElegida):
    palabraEscrita = escribir(palabraElegida)
    acierto = comprobar(palabraEscrita, palabraElegida)

print("************************************************************************************")
print("Has ganado")    


