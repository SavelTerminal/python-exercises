saldo = 500
tentativi = 3
password = "bancomat2025"
scelta = ""


nome_utente = input("Ciao, inserisci il tuo nome utente:")
print("Benvenuto " + nome_utente + ", inserisci la password, hai solo 3 tentativi!")

while tentativi > 0:
    risposta = input("Inserisci la password corretta:")

    if risposta != password :
        print("Password errata, tentativi rimasti:" + str(tentativi))
        tentativi = tentativi -1
    else:
        print("Password corretta, il tuo saldo è: " + str(saldo) + "€")
        break

if tentativi > 0 :
    while True:
       print("Cosa vuoi fare?")
       print ("1 - Preleva")
       print("2 - Deposita")
       print("3 - Esci")
       scelta = int(input("Scegli:"))
       
       if scelta == 1 :
            prelievo = int(input("Quanto vuoi prelevare?"))
            saldo = saldo - prelievo 
            print("il tuo nuovo saldo è: " + str(saldo) + "€")
    
       elif scelta == 2 :
            deposito = int(input("Quanto vuoi depositare?"))
            saldo = deposito + saldo 
            print("Il tuo nuovo saldo è: " + str(saldo) + "€")

       elif scelta == 3 :
            print("Grazie e arrivederci")
            break
    
       else:
            print("Digita solo 1, 2 o 3. Riprova")