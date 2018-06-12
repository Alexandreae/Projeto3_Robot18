# Python 2
# Pip install PyUserInput

from pykeyboard import PyKeyboard

import PlayerIA
import LeTela
import time

time.sleep(3)
#print(LeTela.TelaInput())
# 0 UP
# 1 DOWN
# 2 LEFT
# 3 RIGHT
keyboard=None
lista=[0,0,0,0,0,0,0,0,2,2,0,0,2,2,0,0]
def Command(key):
    global keyboard
    if key == 0: keyboard.tap_key(keyboard.left_key)
    elif key == 1: keyboard.tap_key(keyboard.down_key)
    elif key == 2: keyboard.tap_key(keyboard.up_key)
    elif key == 3: keyboard.tap_key(keyboard.right_key)


def main():
    global keyboard
    Player = PlayerIA.PlayerAI()
    keyboard = PyKeyboard()
    while(True):
        inp = lista
        output = Player.getMove(inp)
        Command(output)
        print(inp)

if __name__ == "__main__":
   main()
