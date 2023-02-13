from printc import *
v = 0
printb('Inserte todo lo que quiera.')
string = binput()
for x in string:
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U'):
        v = v+1
        printb('Vocal detectada ('+str(x)+')')
printb('Que si, Keroro, que si, que es/son '+str(v)+' vocal(es) y punto.')