from printc import *
clear()
limit = "null"
while True:
    try:
        printb('Inserte un numerito')
        limit = binput()
    except ValueError as e:
        printb('ERR: No se que lees, pero vamos, que tiene que ser un numero.')
        clear()
        exit()
    diglimit = int(limit)
    if isinstance(diglimit, int) == True: break
clear()
numb = 0
while numb < diglimit:
    numblast = numb
    printb('Numero: '+str(numb))
    numb = 2*numb+1
while numb > diglimit:
    if numb > diglimit:
        numb = numblast
        printb('Operación revertida.')
    else:
        printb('Operación finalizada.')
        break
numb = int(numb)
clear()
printb('El número es: ' + str(numb))