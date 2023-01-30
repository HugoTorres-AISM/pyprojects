#Requeriments: printc.py
from printc import printc, binput, getn
printc('[37m[44m ! [0m Inserte el primer número.[0m')
n1 = binput()
printc('[37m[44m ! [0m Inserte el segundo número.[0m')
n2 = binput()
printc('[37m[44m ! [0m Inserte el tercer número.[0m')
n3 = binput()
ans = getn(n1, n2, n3)
printc('[37m[44m ! [0m El número más grande es: [0m'+ans)