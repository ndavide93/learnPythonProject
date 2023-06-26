import os
os.chdir('C:/Users/dnordoni/AppData/Local/Programs/Python')
#https://docs.python.org/3/library/os.path.html
def find(path,dir):
    try:
        for cartella in os.listdir(path):
            if cartella == dir:
                print(os.path.dirname(os.path.join(path,cartella,dir)))
                continue
            else:
                if os.path.isdir(os.path.join(path,cartella)):
                    find(os.path.join(path,cartella),dir)
            
    except:
        print('non trovato')
find(path="./Python310",dir="docx2txt") 