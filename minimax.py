#coding:utf-8

import math
import numpy as np

NumOfEmptyCells = []


class AISolver(object):
    """docstring for AISolver."""
    def __init__(self, arg):
        super(AISolver, self).__init__()
        self.arg = arg

    def direction():
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3

    def minimax(node, depth, maximizingPlayer):
        if  depth == 0
            return heuristicScore(node)
        if maximizingPlayer:
            bestvalue = -np.inf
            for child in children:
                val = minimax(child, depth-1, False)
                bestvalue = max(bestvalue, val)
                return bestvalue
        else:
            bestvalue = np.inf
            for child in children:
                val = minimax(child, depth-1, True)
                bestvalue = min(bestvalue, val)
            return bestvalue
#actualScore = Pontuação atual
#clusteringScore = Pontuação de agrupamento
#numOfEmptyCells = Numero de celulas vazias
    def heuristicScore(actualScore, numOfEmptyCells, clusteringScore):
        # codigo heuristico sugerido pelo artigo
        score = actualScore + math.log(actualScore)*numOfEmptyCells - clusteringScore
        return math.max(score, math.min(actualScore, 1))

    def calculateClusteringScore(board):
        clusteringScore = 0

        for i in len()
        return clusteringScore

    def min(x,y):
        if x <= y:
            return x
        else:
            return y
    def max(x,y):
        if x >= y:
            return x
        else:
            return y
