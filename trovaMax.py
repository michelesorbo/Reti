#Scrivere una funzione(Algoritmo) che dati 3 numeri in ingressi mi ritornerà il numero maggio
#es: trovaMAX(5,4,8) => 8; trovaMAX(6,4,3) => 6

def trovaMAX(n1,n2,n3):
    if n1 > n2:
        if n1 > n3:
            print(f"Il maggiore è: {n1}")
        else:
            print(f"Il maggiore è: {n3}")
    else:
        if n2 > n3:
            print(f"Il maggiore è: {n2}")
        else:
            print(f"Il maggiore è: {n3}")

trovaMAX(2,9,7)
trovaMAX(5,2,4)
trovaMAX(4,7,9)

#AND tutte le condizioni devono essere vere (rispettate)
#OR almeno una condizione deve essere vera (rispettata)

def trovaMIN(n1,n2,n3):
    if n1 < n2 and n1 < n3:
         print(f"Il minore è: {n1}")
    elif n2 < n1 and n2 < n3:
        print(f"Il minore è: {n2}")
    else:
        print(f"Il minore è: {n3}")

trovaMIN(2,9,7)
trovaMIN(5,2,4)
trovaMIN(4,7,9)