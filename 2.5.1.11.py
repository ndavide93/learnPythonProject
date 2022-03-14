line1=295743861  # list(input('inserisci 9 cifre'))
line2=431865927
line3=876192543
line4=387459216
line5=612387495
line6=549216738
line7=763524189
line8=928671354
line9=154938672

counter=1
def ctrl(line):   #per controllare i valori
    for ch in line[]:
        if ch in range(1,10):
            ch += counter
        else:
            print('non hai inseriti 9 cifre')
for r in range (9):
    ctrl(line)