from operator import truediv


line1=295743861  # list(input('inserisci 9 cifre'))
line2=431865927
line3=876192543
line4=387459216
line5=612387495
line6=549216738
line7=763524189
line8=928671354
line9=154938672
line=[]
for r in range(9):
    line=input("inserisci 9 numeri da 1 a 9 per la linea " + str(r+1) + ' : ')
    if len(line) == 9 and line.isdigit() :
        True
    else:
        print('riprova')
        break
def ctrl(linea):
    if linea.sort