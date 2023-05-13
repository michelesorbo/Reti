x = 15 #Questa x #Variabile globale visible in tutto il foglio python

def stampa():
    x = 2 #non è questa #Variabile di funzione ed è visibile solo nella funzione
    return x

print(stampa())

#Per usare una variabile globale nella funzione devo usare global

def stampa2():
    global x
    x += 2
    return x

print(stampa2())

print(x)