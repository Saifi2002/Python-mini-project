import random
import time

HIGH_SCORE_FILE = "High_Score.txt"

# ----------- High Score Handling (Per Level) -----------
def load_high_scores():
    scores = {
        "easy": ("", 999999),
        "medium": ("", 999999),
        "insane": ("", 999999),
    }

    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            for line in file:
                level, name, score = line.strip().split(" => ")
                scores[level] = (name, int(score))
    except FileNotFoundError:
        pass

    return scores


def save_high_scores(scores):
    with open(HIGH_SCORE_FILE, "w") as file:
        for level, (name, score) in scores.items():
            if name:
                file.write(f"{level} => {name} => {score}\n")


# ----------- Game Logic -----------
def play_game():
    high_scores = load_high_scores()

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

        choice = input("Enter The Level (1/2/3) : ").strip()

        if choice == "1":
            level = "easy"
            secret_number = random.randint(1, 10)
            max_attempts = 5
        elif choice == "2":
            level = "medium"
            secret_number = random.randint(1, 100)
            max_attempts = 7
        elif choice == "3":
            level = "insane"
            secret_number = random.randint(1, 1_000_000)
            max_attempts = 10
        else:
            print("Invalid choice! Try again.")
            continue

        champion, best_score = high_scores[level]
        print(f"\n🏆 {level.upper()} Champion: {champion or 'None'} ({best_score if champion else 'N/A'} attempts)")

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
                total_time = round(time.time() - start_time, 2)

                print(f"\n🎉 Congratulations {player_name}! You guessed it right: {secret_number}")
                print("Total Attempts:", attempts)
                print(f"⏱️ Time Taken: {total_time} seconds")

                if attempts < best_score:
                    print("🔥 NEW HIGH SCORE FOR THIS LEVEL!")
                    high_scores[level] = (player_name, attempts)
                    save_high_scores(high_scores)
                else:
                    print("Nice try! Record still stands 😄")

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