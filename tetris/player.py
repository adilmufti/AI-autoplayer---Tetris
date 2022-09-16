import random

from board import Direction, Rotation, Action
from random import Random

'''weight_holes = 22.5
weight_aggregate_height = 2.5
weight_bumpiness = 2.5
weight_complete_row = 4.2
weight_max_height = 4.1'''

'''weight_holes = 0.75
weight_aggregate_height = 0.3
weight_bumpiness = 0.18
weight_complete_row = 1.3
weight_max_height = 0'''

'''weight_holes = 0.989
weight_aggregate_height = 0.03358
weight_bumpiness = 0.1213
weight_complete_row = 0.6121
weight_max_height = 0.21844'''

'''weight_holes = 0.999
weight_aggregate_height = 0.03358
weight_bumpiness = 0.1253
weight_complete_row = 0.6121
weight_max_height = 0.21844'''

'''weight_holes = 0.989
weight_aggregate_height = 0.03358
weight_bumpiness = 0.1213
weight_complete_row = 0.36790
weight_max_height = 0.21844'''

'''weight_holes = 0.97226
weight_aggregate_height = 0 #.01894
weight_bumpiness = 0.2407
weight_complete_row = 0.26212
weight_max_height = 0 #.018951'''

'''weight_holes = 0.87496
weight_aggregate_height = 0.01894
weight_bumpiness = 0.00407
weight_complete_row = 0.71023
weight_max_height = 0.17293'''

'''weight_holes = 0.989
weight_aggregate_height = 0.03358
weight_bumpiness = 0.1213
weight_complete_row = 0.3679
weight_max_height = 0.218019'''

'''weight_holes = 0.66175
weight_aggregate_height = 0.47593
weight_bumpiness = 0.2922
#weight_complete_row = 3
weight_max_height = 0.13311'''

'''weight_holes = 21
weight_aggregate_height = 2
weight_bumpiness = 2.55
weight_complete_row = 4.4
weight_max_height = 4.55'''

'''weight_holes = 6.5
weight_aggregate_height = 1
weight_bumpiness = 1
weight_complete_row = 1
weight_max_height = 1'''

weight_holes = 21.52
weight_aggregate_height = 1.65
weight_bumpiness = 2.9
weight_complete_row = 3.4
weight_max_height = 4.5
weight_height_diff = 1.8

'''weight_holes = 0.89388
weight_aggregate_height = 0.33297
weight_bumpiness = 0.30102
weight_complete_row = 0.68934
weight_max_height = 0.18543'''

'''weight_holes = 0.99388
weight_aggregate_height = 0.28297
weight_bumpiness = 0.26200188
weight_complete_row = 0.521934
weight_max_height = 0.192194'''

class Player:
    def choose_action(self, board):
        raise NotImplementedError



class lastplayer(Player):

    def __init__(self, seed=None):
        self.random = Random(seed)
        self.rowage = 0

    def colheights(self, board):
        colheights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for x in range(0, 10):
            for y in range(24, 0, -1):
                if (x, y) in board.cells:
                    colheights[x] = 24 - y
        return colheights

    def aggregate_height(self, board):
        heights1 = self.colheights(board)
        ah = 0
        for i in range(0, 10):
            ah = ah + heights1[i]
        return ah

    def maxh(self, board):
        m = -1110
        h = self.colheights(board)
        for x in range(0, 10):
            if h[x] > m:
                m = h[x]
        return m

    def numberofcellsfilled(self, board):
        occupied = 0
        for y in range(0, 24):
            for x in range(0, 10):
                if (x, y) in board.cells:
                    occupied += 1
        return occupied

    def bumpiness(self, board):
        heights2 = self.colheights(board)
        difference = 0
        for j in range(0, 8):
            rang = (heights2[j] - heights2[j + 1])
            if rang < 0:
                rang = rang * (-1)
            difference = difference + rang
        last = abs(heights2[8] - heights2[9])
        difference = difference + 0.4*last
        return difference

    def height_diff(self, board):
        heights3 = self.colheights(board)
        same = 0
        for k in range(0, 8):
            diff = abs(heights3[k] - heights3[k+1])
            if diff == 0:
                same = same + 1
        return same
    def complete_rows(self, board):
        full = 0
        completerows = 0
        for y in range(0, 24):
            for x in range(0, 10):
                if (x, y) in board.cells:
                    full = full + 1
            if full == 10:
                completerows = completerows + 1
        return completerows

    '''def completed_rows(self, board, oldScore):
        completedrows = board.score - oldScore
        if completedrows < 25:
            completedrows = 0
        if 25 <= completedrows <= 100 and self.maxh(board) < 17:
            completedrows = -20
            self.rowage = 1
        if 100 <= completedrows <= 400 and self.maxh(board) < 13:
            completedrows = 0
            self.rowage = 2
        if 400 <= completedrows <= 1600:
            completedrows = 4 + 125
            self.rowage = 3
        if 1600 <= completedrows:
            completedrows = 10 + 625
            self.rowage = 4
        return completedrows'''

    def holes(self, board):
        holess = self.aggregate_height(board) - self.numberofcellsfilled(board)
        return holess

    '''def score_position(self, board):
        if self.maxh(board) < 18:
            score =- weight_aggregate_height * self.aggregate_height(
                board)- weight_bumpiness * self.bumpiness(board) - weight_max_height * self.maxh(
                board) - (weight_holes) * self.holes(board)
        else:
            score = - weight_aggregate_height * self.aggregate_height(
                board) - 1.2*weight_bumpiness * self.bumpiness(board) - 1.1*weight_max_height * self.maxh(
                board) - (0.7*weight_holes) * self.holes(board)
        return score'''

    def score_position(self, board):
        if self.maxh(board) < 18:
            score = weight_height_diff * self.height_diff(board) - weight_aggregate_height * self.aggregate_height(
                board) - weight_bumpiness * self.bumpiness(board) - weight_max_height * self.maxh(
                board) - (weight_holes) * self.holes(board)
        else:
            score = - weight_aggregate_height * self.aggregate_height(
                board) - 1 * weight_bumpiness * self.bumpiness(board) - 1 * weight_max_height * self.maxh(
                board) - (0.8*weight_holes) * self.holes(board)
        return score

    '''def score_position(self, board, oldScore):
        #if self.maxh(board) < 18:
        score = weight_complete_row * self.completed_rows(board, oldScore) - weight_aggregate_height * self.aggregate_height(
        board) - weight_bumpiness * self.bumpiness(board) - weight_max_height * self.maxh(
        board) - (weight_holes) * self.holes(board)
        else:
            score = weight_complete_row * self.completed_rows(board, oldScore) + (5 ** self.rowage) - weight_aggregate_height * self.aggregate_height(
                board) - weight_bumpiness * self.bumpiness(board) - weight_max_height * self.maxh(
                board) - (weight_holes) * self.holes(board)'''
       # return score

    def choose_action(self, board):

        xpos = board.falling.left
        bestscore = -1000000
        bestmoves = []

        for rotate in range(0, 4):
            cells1 = self.numberofcellsfilled(board)
            for x in range(0, 10):
                oldScore = board.score
                sandbox = board.clone()
                #cells1 = self.numberofcellsfilled(sandbox)
                holes1 = self.holes(sandbox)
                xpos = sandbox.falling.left
                moves = []
                landed = False

                if self.maxh(sandbox) >= 18 and sandbox.bombs_remaining != 0 and self.complete_rows(sandbox) < 30:
                    # need to drop bomb on the highest building
                    return Action.Bomb

                for i in range(0, rotate + 1):
                    sandbox.rotate(Rotation.Clockwise)
                    moves.append(Rotation.Clockwise)

                    if sandbox.falling is not None:
                        xpos = sandbox.falling.left
                    else:
                        landed = True
                        break

                while xpos > x and landed == False:

                    sandbox.move(Direction.Left)
                    moves.append(Direction.Left)

                    if sandbox.falling is not None:
                        xpos = sandbox.falling.left
                    else:
                        landed = True
                        break

                while xpos < x and landed == False:

                    sandbox.move(Direction.Right)
                    moves.append(Direction.Right)

                    if sandbox.falling is not None:
                        xpos = sandbox.falling.left
                    else:
                        landed = True
                        break

                if landed == False:
                    sandbox.move(Direction.Drop)
                    moves.append(Direction.Drop)
                cells2 = self.numberofcellsfilled(sandbox)
                holes2 = self.holes(sandbox)
                if holes2 - holes1 >= 1 and self.maxh(sandbox) < 16 and sandbox.discards_remaining != 0:
                    moves.append(Action.Discard)
                    return Action.Discard
                score = self.score_position(sandbox)
                '''if cells2 - cells1 == -6 and self.maxh(sandbox) < 17:
                    score = score - 40
                if cells2 - cells1 == -6 and self.maxh(sandbox) > 16:
                    score = score + 40
                if cells2 - cells1 == -16 and self.maxh(sandbox) < 15:
                    score = score - 5
                if cells2 - cells1 == -16 and self.maxh(sandbox) > 14:
                    score = score + 50
                if cells2 - cells1 == -26:
                    score = score + 4 + (5 ** 3)
                if cells2 - cells1 == -36:
                    score = score + 10 + (5 ** 4)'''
                if cells2 - cells1 == -6 and self.maxh(sandbox) < 14:
                    score = score - 40
                if cells2 - cells1 == -16 and self.maxh(sandbox) < 11:
                    score = score - 8
                if cells2 - cells1 == -26:
                    score = score + 50
                if cells2 - cells1 == -36:
                    score = score + 1000000000
                if cells2 - cells1 == -6 and self.maxh(sandbox) > 17:
                    score = score + 15
                if cells2 - cells1 == -16 and self.maxh(sandbox) > 15:
                    score = score + 25
                if score > bestscore:
                    bestscore = score
                    bestmoves = moves

        return bestmoves


SelectedPlayer = lastplayer
