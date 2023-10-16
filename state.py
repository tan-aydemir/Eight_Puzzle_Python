#
# state.py
#
# A State class for the Eight Puzzle
#
# name: Tan Aydemir
# email: tanaydemir1@gmail.com
#
#

from board import *

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Method definitions are below ###
    def __init__(self,board,predecessor,move):
        """constructs a new state object by initializing the attributes
        board, predecessor, move, num_moves"""
        self.board = board
        self.predecessor = predecessor
        self.move = move
        if predecessor == None:
            self.num_moves = 0
        else:
            self.num_moves = predecessor.num_moves + 1
    
    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True.
        """
        return True

    def is_goal(self):
        """returns true if the called State object is a goal state. 
        Returns False otherwise.."""
        a = self.board.digit_string()
        count = 0
        for x in range(3):
            for y in range(3):
                 if GOAL_TILES[x][y] != a[count]:
                     return False
                 count += 1
        return True
    
    def generate_successors(self):
        """creates and returns a list of State objects for all successor
        states of the called State object"""
        successors = []
        for m in MOVES:
            b = self.board.copy()
            d = b.move_blank(m)
            if d == True:
                newstate = State(b,self,m)
                successors += [newstate]
        return successors
    
    def print_moves_to(self):
        """prints the sequence of moves that lead from the 
        initial state to the called State object """
        if self.predecessor == None:
            print('initial state:')
            print(self.board)
        else:
            self.predecessor.print_moves_to()
            print('move the blank', self.move + ':')
            print(self.board)
        
        
        
        
        
        
        
        
        
        
        
        
        

