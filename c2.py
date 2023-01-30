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
###########################################
while True:
    printc('[37m[44m ! [0m Inserte otro número. (Use: cancel para finalizar.)[0m')
    numb = binput()