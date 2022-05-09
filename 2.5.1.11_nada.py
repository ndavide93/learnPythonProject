contatore= 1
def ctrllen(linelist):    #verifica se lunghezza  = 9 numeri
    if len(linelist) != 9:
        print('inserisci 9 cifre')
        return False
    else:
        return True
def ctrlseq(linelist):   #verifica se numeri da 1  a 9
    linelist.sort()
    contat = 0
    for n in linelist:
        contat += 1
        if n in linelist == contat:    
            print( n + ' era già stato inserito')        
            break
        
        

for i in range(9):
    line=input('inserisci 9 cifre fino per riempire la linea '+ str(contatore) + ' grazie : ')
    linelist=[]
    linelist[:0] = line
    ctrllen(linelist)
    contatore += 1
    if True:
        ctrlseq(linelist)
    
     

