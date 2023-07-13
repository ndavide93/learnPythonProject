import os
import textract
#https://stackabuse.com/reading-and-writing-ms-word-files-in-python-via-python-docx-module/
#https://textract.readthedocs.io/en/stable/installation.html

import os
os.chdir('C:/Users/bad-b/Desktop/python/python_work/4.4.8')
#https://docs.python.org/3/library/os.path.html
def find(path,parola):
    try:
        for cartella in os.listdir(path):
            if os.path.isfile(cartella):
                text=textract.process(os.path.join(path,cartella))
                for a in text:
                    if a ==parola:
                        print(os.path.join(path,cartella))
                continue
            else:
                if os.path.isdir(os.path.join(path,cartella)):
                    find(os.path.join(path,cartella),dir)
    except:
        print('non trovato')

find(path=os.chdir(str(input('inserisci il percorso in cui cercare'))),parola=(str(input('che cosa stai cercando?'))))