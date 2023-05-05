numeri = [3,6,7,12,34,56,8]
numeri2 = [2,65,45,7,8,90]

# for n in numeri:
#     print(n)

#Una funzione è una ripetizione del codice richiamato all'occorrenza

#Definire una funzione senza parametri
#def nome_funzione():
def saluta():
    print("Ciao dalla funzione")

#Una funzione deve essere invocata
saluta()
saluta()
saluta()
saluta()

#Funzione con parametri
def salutaNome(nome):
    print(f"Ciao da {nome}")

salutaNome("Daniele")
salutaNome("Vincenzo")

n = "Michele"
salutaNome(n)

def somma(n1, n2):
    print(f"La somma è : {n1 + n2}")


somma(2,5)
somma(7,8)


#Funzioni con ritorno può essere usata per assegnare un valore ad una variabile oppure inserita in un print()
def cubo(n):
    return n*n*n

cb = cubo(3) #Assegno il ritorno della funzione cubo a cb

print(cb)
print(cubo(9))


def stampaLista(lista):
    for item in lista:
        print(item)

nomi = [3,9,'Antonio','Mario','Francesco']

stampaLista(numeri)
stampaLista(numeri2)
stampaLista(nomi)

# Scrivi una semplice funzione che, data una lista di numeri, fornisca in output un istogramma basato su questi numeri, 
# usando asterischi per disegnarlo.
# Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:
# ***
# *******
# *********
# *****

#Soluzione
def istogramma(lista):
    #Controllare se gli elemnti sono numerici se non lo sono andare avanti
    for l in lista:
        print(type(l))
        print("*" * l)

l1 = [3,7,9,5]

istogramma(l1)
istogramma(nomi)
istogramma([4,7,9])