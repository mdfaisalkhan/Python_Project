import random
randnumber = random.randint(1,100)
user = None
guess = 0
while(user!=randnumber):
    user = int(input("Enter the number "))
    if (user == randnumber):
        print("You guessed it right!")
    else:
        if user > randnumber:
            print("you guessed it worng! enter a smaller number")
        else:
            print("you guessed it wrong! enter the larger number")
  
    guess+=1
    

print("You guessed the number in ",guess,"guesses")
