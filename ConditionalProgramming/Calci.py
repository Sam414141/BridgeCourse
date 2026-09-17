while True:
    print("---------Calculater----------")
    print("Choice List")
    print("Press 1 for Addition")
    print("Press 2 for Substraction ")
    print("Press 3 for Multiplication ")
    print("Press 4 for Division ")
    print("Press 5 for Factorial ")
    choice = int(input("Enter Your Choice :"))
    if 5 >= choice & choice >= 1:
        if choice == 5:
            num1 = int(input("Enter a number :"))
        else:
            num1 = int(input("Enter first number :"))
            num2 = int(input("Enter second number :"))
        match choice:
            case 1: print(f"Addition = {num1 + num2}")
            case 2: print(f"Substraction = {num1 - num2}")
            case 3: print(f"Multiplication = {num1 * num2}")
            case 4: 
                if num2 == 0:
                    print("Second Number is 0 Division Operation Failed")
                else:
                    print(f"Division = {num1 / num2}")
            case 5: 
                fact = 1
                for i in range(1,num1+1):
                    fact *= i
                    num1 += 1
                print(f"Factorial = {fact}")
                    
    else:
        print("Invalid Choice !!!!")

    val = int(input("Enter 0 for Continue and 1 for Exit "))
    if val == 0:
        next
    elif val == 1:
        print("Exiting Now ")
        break
    else:
        print("Invalid Choice Exiting Anyway ")
        break
    