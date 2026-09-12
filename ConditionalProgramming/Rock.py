r = "rock"
p = "paper"
s = "scissor"
print("---------- Welcome to Rock/Paper/Scissor -----------")
choice1 = input("Player1 enter your choice :").lower()
choice2 = input("Player2 enter your choice :").lower()
if (choice1 == r or choice1 == p or choice1 == s) & (choice2 == r or choice2 == p or choice2 == s):
    if choice1 == r and choice2 == r:
        print("Its Drawww '_'")
    elif choice1 == p and choice2 == r:
        print("Player1 Wins :)")
    elif choice1 == s and choice2 == r:
        print("Player2 Wins :)")
    elif choice1 == r and choice2 == p:
        print("Player2 Wins :)")
    elif choice1 == p and choice2 == p:
        print("Its Drawww '_'")
    elif choice1 == s and choice2 == p:
        print("Player1 Wins :)")
    elif choice1 == r and choice2 == s:
        print("Player1 Wins :)")
    elif choice1 == p and choice2 == s:
        print("Player2 Wins :)")
    elif choice1 == s and choice2 == s:
        print("Its Drawww '_'")
    else:
        print("Error !!!!!")
else:
    print("Invalid Choices !!")

