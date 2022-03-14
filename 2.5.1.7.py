text =input('inserisci una frase palindroma: ')
text=text.replace(' ','')  #leva spazi
text=text.upper()  #all maiuscolo
listText=[]
listText[:0]=text       #converti a lista
inverseText = []        #lista check palindromo
if text == ' ':    #evita spazio 
    print('inserisci una frase')
if text == '':    #evita spazio 
    print('inserisci una frase')
else:    
    for ch in listText:                     #check caratteri
        inverseText.insert(0,ch)       #piazza il carattere all'inverso 
    if listText == inverseText:
        print('è un palindromo')
    else:
        print('ritenta')












