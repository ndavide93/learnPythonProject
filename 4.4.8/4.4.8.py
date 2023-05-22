import os
class Cercacartelle:
    def find(self,path,dir):
        try:
            os.chdir(path)
            print('cartella trovata')
        except:
            print('cartella non trovata , riprova')
        for percorso in os.listdir(path):
            while dir in os.listdir(percorso):
                print(os.listdir(percorso))
                continue
            else:
                os.chdir('path\percorso')
                print(os.listdir())

ciao = Cercacartelle()
ciao.find('./tree', 'python')