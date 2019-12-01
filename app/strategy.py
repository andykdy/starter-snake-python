from util import *
import random

"""
Strategy structure
The AI will always have a strategy that determines how it will behave
"""


class Strategy:
    def __init__(self, me, board):
        self.me = me
        self.board = board
        self.moves = ['up', 'down', 'left', 'right']
        self.heuristics = [x[:] for x in [[0] * board["width"]] * board["width"]]

    """
    Returns the coordinates of the nearest food in regards to the head
    Uses Manhattan distance calculation
    """
    def nearest_food(self):
        foods = self.board["food"]
        head = self.me["body"][0]
        dist = [0] * len(foods)
        for idx, food in enumerate(foods):
            dist[idx] = manhattan((food["x"], food["y"]), (head["x"], head["y"]))
        return foods[dist.index(min(dist))]

    """
    Updates the Strategy with new board data
    """
    def update(self, me, board):
        self.me = me
        self.board = board


"""
Starting/Idle strategy
Used primarily for debugging and implementation
"""
class Start(Strategy):
    def __init__(self, me, board):
        Strategy.__init__(self, me, board)

    def calculate_move(self):
        possible_moves = ['up', 'down', 'left', 'right']
        body = self.me["body"]
        for part in body:
            h_diff = body[0]["x"] - part["x"]
            v_diff = body[0]["y"] - part["y"]
            board_width = self.board["width"]
            print(h_diff, v_diff)
            if (h_diff is 1 or body[0]["x"] is 0) and 'left' in possible_moves :
                possible_moves.remove('left')
            if (h_diff is -1 or body[0]["x"] is board_width - 1) and 'right' in possible_moves:
                possible_moves.remove('right')
            if (v_diff is 1 or body[0]["y"] is 0) and 'up' in possible_moves:
                possible_moves.remove('up')
            if (v_diff is -1 or body[0]["y"] is board_width - 1) and 'down' in possible_moves:
                possible_moves.remove('down')
        if len(possible_moves) is 0:
            return 'up'
        return random.choice(possible_moves)


"""
Prioritize food acquisition over anything else
"""
class Hungry(Strategy):
    def __init__(self, me, board):
        Strategy.__init__(self, me, board)


"""
Look for nearest snake and attempt head on collision in order to execute target
"""
class HeadHunter(Strategy):
    def __init__(self, me, board):
        Strategy.__init__(self, me, board)


"""
Defensive position, chase tail in order to reduce avenue of attack
"""


class TailChase(Strategy):
    def __init__(self, me, board):
        Strategy.__init__(self, me, board)
