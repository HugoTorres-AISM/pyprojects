from printc import printc, binput, printb, clear
clear()
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
    clear()
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
avrg1=0
for i in arr:
    avrg1 = avrg1+int(i)
avrg1 = avrg1/len(arr)
clear()
printb('La media de esos numericos es: '+str(avrg1))