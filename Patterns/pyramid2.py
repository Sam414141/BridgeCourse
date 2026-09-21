n = int(input("Enter Number of rows"))
for i in range(1,5):
    for j in range(1,n-i+1):
        print(" ",end="")
    
    for i in range(1,i*2):
        print("*",end="")
        
    print()