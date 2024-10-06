def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    if y == 0:
        return float('inf') if x >= 0 else float('-inf')
    return x/y