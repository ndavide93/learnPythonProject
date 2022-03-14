line1=295743861  # list(input('inserisci 9 cifre'))
line2=431865927
line3=876192543
line4=387459216
line5=612387495
line6=549216738
line7=763524189
line8=928671354
line9=154938672

def ctrlRow(line):
    for ch in line.sort():
        if ch.isnum() in range(1,10):
            return True
        else:
            print('reinserisci solo numeri')

for 