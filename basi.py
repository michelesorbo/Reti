#Dichiarazione di variabili
nome = "Michele     " #Dichiaro una varibile e la inizializzo con il valore Michele. Questa variaibìle è di tipo stringa
eta = 43 #Dichiaro una variabile ma questa volta è di tipo Numerico
cognome = 'Sorbo' #In python la differenza tra " e ' non esiste

#Gestire le stringhe
print(nome.lower()) #Modifica la stringa in minuscolo
print(nome.upper()) #Modifica la stringa un MAIUSCOLO
print(nome.strip()) #Rimuove i caratteri vuoti

#Per vedere di che tipo è la variabile si usa il comando type()
print(type(nome))
print(type(eta))
print(type(cognome))

#Operatori numerici
#Posso fare operazioni solo con NUMERI
n1 = 4
n2 = 5
print(f"Somma: {n1 + n2}") #Somma
print(f"Sottrazione: {n1 - n2}")
print(f"Moltiplicazione: {n1 * n2}")
print(f"Divisione: {n1 / n2}")
print(f"Modulo (o resto della divisione): {n1 % n2}")


#Condizioni IF ELIF ELSE
#Una condizione serve a far esegurie un codice se la condizione è rispettata

if 4 > 3: #Maggiore stretto 
    print("Maggiore stretto")

if 3 >= 3: #Maggiore uguale
    print("Vero")

if 3 < 3:#Minore Stretto 
    print("False")

if 3 <= 3: #Minore ugule
    print("True")

if 3 == 3: #Ugugaglianza è sempre stretta
    print("3 == 3 True")

n3 = 3
if n3 == '3':
    print("True")
else:
    print("False")


#Esercizio: Dato un numero da tastiera dire se è pari o dispari
# 1) Prendo in input il numero che devo esaminare
numero = input("Inserisci un numero e ti dirò se è pari o dispari: ")
#Ricada che il numero è di tipo Stringa
#Faccio il modulo 2 del numero per vedere se ha resto. Se il resto è = a 0 è pari altrimenti è dispari
if int(float(numero))%2 == 0:
    print("Il numero è pari")
else:
    print("Il numero è dispari")