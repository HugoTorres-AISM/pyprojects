try:
    # Import unsecessary things
    import os, time 
    # Entire price:
    ep=0
    try:
         ep=float(input('> Input the entire price of the item. | '))
    except ValueError as e:
        print('> Unexcepted error:', e, ' - Press any key to continue.')
        os.system('pause > NUL')
        while True:
            if (float(ep)):
                break
            else:
                ep=input('> Input the entire price of the item. | ')
    #discount
    dc=0
    try:
        dc=float(input('> Input the discount to apply the item. (Without the %) | '))
    except ValueError as e:
        print('> Unexcepted error:', e, ' - Press any key to continue.')
        os.system('pause > NUL')
        while True:
            if (float(dc)):
                break
            else:
                ep=input('> Input the discount to apply the item. (Without the %) | ')
except ValueError as e:
    print('> Unexcepted error:', e, ' - Press any key to close.')
    os.system('pause > NUL')
#solution
try:
    r = ep*dc/100
    print('The ', dc, "%" , ' of ', ep, ' is ', r)
    print(' ')
    print('Final price: ', ep-r)
    os.system('pause > NUL')
except ValueError as e:
    print('> Unexcepted error:', e, ' - Press any key to close.')
    os.system('pause > NUL')