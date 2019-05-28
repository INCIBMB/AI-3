import random

class TicTacToe():
    def __init__(self):
        """
        Board is a 1D array representing the board with positions given below
        |0|1|2|
        |3|4|5|
        |6|7|8|
        board[2]=moves[0] will place an X on the position 2
        board[2]='-' will make that position empty again
        """
        self.board = None
        self.moves = ['X', 'O']

    def show(self):
        for element in [self.board[i:i + 3] for i in range(0, len(self.board), 3)]:
            print(element)

    def get_free_positions(self):
        """what spots are left empty?"""
        return [k for k, v in enumerate(self.board) if v is '-']
        
        


    def evaluate(self):
        """Evaluates a board and returns -10 if X wins and 10 if O wins. Nothing is returned if not terminal state"""
        for i in range(0,9,3):
            if(self.board[i]==self.board[i+1] and
               self.board[i+1]==self.board[i+2]):
                if self.board[i]=='X':
                    return -10
                elif self.board[i]=='O':
                    return 10

        for i in range(3):
            if(self.board[i]==self.board[i+3] and
               self.board[i+3]==self.board[i+6]):
                if self.board[i]=='X':
                    return -10
                elif self.board[i]=='O':
                    return 10

        if(self.board[0]==self.board[4] and
           self.board[4]==self.board[8]):
            if self.board[0]=='X':
                    return -10
            elif self.board[0]=='O':
                    return 10

        if(self.board[2]==self.board[4] and
           self.board[4]==self.board[6]):
            if self.board[2]=='X':
                    return -10
            elif self.board[2]=='O':
                    return 10
    

    def minimax(self, move, alpha, beta):
        """

        Write the alpha beta version here
        A terminal state is defined by the function evaluate returning 10 or -10
        or by not having anymore free position (indicating a draw by the value 0)

        move: could take 'X' or 'O' indicating who is playing next
        
        aplha and beta: used for pruning.

        minimax should return the value of the board
        """
        


    def findBestMove(self, board):
        bestVal = -1000
        choices = []
        self.board = board
##      always start at position 4
        if len(self.get_free_positions()) == 9:
            return 4
        """
        Write the code here to find the best move
        You should add the best move to choice.
        If multiple moves are best that add them to choices
        """
        if choices != []:
            return random.choice(choices)
        else:
            return None


