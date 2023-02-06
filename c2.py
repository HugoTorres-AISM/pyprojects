#Requeriments: printc.py
from printc import printc, binput
printc('[37m[44m ! [0m Inserte el primer número.[0m')
arrn1 = binput()
arr = []
arr.append(arrn1)
###########################################
#             Array + Printc              #
###########################################
def addn(num):
    global arr
    arr.append(num)
def sum(arr):
    sum = 0
    for i in arr:
        iint = int(i)
        sum = sum + iint
    return(sum)
###########################################
while True:
    printc('[37m[44m ! [0m Inserte otro número. (Use: cancel para finalizar.)[0m')
    numb = binput()
    if (numb == 'cancel'):
        break
    else:
        integ = 'true'
        try:
            xcf = int(numb)
        except:
            printc('[37m[44m ! [0m No mijo, esto no. [0m')
            integ = 'false'
        if (integ != 'false'):  
            addn(numb)
        
arrn = ",".join(str(x) for x in arr)
printc('[37m[44m ! [0m Array: [0m' + arrn)
printc('[37m[44m ! [0m Resultado (Aprende a sumar): [0m' + str(sum(arr)))