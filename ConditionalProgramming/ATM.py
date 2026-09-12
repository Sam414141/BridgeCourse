available_balance = 0
while True:
    print("---------ATM----------")
    print("Choice List")
    print("Press 1 for Check Balance")
    print("Press 2 for Deposite")
    print("Press 3 for Withdraw ")
    print("Press 4 for Exit")
    choice = int(input("Enter Your Choice :"))
    if 4 >= choice & choice >= 1:
        match choice:
            case 1: 
                print(f"Available Balance : {available_balance}")
            case 2: 
                temp = int(input("Enter Amount to Deposite :"))
                available_balance += temp
                print("Amount Deposited Successfully...")
                print(f"Available Balance : {available_balance}")
                print("Thank You ^_^")
            case 3: 
                temp = int(input("Enter Amount to Withdraw :"))
                available_balance -= temp
                print("Amount Withdrawal Successfully...")
                print(f"Available Balance : {available_balance}")
                print("Thank You ^_^")
            case 4:
                break 
    else:
        print("Invalid Choice !!!!")
        next
    