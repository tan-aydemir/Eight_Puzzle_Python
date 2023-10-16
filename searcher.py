#
# searcher.py
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Tan Aydemir
# email: tanaydemir1@gmail.com
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        The program is a superclass of classes for
        other state-space search algorithms, as well.
    """
    ### Seacher Method definitions are coded below. ###
    def __init__(self,depth_limit):
        """constructs a new Searcher object with depth_limit, num_tested and states."""
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s

    def add_state(self,new_state):
        """takes a single State object called new_state and 
        adds it to the Searcher‘s list of untested states"""
        self.states += [new_state]
        
    def should_add(self,state):
        """takes a State object called state and returns True
        if the called Searcher should add state to its 
        list of untested states"""
        if state.creates_cycle():
            return False
        elif self.depth_limit != -1 and state > self.depth_limit:
            return False
        else:
            return True
        
    def add_states(self,new_states):
        """takes a list State objects called new_states, and
        that processes the elements of new_states one at a time"""
        for s in new_states:
            if self.should_add(s) == True:
                self.add_state(s)
            
    def next_state(self):
        """used to obtain the next state to be tested"""
        s = random.choice(self.states)
        self.states.remove(s)
        return s

    def find_solution(self,init_state):
        """ performs a full state-space search that begins 
        at the specified initial state init_state and ends 
        when the goal state is found or when the Searcher 
        runs out of untested states."""
        self.add_state(init_state)
        while len(self.states) != 0:
            temp = self.next_state()
            self.num_tested += 1
            if temp.is_goal() == True:
                return temp
            else:
                self.add_states(temp.generate_successors())
        return None
            
    ### BFSeacher and DFSearcher class definitions are coded below. ###

class BFSearcher(Searcher):
    """perform breadth-first search (BFS) instead of random search"""
    def next_state(self):
        s = self.states[0]
        self.states.remove(s)
        return s
    
class DFSearcher(Searcher):
    """perform depth-first search (DFS) instead of random search"""
    def next_state(self):
        s = self.states[-1]
        self.states.remove(s)
        return s
    
    
    


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

def h1(state):
    """takes a State object called state, and that computes
    and returns an estimate of how many additional moves are needed to get from state to the goal"""
    estimate = state.board.num_misplaced()
    return estimate


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### GreedySearcher method definitions are coded here. ###
    def __init__(self,heuristic):
        """constructs a new GreedySearcher object."""
        super().__init__(-1)
        self.heuristic = heuristic

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def priority(self,state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1*self.heuristic(state)
    
    def add_state(self,state):
        """overrides (i.e., replaces) the add_state method that is inherited from Searcher"""
        priority = self.priority(state)
        self.states += [[priority,state]]
        
    def next_state(self):
        """ overrides (i.e., replaces) the next_state method that is inherited from Searcher"""
        maxstate = max(self.states)
        self.states.remove(maxstate)
        return maxstate[1]
    
    
### AStarSeacher class definition is coded below. ###
class AStarSearcher(Searcher):
    """performs A * search"""
    def __init__(self,heuristic):
        """constructs a new AStarSearcher object."""
        super().__init__(-1)
        self.heuristic = heuristic

    
    def priority(self,state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher"""
        return -1*(self.heuristic(state)+ state.num_moves)






