game = ""
def welcome(name):
    print('Hello ' + name + ' and welcome to the World of Games (WoG). \nHere you can find many cool games to play.\n\n\n')
def load_game(name):
    game = int(input("Please choose a game to play: \n"
                 "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
                 "2. Guess Game - guess a number and see if you chose like the computer\n"
                 "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
                 ":"))
    difficulty = input("\n\n\nPlease choose game difficulty from 1 to 5: ")

    # match case
    match game:
        # pattern 1
        case 1:

            print("\n\n\nYou have choose to play: Memory Game\ndifficulty level: " + difficulty)
            from MemoryGame import play
            play(difficulty,name)

        # pattern 2
        case 2:
            print("You have choose to play: Guess Game\ndifficulty level: " + difficulty)
            print("\n\n\n\nlets Play the Guess Game")
            from GuessGame import play
            play(difficulty,name)
        # pattern 3
        case 3:
            print("You have choose to play: Currency Roulette\ndifficulty level: " + difficulty)
            print("\n\n\n\nlets Play the Currency Roulette Game")
            from CurrencyRouletteGame import play
            play(difficulty, name)
        # default pattern
        case _:
            print("Game option should be between 1 and 3")