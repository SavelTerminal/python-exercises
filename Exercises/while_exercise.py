domanda1 = "Quanto fa 3 x 3?"
domanda2 = "Quanto fa 10 x 5?"
domanda3 = "Quanto fa 5 x 5?"
risposte = [9, 50, 25]
domande = [domanda1, domanda2, domanda3]


print("Benvenuto nel quiz matematico, come ti chiami?")
nome = input()
print("Benvenuto " + nome + "! Che il quiz abbia inizio")

for i in range(3):
    tentativi = 3
    while tentativi > 0:
        print(domande[i])
        risposta_corretta = risposte[i]
        risposta_utente = int(input())
        if risposta_utente == risposta_corretta:
            print("Risposta corretta! Andiamo con la prossima.")
            break
        else:
            print("Risposta Errata, riprova")
            tentativi -= 1
