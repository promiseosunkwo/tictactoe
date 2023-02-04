from player import HumanPlayer, RandomComputerPlayer
import time

class tictactoe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self): #this methods prints the empty board to the console
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod #static methods are the methods that don't necessarily relate to the class ie we don't pass in any self arguement
    def print_board_nums(): #this methods prints the eboard with the indexes to the console
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def empty_squares(self):
        return ' ' in self.board #returns the spaces in the board

    def num_empty_squares(self):
        return self.board.count(' ') #counts the empty spaces and returns the count


    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == ' '] #this is the list comprehension method which is cleaner
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        #         return moves
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #checking if the rows have same value 
        row_index = square //3
        row = self.board[row_index*3 :( row_index + 1)*3 ]
        if all([spot == letter for spot in row]):
            return True

        #checking if the columns have same value 
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #checking if the diagonal have same value 
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in[ 0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in[ 2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True


def play(game, x_player, o_player, print_game=True): # the game itself
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_squares():
        if letter == 'O':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') #empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X' # short hand to say if letter is X then the next should be O vise versa

        #time sleep gives a little break between when you play and when the computer plays
        time.sleep(0.8)

    if print_game:
        print('it\'s a tie! ')



if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = tictactoe()
    play(t,o_player,x_player,print_game=True)