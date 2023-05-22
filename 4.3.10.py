from os import strerror



report={}
try:
    #C:\Users\bad-b\Desktop\python\python work\4.3.10.txt
    percorso=input('inserisci il percorso del file da aprire : ')
    file= open(percorso, 'rt')
    leggilinee=file.readlines()
   
    for colonne in leggilinee:
        colonne=leggilinee.split()
        studenti=colonne[0] + ' ' + colonne[1]
        voto= colonne[2]



except:
    print('sheeet')