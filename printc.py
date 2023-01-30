def printc (str ):#line:1
    import os #line:2
    os .system ('echo '+str )#line:3
def binput ():#line:4
    O000O0OOOOOOO000O =input ('> ')#line:5
    return O000O0OOOOOOO000O #line:6
def getn (n1 ,n2 ,n3 ):#line:7
    if (n1 >n2 and n1 >n3 ):#line:8
        return n1 #line:9
    else :#line:10
        if (n2 >n3 ):#line:11
            return n2 #line:12
        else :#line:13
            if (n1 <n3 ):#line:14
                return n3 #line:15
            else :#line:16
                return n1 