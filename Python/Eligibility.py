role = input("Enter your role :").lower()
age = int(input("Enter your age :"))
print(f"Eligible : {"student" == role and age < 21} ")
