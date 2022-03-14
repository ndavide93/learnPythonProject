text =input('inserisci una frase : ')
text2=input('inserisci una frase per verificare che sia un anagramma:')
text=text.replace(' ','')  #leva spazi
text=text.upper()  #all maiuscolo
text2=text2.replace(' ','')  #leva spazi
text2=text2.upper()  #all maiuscolo
listText=[]
listText[:0]=text       #converti a lista
listText2=[]
listText2[:0]=text2 
listText.sort()
listText2.sort()
if listText == listText2:
    print('congratulations')
else:
    print('ritenta')


