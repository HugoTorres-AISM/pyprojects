from printc import *
clear()
printb('Inserte un numerito')
x1 = binput()
while True:
    if (str.isdigit(x1)):
        if ('-' in x1):
            clear()
            printb('No me toques los integrales, vuelve otra vez.')
            x1 = binput()  
        else:
            if (x1 == 0):
                clear()
                printb('No me toques los integrales, vuelve otra vez.')
                x1 = binput()  
            else:
                break
    else:
        clear()
        printb('No me toques los integrales, vuelve otra vez.')
        x1 = binput()
clear()
rest1 = 1
rest2 = 1
res = 1
while (int(rest2) <= int(x1)):
    res = rest1*res
    rest1 = rest1+1
    rest2 = rest2+1
    printb('Estado: '+str(rest1-1)+'/'+str(x1))
printb('No se para que sirve, pero toma: '+str(res))