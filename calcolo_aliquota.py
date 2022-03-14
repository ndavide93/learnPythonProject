reddito = int(input('inserisci il tuo reddito :'))
aliquota=0.0
if reddito < 10000.0 :
    aliquota = 0
elif reddito <= 20000.0:
    aliquota = reddito * 0.05
elif reddito <= 30000.0:
    aliquota = reddito * 0.1
elif reddito <= 50000.0:
    aliquota = reddito * 0.2
else :
    aliquota = reddito *0.3
print('per questo reddito ', reddito ,' , devi pagare ', aliquota, 'di aliquota')