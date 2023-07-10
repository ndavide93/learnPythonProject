import docx2txt
from datetime import datetime
import os
timestamp=datetime.now()

def find(percorso,nomefile):
    try:
        for cartella in os.listdir(percorso):
            if cartella == dir:
                print(os.path.dirname(os.path.join(percorso,cartella,dir)))
                continue
            else:
                if os.path.isdir(os.path.join(percorso,cartella)):
                    find(os.path.join(percorso,cartella),dir)
            
    except:
        print('non trovato')
#creazione variabile path per directory da analizzare
path=input('Inserisci il percorso da analizzare :  ')
realpath=path.replace(os.sep,'/')
path=realpath
print(path)

#leggi doc
text=docx2txt.process("HARDWARE - POS_INGENICO - HOW TO_v.2 - 20190718.docx")
repository= open('repository.txt','w')
repository.write(text)
repository.close()


os.chdir('C:/Users/bad-b/Desktop/python/python_work/4.4.8')
#https://docs.python.org/3/library/os.path.html
 