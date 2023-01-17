#Import basics
import time, os

#Ask for the vars
n1 = input("> Insert the first number [0-9] | ")
s1 = input("> Insert the first operators [+, -, *, /] | ")
n2 = input("> Insert the second number [0-9] | ")
r1=""

#Check vars
while True:
    if str.isdigit(n1):
        print('> Number 1 is valid.')
        break
    else:
        print('> Number 1 is not an usable digit.')
        n1 = input("> Insert the first number [0-9] | ")

while True:
    if s1 == '+':
        print('Operator 1 is valid.')
        break
    elif s1 == '-':
        print('Operator 1 is valid.')
        break
    elif s1 == '*':
        print('Operator 1 is valid.')
        break
    elif s1 == '^':
        print('Operator 1 is valid.')
        break
    elif s1 == '/':
        print('Operator 1 is valid.')
        break
    else:
        print('> Operator 1 is not an usable digit.')
        s1 = input("> Insert the first operators [+, -, *, /] | ")

while True:
    if str.isdigit(n2):
        print('Number 2 is valid.')
        break
    else:
        print('> Number 2 is not an usable digit.')
        n2 = input("> Insert the second number [0-9] | ")

#Make resp

if s1 == "+":
    r1 = int(n1)+int(n2)
    print(' ')
if s1 == '-':
    r1 = int(n1)-int(n2)
    print(' ')
if s1 == '*':
    r1 = int(n1)*int(n2)
    print(' ')
if s1 == '^':
    r1 = int(n1)^int(n2)
    print(' ')
if s1 == '/':
    r1 = int(n1)/int(n2)
    print(' ')
print(str(n1) + str(s1) + str(n1) + ' = ' + str(r1))
print("Hola",34)
