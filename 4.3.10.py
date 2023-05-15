from os import strerror

report={}
try:
    #C:\Users\bad-b\Desktop\python\python work\4.3.10.txt
    percorso=input('inserisci il percorso del file da aprire : ')
    file= open(percorso, 'rt')
    line = file.readline()
    studenti_voti={}
    if line != '' :
        nome=str()
        voto=float()
        for char in line:
            if char.isalpha() or char == ' ':
                nome=nome+char
                continue
            else:
                studenti_voti[nome]=''
                voto+=float(char)
                studenti_voti[nome]=voto
                continue
        

        
        
except:
    print('non va')