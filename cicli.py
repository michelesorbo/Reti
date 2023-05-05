#Cicclo FOR

somma=0

for n in range(1,11): #va da 0 a 9
    print(f"{somma} += {n}") #Stamapre a video cosa succede
    somma += n #aggiorno la varibile somma

#Quando finisco il for faccio stampare la somma
print("La somma dei primi 10 numeri è: " + str(somma))


#Tutti gli input da tastiera sono di tipo stringa quindi usare int() per fare il cast
#Chiedere la tabellina da visualizzare
tabellina = input("Quale tabellina vuoi visualizzare? ")
for n in range(1, 11):
    print(f"{tabellina} * {n} = {n * int(tabellina)}")


#Ciclo WHILE
for i in range(1, 11, 1):
    print(i)

print("\nCiclo WHILE\n")
n = 1 #condizione di inzio del WHILE nel FOR è la prima voce del RANGE
while n <= 10: #Condizione di uscita dal ciclo WHILE nel for è la seconda voce del RANGE
    print(n) #Dentro il FOR
    n += 1 #Incremento della n nel FOR è l'ultima voce del RANGE


#Scrivere un programma che facca la somma dei numeri inseriti da tastiera termina quanod inserisco 0
numero = int(input("Faccio la somma dei numeri termino con 0: ")) #Faccio il cast in int direttamente dopo l'input
somma = 0 #Variabile di appoggio per memorizzare le somme dei vari numeri inseriti

while numero != 0:
    somma += numero #(somma = somma + numero) Sommo il numero inserito con i vecchi numeri
    numero = int(input("Inserisci un nuovo numero da sommare oppure 0 per terminare: "))

print(f"La somma totale è {somma}") #print("La somma è: " + str(somma))

#Scrivere un programma che facca la somma dei numeri pari e dei numeri dispari inseriti da tastiera termina quanod inserisco 0
#Al termine dare il totale dei numeri pari e il totale dei numeri dispari

numero = int(input("Faccio la somma dei numeri termino con 0: ")) 
somma_p = 0
somma_d = 0 

while numero != 0:
    if numero%2 == 0:
        somma_p += numero
    else:
        somma_d += numero

    numero = int(input("Inserisci un nuovo numero da sommare oppure 0 per terminare: "))

print(f"La somma totale dei numeri pari è {somma_p}") #print("La somma è: " + str(somma))
print(f"La somma totale dei numeri dispari è {somma_d}")