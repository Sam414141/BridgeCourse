#print("Enter a Range to get the even numbers :")
start = int(input("Enter Starting Point :"))
counter = 0
while start<120:
    if start % 2==0:
        counter += 1
        start += 2
    else:
        start += 1
print(counter)