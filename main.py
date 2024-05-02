#AI IS BLACK AND MINIMIZER

from ninemans.game import Game

print("Welcome to Nine Man's Morris!")
while True:
    player = input('Do you want to play first? This will give you a slight adventage (type "y" for yes or "n" for no): ')
    if player.lower() == "y":
        first = "WHITE"
        break
    elif player.lower() == "n":
        first = "BLACK"
        break
    else:
        print("Invalid input. Try again.")

game = Game(first)
game.play()