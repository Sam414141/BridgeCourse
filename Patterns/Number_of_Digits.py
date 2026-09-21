num = int(input("Enter Number :"))
counter = 0
while num>=0:
    if num % 10 != 0 or num >0:
        counter += 1
        num = num // 10
    else:
        break
print(counter)