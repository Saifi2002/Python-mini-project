import random
import time

with open("High_Score.txt", "r") as file:
    high_score = int(file.read())

play_game = input("Do you want to play game? (YES/No) : ").lower()

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
    start_time = time.time()
  
    while True:     
    
        guess = int(input("Guess the number: "))
        attempts = attempts + 1
    
        if guess == secret_number :
            print("Congratulations buddy!! Your Guess is right 🎉 "+""+ "The Secret Key is",secret_number)
            print ("Total Attempts ",attempts)
            
            end_time = time.time()
            total_time = round((end_time - start_time), 2)
            
            if attempts < high_score:
                print("🏆 NEW HIGH SCORE!")
                with open("High_Score.txt", "w") as file:
                    file.write(str(attempts))
                high_score = attempts
            else:
                print("High Score remains:", high_score)
            
            print("⏱️ Time Taken : ", total_time, "seconds")
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
    
    play_game = input("Do u want to play again yes/no : ").lower()