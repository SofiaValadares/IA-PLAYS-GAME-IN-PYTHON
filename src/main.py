import c_draw as draw
from levels import LEVELS

if __name__ == "__main__":
    while True:
        
        menu = draw.MainMenu(LEVELS)

        level = menu.run()

        if level == []: break

        game = draw.Game(level)

        if game.run(): break