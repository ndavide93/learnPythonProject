
from os import strerror

istogramma={}
try:
    stream= open('file.txt', 'rt')
    line = stream.readline()
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
            print(char+'->'+istogramma[char])
except:
    print('non va')