import os, time, random

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
            os.system(bline)
            os.system('echo [37m[44m ! [0m Respuesta correcta[0m')
            os.system(bline)
            p = +3
    else: 
            os.system(bline)
            os.system('echo [37m[41m ! [0m Respuesta incorrecta.[0m')
            os.system(bline)

os.system('@echo off')
os.system(bline)
os.system('echo [37m[44m ! [0m Bienvenido al juego, ¿Cúal es tu nombre?[0m')
os.system(bline)
name = input('> ')
os.system(bline)
os.system('echo [37m[44m ! [0m ¡Maravilloso, presiona cualquier tecla para iniciar![0m')
os.system(bline)
os.system('pause > NUL')
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
os.system('echo [37m[44m ! [0m ¿Como harías un echo en blanco (Batch)?[0m')
os.system(bline)
os.system('echo [37m[43m a [0m echo.[0m')
os.system("echo [37m[43m b [0m echo ' ' [0m")
os.system("echo [37m[43m c [0m echo' '[0m")
os.system(bline)
r2 = validansw(input('> '))
if (r2 == 'a'):
    corr(True)
else:
    corr(False)
#Inicio preg
os.system('cls')
os.system(bline)
os.system('echo [37m[44m ! [0m ¿Como harías un echo en blanco (Batch)?[0m')
os.system(bline)
os.system('echo [37m[43m a [0m echo.[0m')
os.system("echo [37m[43m b [0m echo ' ' [0m")
os.system("echo [37m[43m c [0m echo' '[0m")
os.system(bline)
r3 = validansw(input('> '))
if (r3 == 'a'):
    corr(True)
else:
    corr(False)
#Inicio preg
os.system('cls')
os.system(bline)
os.system('echo [37m[44m ! [0m ¿Como harías un echo en blanco (Batch)?[0m')
os.system(bline)
os.system('echo [37m[43m a [0m echo.[0m')
os.system("echo [37m[43m b [0m echo ' ' [0m")
os.system("echo [37m[43m c [0m echo' '[0m")
os.system(bline)
r4 = validansw(input('> '))
if (r4 == 'a'):
    corr(True)
else:
    corr(False)
#Inicio preg
os.system('cls')
os.system(bline)
os.system('echo [37m[44m ! [0m ¿Como harías un echo en blanco (Batch)?[0m')
os.system(bline)
os.system('echo [37m[43m a [0m echo.[0m')
os.system("echo [37m[43m b [0m echo ' ' [0m")
os.system("echo [37m[43m c [0m echo' '[0m")
os.system(bline)
r5 = validansw(input('> '))
if (r5 == 'a'):
    corr(True)
else:
    corr(False)