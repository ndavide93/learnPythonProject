from os import strerror

report={}
try:
    #C:\Users\bad-b\Desktop\python\python work\4.3.10.txt
    percorso=input('inserisci il percorso del file da aprire : ')
    file= open(percorso, 'rt')
    line = file.readline()
    if line != '' :
        
        
            

except:
    print('non va')