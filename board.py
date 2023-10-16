#
# board.py
#
# A Board class for the Eight Puzzle
#
# name: Tan Aydemir
# email: tanaydemir1@gmail.com
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                self.tiles[r][c] = digitstr[3*r+c]
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c

    ### the other method definitions are below ###


    def __repr__(self):
        """returns a string representation of a Board object"""
        s = ''
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] == '0':
                    s+= '_ '
                else:
                    s += self.tiles[row][col] + ' '
            s += '\n'
        return s
            
    def move_blank(self,direction):
        """takes an input, direction, and attempts to modify the Board object's 
        contents accordingly. returns True is the potential move is possible,
        returns False otherwise"""
        if direction != 'up' and direction != 'down' and \
            direction !='left' and direction !='right':
            return False
        else:
            if direction == 'left':
                if self.blank_c == 0:
                    return False
                else:
                    variable = self.tiles[self.blank_r][self.blank_c-1]
                    self.tiles[self.blank_r][self.blank_c-1] = self.tiles[self.blank_r][self.blank_c]
                    self.tiles[self.blank_r][self.blank_c] = variable
                    self.blank_c -= 1
                    return True
                    
            elif direction == 'right':
                if self.blank_c == 2:
                    return False
                else:
                    variable = self.tiles[self.blank_r][self.blank_c+1]
                    self.tiles[self.blank_r][self.blank_c+1] = self.tiles[self.blank_r][self.blank_c]
                    self.tiles[self.blank_r][self.blank_c] = variable
                    self.blank_c += 1
                    return True

            elif direction == 'down':
                if self.blank_r == 2:
                    return False
                else:
                    variable = self.tiles[self.blank_r+1][self.blank_c]
                    self.tiles[self.blank_r+1][self.blank_c] = self.tiles[self.blank_r][self.blank_c]
                    self.tiles[self.blank_r][self.blank_c] = variable
                    self.blank_r += 1
                    return True       
            elif direction == 'up':
                if self.blank_r == 0:
                    return False
                else:
                    variable = self.tiles[self.blank_r-1][self.blank_c]
                    self.tiles[self.blank_r-1][self.blank_c] = self.tiles[self.blank_r][self.blank_c]
                    self.tiles[self.blank_r][self.blank_c] = variable
                    self.blank_r -= 1
                    return True
            
    def digit_string(self):
        """creates and returns a string of digits that corresponds to 
        the current contents of the called Board object's tiles attribute"""
        s = ''
        for r in range(3):
            for c in range(3):
                s+= self.tiles[r][c]
        return s
    
    def copy(self):
        """returns a newly-contructed Board object that's a deep copy
        of the called object"""
        newboard = Board(self.digit_string())
        return newboard
    
    def num_misplaced(self):
        """counts and returns the number of tiles in the called Board object
        that are not where they should be (excluding blanks)"""
        numtil = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] != GOAL_TILES[r][c]:
                    if self.tiles[r][c] == "0":
                        numtil += 0
                    else:
                        numtil+= 1
        return numtil
    def __eq__(self,other):
        """returns True is the called self object and the called other
        object have the same content, returns False otherwise"""
        if self.tiles == other.tiles:
            return True
        else:
            return False










