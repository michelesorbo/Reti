#per gestire gli errori si usa try except

#Creo una funzione per sommare 2 numeri

def somma():
    try: #Proviamo a fare la somma
        n1 = int(input("Inserisci il primo numero da sommare: "))
        n2 = int(input("Inserisci il secondo numero da sommare: "))

        print(f"La somma è: {n1 + n2}")
    except ValueError: #Altrimenti gestisci l'errore
        print("Puoi usare solo numeri... non fare il furbo")

def sommaContinua():
    somma = 0
    n = 0
    try:
        n = int(input("Inserisci un numero da sommare 0 per terminare: "))
    except ValueError:
        print("Puoi usare solo numeri... non fare il furbo")


    while n != 0:
        try:
            somma += n
            n = int(input("Inserisci un numero da sommare 0 per terminare: "))
        except ValueError:
            print("Puoi usare solo numeri... non fare il furbo")
    
    print(f"La somma dei numeri è: {somma}")



sommaContinua()