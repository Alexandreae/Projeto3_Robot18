# Python 2
# Pip install PyUserInput

from pykeyboard import PyKeyboard

import PlayerIA
import LeTela


# 0 UP
# 1 DOWN
# 2 LEFT
# 3 RIGHT

def Command(key):
    if key == 0: keyboard.tap_key(keyboard.up_key)
    elif key == 1: keyboard.tap_key(keyboard.down_key)
    elif key == 2: keyboard.tap_key(keyboard.left_key)
    elif key == 3: keyboard.tap_key(keyboard.right_key)


def main():
    Player = PlayerIA.PlayerAI()
    keyboard = PyKeyboard()
    while(True):
        input = TelaInput()
        output = Player.getMove(input)
        Command(output)

if __name__ == "__main__":
    main()
