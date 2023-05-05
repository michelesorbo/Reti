#Una lista è una collezzione di valori
alunno = "Daniele" #Variabile
alunni = ['Daniele','Salvatore', 'Gabriele', 'Salvatore'] #Lista

print(alunni.count('Salvatore'))#Conta gli elementi presneti nella lista

print(len(alunni))#len() conta gli elementi di una lista

#Leggo un elemento della lista
#Ricorda che oltra al contenuto la lista ha anche un indice che parte da 0 e si riferisce al primo contenuto della lista
print(alunni[1])

alunni[1] = "Matteo" #Modifica di un contenuto nella lista
print(alunni[1])

#Per aggiungere altri elementi nella lista uso il metodo append
alunni.append("Giulia")
print(alunni)

#Rimuovo l'utimo elemento della lista
alunni.pop()
print(alunni)

#Per stamapare tutti gli elementi della lista
# for pippo in alunni:
#     print(pippo)

# #Le liste posso contenere più tipi di valori.
# lista_mista = ['Michele', 34,[23,"Rosso"]]
# print(lista_mista[2][1])


#Esercizio data una lista numerica fare la somma di tutti gli elemnti della lista
numeri = [2,45,76,89,87,9,3]

somma = 0

for n in numeri:
    somma += n

print(f"La somma total è {somma}")

#Ordinare una lista
nomi_lista = ['Mario', 'Alberto', 'Giuseppe']
print(nomi_lista[0])#Mario
nomi_lista.sort() #Ordina la lista in modo crescente la modifica alla lista è permanente
print(nomi_lista[0])#Alberto
print(nomi_lista)

nomi_lista.sort(reverse=True) #Ordina in modo decrescente
print(nomi_lista)

#Ricerca in una lista
if 'Alberto' in nomi_lista:
    print("Presente")
else:
    print("Assente")

#Da fare
#Fare la somma dei numeri pari e dispari chiesti da tastiera, memorizzare i numeri inseriti sia pari che dispari. Non usare variabili
# per fare la somma tipo somma_p e somma_d

#2° quando inserisco un numero controllo se è già stato inserito, se è presente lo segnolo e non lo aggiungo

#Per tutti il comando per uscire è fine 
