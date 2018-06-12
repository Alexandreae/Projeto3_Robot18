import sys
from random import randint
import MiniMax
import MiniMaxAB
import numpy as np
import Helper

class PlayerAI:
    def getMove(self, mapgrid):
        [children, moving] = Helper.getAvailableChildren(mapgrid)  # Cria as possibilidades de novo Grid
        maxpath = -np.inf
        direction = 0

        for i in range(len(children)):
            c = children[i]
            emptyTiles = len([j for j, x in enumerate(c) if x == 0])
            m = moving[i]
            highest_value = -np.inf
            selection = 2
##                        if selection == '1':
##                            maxdepth = 4
##                            highest_value = MiniMax.calculate(c, maxdepth, False)  # Aplica MiniMax Comum
##                            if m == 0 or m == 2:
##                                highest_value += 10000
            if selection == 2:
                maxdepth = 4
                highest_value = MiniMaxAB.calculate(c, maxdepth,-np.inf,np.inf, False)  # Aplica MiniMax Alpha Beta
                if m == 0 or m == 2:
                    highest_value += 10000

            if highest_value > maxpath:
                direction = m
                maxpath = highest_value

            return direction
