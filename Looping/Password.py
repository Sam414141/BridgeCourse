correct_Password = "passwordx"
cheker = True
while cheker:
    entered_Password = input("Enter password to Exit:")
    if entered_Password == correct_Password:
        print("Password Matched <:-:-:-:---")
        cheker = False
    else:
        cheker = True

