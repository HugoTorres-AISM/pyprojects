def printc(str):#line:1
    import os #line:2
    os.system("echo.")
    os.system ('echo '+str )#line:3
    os.system("echo.")
def printb(str):#line:1
    import os #line:2
    os.system('echo.')
    os.system ('echo [37m[44m ! [0m '+str+'[0m' )#line:3
    os.system('echo.')
def binput():#line:4
    str = input ('> ')#line:5
    return str #line:6
def getn(n1 ,n2 ,n3 ):#line:7
    from printc import printc
    try:
        if (n1 > n2 and n1 > n3):
            return n1
        else:
            if (n2 > n3):
                return n2
            else:
                return n3
    except ValueError as e:
        printc('[37m[41m ! [0m Hubo un error inesperado y el número no puedo ser obtenido. | [0m',e)
        return -1
def intersection(list_a, list_b):
    return [ e for e in list_a if e in list_b ]
def pause():
    import os
    os.system('pause > NUL')