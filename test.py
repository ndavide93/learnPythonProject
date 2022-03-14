def mysplit(strng):
    lista=[]
    parola=''
    for ch in str(strng):
        if ch == parola:
            return None
        elif ch !=' ':
            parola+= ch
            
        else :
            lista.append(parola)
            parola=' '
    lista.append(parola)
    return lista
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" ab c "))
print(mysplit(""))