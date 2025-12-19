import random

play_game = input("Do you want to play game? (YES/No) : ")

while play_game == "yes":
    print("Choose Difficulty level")
    print("Level 1 -> Easy ")
    print("Level 2 -> Medium ")
    print("Level 3 -> Insane ")
    
    level = int(input("Enter The Level : "))

    if level == 1 :
        secret_number = random.randint(1,10)
    elif level == 2 :
        secret_number = random.randint(1,100)
    elif level == 3 : 
        secret_number = random.randint(1,10000000000000000000000)

    attempts = 0
  
    while True:     
    
        guess = int(input("Guess the number: "))
        attempts = attempts + 1
    
        if guess == secret_number :
            print("Your Guess is right 🎉 "+""+ "The Secret Key is",secret_number)
            print ("Total Attempts ",attempts)
            break

        elif guess > secret_number :
            if guess - secret_number <=2 :
                print("Very Close!")
            else :
                print("Your guess number is high")
    
        elif guess < secret_number :
            if secret_number - guess <=2 :
                print("Very Close!")
            else :
                print("Your guess number is low")
    
        if attempts >=5 :
            print("😢 You Lose!")
            print("Secret number is : ",secret_number)
            break
    
    play_game = input("Do u want to play again yes/no : ")