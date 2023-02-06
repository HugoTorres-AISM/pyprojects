from printc import printc, binput
printc('[37m[44m ! [0m Inserte algo interesante. (1/2)[0m')
str1 = binput()
printc('[37m[44m ! [0m Inserte algo interesante. (2/2)[0m')
str2 = binput()
lstr1 = len(str1)
lstr2 = len(str2)
if (lstr1 > lstr2):
    printc('[37m[44m ! [0m Me aburres: [0m'+str1)
else:
    if (lstr1 == lstr2):
        printc('[37m[44m ! [0m Me aburres, son las dos igualitas.[0m')
    else:
        printc('[37m[44m ! [0m Me aburres: [0m'+str2)