import random

# Function to simulate rolling a dice
def roll():
    """Simulates rolling a six-sided dice and returns a random value between 1 and 6."""
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

# Main game loop to set up the game and handle player turns
def play_game():
    """Main function to play the dice rolling game."""

    # Get the number of players (between 2 and 4)
    while True:
        players_number = input("Enter the number of players (2-4): ")
        if players_number.isdigit():
            players_number = int(players_number)
            if 2 <= players_number <= 4:
                break
            else:
                print("Must be 2 to 4 players!")
        else:
            print("Invalid input, try again!")

    # Get the maximum score to win the game
    while True:
        max_score = input("Enter max score: ")
        if max_score.isdigit() and int(max_score) > 0:
            max_score = int(max_score)
            break
        else:
            print("Invalid input, please enter a positive number!")

    # Initialize the scores for all players
    players_scores = [0 for _ in range(players_number)]

    # Game continues until a player reaches the max score
    while max(players_scores) < max_score:
        for player_index in range(players_number):
            print(f"\nPlayer {player_index + 1}'s turn.")
            print(f"Your total score is {players_scores[player_index]}")

            current_score = 0

            # Player keeps rolling until they choose to stop or roll a 1
            while True:
                should_roll = input("Would you like to roll (yes/no)? ").lower()

                if should_roll != "yes":
                    break  # Player chooses to stop rolling

                # Roll the dice
                value = roll()

                # If player rolls a 1, their turn ends and they lose the points for this round
                if value == 1:
                    print(f"You rolled a {value}! Turn over, no points added.")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f"You rolled a {value}!")

                # Display the current score of this turn
                print(f"Your current score this turn is: {current_score}.")

            # Add the current score to the player's total score
            players_scores[player_index] += current_score
            print(f"Your total score is now {players_scores[player_index]}.")

            # Check if the player has reached the maximum score to win
            if players_scores[player_index] >= max_score:
                break

    # Determine the winner by the highest score
    winner_score = max(players_scores)
    winner_index = players_scores.index(winner_score)

    # Announce the winner
    print(f"\nPlayer {winner_index + 1} has won the game with a score of {winner_score}!")

# Run the game
if __name__ == "__main__":
    play_game()
