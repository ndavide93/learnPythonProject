text = input("Enter your message: ")
key= int(input('inserisci la criptazione: '))
cifrato=''
if key >= 1 and key <= 25:
    for ch in text:
        if not ch.isalpha():
            newcifrato = ch
        elif not ch.isupper(): #minuscolo
            newcifrato=(chr(ord(ch) + key ))#- ord('a'))
            if ord(newcifrato)> 122:   # se supera la z newkey deve esser la differenza tra newcifrato e 122
                newkey= ord(newcifrato) -122  
                newcifrato = chr((96)+ newkey)   #newcifrato
           
        elif ch.isupper():  #maiuscolo
            newcifrato=chr((ord(ch) + key)) #- ord('A'))
            if ord(newcifrato)> 90:
                newkey= ord(newcifrato)- 90
                newcifrato = chr((64)+ newkey)
        cifrato += newcifrato 
else:
    print('inserisci un numero tra 1 e 25')
print(cifrato)
