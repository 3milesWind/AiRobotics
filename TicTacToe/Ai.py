from __future__ import absolute_import, division, print_function
import copy, random
from main import Game

MAX_PLAYER, CHANCE_PLAYER = 'x', '0'
class Node:
    def __init__(self, state, player_type):
        self.state = (copy.deepcopy(state[0]), state[1])
        self.children = []
        self.player_type = player_type

class AI:
    # Recommended: do not modify this __init__ function
    def __init__(self, root_state):
        self.root = Node(root_state, MAX_PLAYER)

    # recursive function to build a game tree
    def build_tree(self, node=None):
        if node == None:
            node = self.root
        if Game.isTerminal():
            return node
        if node.player_type == MAX_PLAYER:
            openTitle = Game.open_tiles()
            for title in openTitle:
                node.children.append()

        elif node.player_type == CHANCE_PLAYER:
            pass

    # Do not modify this function
    def compute_decision(self):
        self.build_tree()
        direction, _ = self.expectimax(self.root)
        return direction
