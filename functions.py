def func(x):
    return x + 1

def square(x):
    return x*x

def turnsix(x):
    return 6

def ceiling(x,y):
    i = 0

    while( (y * i) < x):
        i = i+1

    return i

def remainder(x,y):
    
    while(x >= y):
        x=x-y

    return x
