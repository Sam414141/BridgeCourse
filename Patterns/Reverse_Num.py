num = int(input("Enter Number :"))
num2 = 0
while True:
    if num % 10 != 0 or num >0:
        num2 = num2 * 10 + (num%10)
        num = num // 10
    else:
        break
print(num2)