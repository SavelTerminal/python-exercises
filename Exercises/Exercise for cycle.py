pin = 2468
somma = 0

while True:
    risposta = int(input("Inserisci il pin corretto"))
    
    if risposta != pin:
        print ("Pin incorretto, riprova.")
    
    else:
        print("Pin corretto!")
        break

for i in range(5):
    numero = int(input("Inserisci un numero qualsiasi, 5 volte:"))

    if numero > 10 and numero < 100:
        somma += numero
    
    elif numero < 0:
        print("Input interrotto, Somma parziale:" + str(somma))
        break

    else:
        pass

else:
    print("La somma finale è: " + str(somma))