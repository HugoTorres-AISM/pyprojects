import os, time, random
os.system('cls')
global p
pause = 'pause > NUL'
bline = 'echo.'
p = 0

def checkansw(var):
    if (var == 'a'):
        return True
    elif (var == 'b'):
        return True
    elif (var == 'c'):
        return True

def validansw(var):
    while True:
        if checkansw(var):
            return var
            break
        else:
            os.system(bline)
            os.system('echo [37m[41m ! [0m ¡Solo puedes usar a, b, c![0m')
            os.system(bline)
            var = input('> ')
            
def corr(v):
    if (v == True):
            global p
            os.system(bline)
            os.system('echo [37m[44m ! [0m Respuesta correcta, presiona cualquier tecla para continuar.[0m')
            os.system(bline)
            p = p+3
            os.system(pause)
    else: 
            os.system(bline)
            os.system('echo [37m[41m ! [0m Respuesta incorrecta, presiona cualquier tecla para continuar.[0m')
            os.system(bline)
            os.system(pause)

os.system('@echo off')
os.system(bline)
os.system('echo [37m[44m ! [0m Bienvenido al juego, ¿Cúal es tu nombre?[0m')
os.system(bline)
name = input('> ')
os.system(bline)
os.system('echo [37m[44m ! [0m ¡Maravilloso, ' + name.title() + ', presiona cualquier tecla para iniciar![0m')
os.system(bline)
os.system(pause)
#Inicio preg
os.system('cls')
os.system(bline)
os.system('echo [37m[44m ! [0m ¿Como harías un echo en blanco (Batch)?[0m')
os.system(bline)
os.system('echo [37m[43m a [0m echo.[0m')
os.system("echo [37m[43m b [0m echo ' ' [0m")
os.system("echo [37m[43m c [0m echo' '[0m")
os.system(bline)
r1 = validansw(input('> '))
if (r1 == 'a'):
    corr(True)
else:
    corr(False)
#Inicio preg
os.system('cls')
os.system(bline)
os.system('echo [37m[44m ! [0m ¿Cómo importarías módulos en Python?[0m')
os.system(bline)
os.system('echo [37m[43m a [0m getmodules A, B[0m')
os.system("echo [37m[43m b [0m from X import *[0m")
os.system("echo [37m[43m c [0m import A, B[0m")
os.system(bline)
r2 = validansw(input('> '))
if (r2 == 'c' or r2 == 'b'):
    corr(True)
else:
    corr(False)
#Inicio preg
os.system('cls')
os.system(bline)
os.system('echo [37m[44m ! [0m ¿Qué es PyPI?[0m')
os.system(bline)
os.system('echo [37m[43m a [0m Pylance Program Indexer[0m')
os.system("echo [37m[43m b [0m Python Program Indexer[0m")
os.system("echo [37m[43m c [0m Python Package Manager[0m")
os.system(bline)
r3 = validansw(input('> '))
if (r3 == 'c'):
    corr(True)
else:
    corr(False)
#Inicio preg
os.system('cls')
os.system(bline)
os.system('echo [37m[44m ! [0m ¿Cuál de estas herramientas se usan para obtener datos de un usuario?[0m')
os.system(bline)
os.system('echo [37m[43m a [0m holehe[0m')
os.system("echo [37m[43m b [0m sherlick[0m")
os.system("echo [37m[43m c [0m shorlok[0m")
os.system(bline)
r4 = validansw(input('> '))
if (r4 == 'a'):
    corr(True)
else:
    corr(False)
#Inicio preg
os.system('cls')
os.system(bline)
os.system('echo [37m[44m ! [0m ¿Cuál de estos es el editor de código más rápido?[0m')
os.system(bline)
os.system('echo [37m[43m a [0m Notepad[0m')
os.system("echo [37m[43m b [0m Sublime Text[0m")
os.system("echo [37m[43m c [0m Visual Studio Code[0m")
os.system(bline)
r5 = validansw(input('> '))
if (r5 == 'b'):
    corr(True)
else:
    corr(False)
os.system('cls')
if p<10:
    os.system('echo [37m[44m                                         [0m[0m[37m[44m [0m[0m')
    os.system('echo [37m[44m [0m                                        [0m[37m[44m [0m[0m')
    os.system('echo [37m[44m [0m         Has obtenido '+str(p)+' puntos.        [0m [37m[44m [0m[0m')
    os.system('echo [37m[44m [0m                                        [0m[37m[44m [0m[0m')
    os.system('echo [37m[44m                                         [0m[0m[37m[44m [0m[0m')
else:
    os.system('echo [37m[44m                                         [0m[0m[37m[44m [0m[0m')
    os.system('echo [37m[44m [0m                                        [0m[37m[44m [0m[0m')
    os.system('echo [37m[44m [0m         Has obtenido '+str(p)+' puntos.       [0m [37m[44m [0m[0m')
    os.system('echo [37m[44m [0m                                        [0m[37m[44m [0m[0m')
    os.system('echo [37m[44m                                         [0m[0m[37m[44m [0m[0m')