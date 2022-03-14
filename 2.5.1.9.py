compleanno=input('inserisci il tuo compleanno in qualsiasi formato')
lista=[]
somma=0
for ch in compleanno:
    lista.append(ch)
for ch in lista:
    ch=int(ch)
    somma = somma + ch

print(lista)
print(somma)