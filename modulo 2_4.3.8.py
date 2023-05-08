from os import strerror

istogramma={}
try:
    #C:\Users\bad-b\Desktop\python\python work\file.txt
    percorso=input('inserisci il percorso del file da aprire : ')
    file= open(percorso, 'rt')
    line = file.readline()
    if line != '' :
        for char in line:
            if char not in istogramma and char.isalpha():
                char=char.lower()
                istogramma[char]= '1'
            elif char.isalpha():
                char=char.lower()
                istogramma[char]=str(int(istogramma[char])+1)
            else:
                continue
        for char in sorted(istogramma):
            newstream=open(percorso +'.hist','at')
            newstream.writelines('\n'+ char + '->' +istogramma[char])
            

except:
    print('non va')
 