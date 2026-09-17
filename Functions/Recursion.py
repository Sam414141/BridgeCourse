def num(n):
    if n < 0:
        return n
    print(n)
    num(n-1)
    
num(10)