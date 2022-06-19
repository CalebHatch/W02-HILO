"""
Hilo Game
by: Caleb Hatch
"""
import random


# Keeps track of the amount of the player's points.
class Player:
    def __init__(self, points):
        self.points = points


player = Player(300)

game_loop = True


# Contains conditions for all three game endings
class GameEndResults:
    global game_second_card, player_guess

    # For when the player guesses correctly. Adds 100 to score
    @staticmethod
    def win_result():
        print("Next card was " + str(game_second_card) + ", and you guessed \"" + str(
            player_guess) + "\". You got it!")
        print("")
        player.points = (player.points + 100)

    # For when the player guesses incorrectly
    @staticmethod
    def loss_result():
        print("Next card was " + str(game_second_card) + ", and you guessed \"" + str(player_guess) +
              "\". Better luck next time!")
        print("")
        player.points = (player.points - 75)

    # For whenever the game should be ended. Outputs a "game over" message to the user and uses the "quit()"
    # command to end the program.
    @staticmethod
    def player_end_state():
        global game_loop
        print("Game over!\nGoodbye.")
        quit()


def main():
    global player, game_loop, game_second_card, player_guess

    while game_loop:
        game_first_card = random.randint(1, 13)
        print("The card is: " + str(game_first_card) + ".")

        player_guess = input("Higher or Lower? [h/l]: ")
        player_guess = player_guess.upper()

        game_second_card = random.randint(2, 12)

        if game_first_card > game_second_card:
            if player_guess == "L":
                GameEndResults.win_result()
            elif player_guess == "H":
                GameEndResults.loss_result()
        elif game_first_card < game_second_card:
            if player_guess == "H":
                GameEndResults.win_result()
            elif player_guess == "L":
                GameEndResults.loss_result()
        elif game_first_card == game_second_card:
            GameEndResults.win_result()

        print("Your score is: " + str(player.points) + ".")
        user_retry = input("Play again? [y/n]: ")
        user_retry = user_retry.upper()

        if user_retry == "Y":  # Game will loop as long as the user keeps entering "y"
            game_loop = True
            continue
        elif user_retry == "N":
            GameEndResults.player_end_state()
        else:
            print("Invalid input. Please type either \"y\" or \"n\"")

        if player.points <= 0:
            print("Your score reached below zero!")
            GameEndResults.player_end_state()


if __name__ == "__main__":
    global game_second_card, player_guess
    main()
