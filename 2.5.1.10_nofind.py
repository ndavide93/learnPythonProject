daTrovar=input('inserisci la parola da trovar :').lower()
daAnalizzar=input('inserisci un insieme di lettere da verificare : ').lower()
listdaTrov=[]
listdaTrov[:0]=daTrovar   #converti in lista
listadaAnaliz=[]
listadaAnaliz[:0]=daAnalizzar
counter=int()
for ch in daTrovar:
    if ch in listadaAnaliz:
       counter = counter + 1 
    else:
        counter = counter
if counter is len(daTrovar):
    print('yes')
else:
    print('no')

