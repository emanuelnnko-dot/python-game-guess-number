import random

print("=================")
print("GuessNumber-Game")
print("_________________ \n")
print("Welcome to GuessNumber Game \n")

print("Game Info:")
print(" > Please make sure you provide your user name and you continue to use the same user name.")
print(" > Kindly choose your prefered game difficult level either Easy (Level: 1), medium (Level: 2) or hard (Level: 3).")
print(" > Make sure you guess your number from 1 to 100 (not outside that range).")
print(" > Continue playing the game by guessing the number and type it to see if it matches with the correct number.")
print()

game_levels = { 
    "1": {"attempts_num": 10, "name": "Easy"},
    "2": {"attempts_num": 7, "name": "Medium"},
    "3": {"attempts_num": 5, "name": "Hard"},      
}

user_name = None
while True:
    user_name = input("Enter your user name: ").strip()
    print()
    if not user_name:
        print("Please make sure you enter your user name and you continue to use the same user name. \n")
        continue
    break

print(f'Hello "{user_name}", please continue with the game...')

selected_game_level = None
while True:
    selected_game_level = input("Choose game difficult level (by typing its respective level number): ").strip()
    print()
    if selected_game_level not in game_levels:
        print("Select game dificult level by only typing a number either 1, 2, or 3.")
        print("Type number 1 for Level 1 (Easy), 2 for Level 2 (Medium) or 3 for Level 3 (Hard). \n")
        continue
    break

print(f'You have selected "Level {selected_game_level}" ({game_levels[selected_game_level]["name"]} Level). \n')
input('Press "Enter" to start the game: ')

generated_number = random.randint(1, 100)

# print("Randomly Generated Number:", generated_number) # TODO: REMOVE THIS LINE *****************************************************************************************

players_scores_info = []

for attempt in range(1, game_levels[selected_game_level]["attempts_num"] + 1):
    try:
        attempts_remain = game_levels[selected_game_level]["attempts_num"] - attempt
        print()
        user_guessed_number = int(input("Guess the number: ").strip())
    except ValueError:
        print("Make sure you enter a number, your previous guess was not a number.")
        print(f"You have done {attempt} attempt(s), you have {attempts_remain} remaining guesses.")
    else:
        if user_guessed_number not in range(1, 100 + 1):
            print("Make sure you enter a number within a given range (from 1 t0 100), your previous guess was outside that range.")
            print(f"You have done {attempt} attempt(s), you have {attempts_remain} remaining guesses. \n")
        else:
            print(f"You have done {attempt} attempt(s), you have {attempts_remain} remaining guesses. \n")

            def is_guess_correct():
                if user_guessed_number == generated_number:
                    return True

            def feedback_help_info():
                gap = abs(generated_number - user_guessed_number)
                if gap <= 2: print("You are very close to correct answer!")
    
                if user_guessed_number < generated_number:
                    if gap >= 3 and gap <= 10: print("Your guess is little bit low. \n")
                    if gap > 10: print("Your guess is too low.")
    
                elif user_guessed_number > generated_number:
                    if gap >= 3 and gap <= 10: print("Your guess is little bit high.")
                    if gap > 10: print("Your guess is too high. \n")

            if not is_guess_correct():
                feedback_help_info()
                
            def is_game_over():
                if is_guess_correct() or attempts_remain == 0:
                    return True

            def game_over_message():
                if is_guess_correct():
                    print(f"Congratulations! You guess correctly.")
                elif attempts_remain == 0:
                    print(f"Sorry! All your guesses are incorrect.")

                print("The game is over, you may try again with different levels.")

            def manage_scores():
                score_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                current_player_score = score_values[-attempt]

                # print("Current player:", user_name, "Score:", current_player_score) # TODO: To be removed. *****************************

                user_name_exist = False
                for info in players_scores_info:
                    if info["user_name"] == user_name:
                        info["score"] += current_player_score
                        user_name_exist = True
                        num += 1

                # print("user_exist:", user_name_exist)
                
                if not user_name_exist:
                    current_player_score_info = {"user_name": user_name, "score": current_player_score}
                    players_scores_info.append(current_player_score_info)
                    
                # print("Players score info:", players_scores_info)

                with open("players_scores.txt", "w") as file:
                    for info in players_scores_info:
                        file.write(f'User name: {info['user_name']} - Score: {info['score']} \n')


            if is_guess_correct():
                manage_scores()
                
            if is_game_over():
                game_over_message()
                break
            
