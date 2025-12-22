import random
import time

# ----------- High Score Handling -----------
def load_high_score(filename="High_Score.txt"):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if not lines:
                return "", 999999
            best_score = 999999
            top_player = ""
            for line in lines:
                name, score = line.strip().split(" => ")
                score = int(score)
                if score < best_score:
                    best_score = score
                    top_player = name
            return top_player, best_score
    except FileNotFoundError:
        return "", 999999

def save_high_score(player_name, attempts, filename="High_Score.txt"):
    with open(filename, "a") as file:
        file.write(f"{player_name} => {attempts}\n")


# ----------- Game Logic -----------
def play_game():
    top_player, high_score = load_high_score()

    play = input("Do you want to play game? (YES/No) : ").strip().lower()
    if play != "yes":
        print("Maybe next time! 👋")
        return

    player_name = input("Enter your name: ").strip()

    while True:
        print("\nChoose Difficulty level")
        print("Level 1 -> Easy (1-10, 5 attempts)")
        print("Level 2 -> Medium (1-100, 7 attempts)")
        print("Level 3 -> Insane (1-1000000, 10 attempts)")

        level = input("Enter The Level (1/2/3) : ").strip()
        if level not in ["1", "2", "3"]:
            print("Invalid choice! Try again.")
            continue

        level = int(level)
        if level == 1:
            secret_number = random.randint(1, 10)
            max_attempts = 5
        elif level == 2:
            secret_number = random.randint(1, 100)
            max_attempts = 7
        else:
            secret_number = random.randint(1, 1000000)
            max_attempts = 10

        attempts = 0
        start_time = time.time()

        while attempts < max_attempts:
            try:
                guess = int(input("Guess the number: ").strip())
            except ValueError:
                print("Please enter a valid number!")
                continue

            attempts += 1

            if guess == secret_number:
                end_time = time.time()
                total_time = round(end_time - start_time, 2)
                print(f"\n🎉 Congratulations {player_name}! You guessed it right: {secret_number}")
                print("Total Attempts:", attempts)
                print(f"⏱️ Time Taken: {total_time} seconds")

                if attempts < high_score:
                    print("---- 🏆 NEW HIGH SCORE! ----")
                    save_high_score(player_name, attempts)
                    high_score = attempts
                    top_player = player_name
                else:
                    print("---- Current Champion ----")
                    print("Name:", top_player, "🏆")
                    print("Best Score:", high_score)
                break

            elif abs(guess - secret_number) <= 2:
                print("🔥 Very Close!")
            elif guess > secret_number:
                print("Your guess is high")
            else:
                print("Your guess is low")

        else:
            print(f"\n😢 You Lose! Secret number was: {secret_number}")

        again = input("\nDo you want to play again? (yes/no) : ").strip().lower()
        if again != "yes":
            print("Thanks for playing! Bye 👋")
            break


# ----------- Run the Game -----------
if __name__ == "__main__":
    play_game()
