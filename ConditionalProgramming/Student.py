score = int(input("Enter your Marks :"))
if score > 90 and score <=100:
    print("You got O grade")
elif score > 80 and score <=90:
    print("You got A grade")
elif score > 65 and score <=80:
    print("You got B grade")
elif score >= 35 and score <=65:
    print("You got C grade")
elif score >=0 and score < 35:
    print("You got F grade")
else:
    print("Invalid Marks !!!")
    