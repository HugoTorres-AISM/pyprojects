from printc import *
###########################################################
def intersection(list_a, list_b):
    return [ e for e in list_a if e in list_b ]
###########################################################
printb('Inserte lo que quiera, me da igual, pero separe cada cosa con comas y un espacio, ya que si no me das cringe. (, ) - Limite de 128 elementos por fastidiar. (0/1)')
string1 = binput()
l1 = string1.split(', ', 128)

printb('Inserte lo que quiera, me da igual, pero separe cada cosa con comas y un espacio, ya que si no me das cringe. (, ) - Limite de 128 elementos por fastidiar. (1/1)')
string2 = binput()
l2 = string2.split(', ', 128)
l3 = intersection(l1, l2)
res = ",".join(str(x) for x in l3)
printb('Toma y vete: '+res)