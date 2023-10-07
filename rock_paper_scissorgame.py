import random
user_score = 0
computer_score = 0
choices = {1: "rock", 2: "paper", 3: "scissors"}
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It is a  tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"
while True:
    print("\nWelcome to Rock-Paper-Scissors-Game!")
    print("Enter your choice: 1 for rock, 2 for paper, 3 for scissors")
    user_choice = int(input("Your choice: "))
    if user_choice not in [1, 2, 3]:
        print("Invalid choice. Please choose 1,2,or3.")
        continue
    computer_choice = random.randint(1,3)

    print(f"You chose {choices[user_choice]}")
    print(f"Computer chose {choices[computer_choice]}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    print(f"Score: User {user_score} - {computer_score} Computer")

    play_again = input("Do you want to play the game again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing this game!")
