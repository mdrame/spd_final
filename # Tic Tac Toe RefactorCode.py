import random

NUM_SPACES = 10
def draw_board(board):
  """
  This function prints out the board that it was passed.
  "board" is a list of 10 strings representing the board (ignore index 0).
  """
  print('   |   |')
  print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
  print(' ❼ |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  print(' ❹ |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  print(' ❶ |   |')

def input_player_letter():
  """
  Lets the player type which letter they want to be.
  Returns a list with the player’s letter as the first item,
  and the computer's letter as the second.
  """
  letter = ''
  while not (letter == 'X' or letter == 'O'):
    print('Do you want to be X or O?')
    letter = input().upper()

  # the first element in the list is the player’s letter, 
  # the second is the computer's letter.
  if letter == 'X':
    return ['X', 'O']                    
  return ['O', 'X']

def who_goes_first():
  """
  Randomly choose the player who goes first.
  """
  if random.randint(0, 1) == 0:
    return 'computer'                     
  return 'player'

def play_again():
  """
  This function returns True if the player wants to play again,
  otherwise it returns False.
  """
  print('Do you want to play again? (yes or no)')
  return input().lower().startswith('y')

def make_move(board, letter, move):
  board[move] = letter

def is_winner(board, letter):
  """
  Given a board and a player’s letter, this function returns True if that player has won.
  We use bo instead of board and le instead of letter so we don’t have to type as much.
  """
  ac_top = (board[7] == letter and board[8] == letter and board[9] == letter)
  ac_middle = (board[4] == letter and board[5] == letter and board[6] == letter)
  ac_bottom = (board[1] == letter and board[2] == letter and board[3] == letter)
  do_left = (board[7] == letter and board[4] == letter and board[1] == letter)
  do_middle = (board[8] == letter and board[5] == letter and board[2] == letter)
  do_right = (board[9] == letter and board[6] == letter and board[3] == letter)
  diagonal_a = (board[7] == letter and board[5] == letter and board[3] == letter)
  diagonal_b = (board[9] == letter and board[5] == letter and board[1] == letter)

  return (ac_top or ac_middle or ac_bottom or do_left or
        do_middle or do_right or diagonal_a or diagonal_b)

def get_board_copy(board):
  """
  Make a duplicate of the board list and return it the duplicate.
  """
  dupeBoard = []
  for i in range(len(board)):
      dupeBoard.append(board[i])
  return dupeBoard

def is_space_free(board, move):
  """Return true if the passed move is free on the passed board."""
  return board[move] == ' '

def get_player_move(board):
  """
  Let the player type in their move.
  """
  player_move = ' ' # TODO: W0621: Redefining name 'move' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
  while player_move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(player_move)):
      print('What is your next move? (1-9)')
      player_move = input()
  return int(player_move)

def choose_random_move_from_list(board, moves_list):
  """
  Returns a valid move from the passed list on the passed board.
  Returns None if there is no valid move.
  """
  possible_moves = []
  for i in moves_list:
    if is_space_free(board, i):
      possible_moves.append(i)

  if len(possible_moves) != 0: # TODO: How would you write this pythanically? (You can google for it!)
      return random.choice(possible_moves) # TODO: Else was not necessary
  return None

def get_computer_move(board, computer_letter): # TODO: W0621: Redefining name 'computerLetter' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
  """
  Given a board and the computer's letter, determine where to move and 
  return that move.
  """
  if computer_letter == 'X':
    player_letter = 'O'
  else:
    player_letter = 'X'

  # Here is our algorithm for our Tic Tac Toe AI:
  # First, check if we can win in the next move
  for i in range(1, NUM_SPACES):
    copy = get_board_copy(board)
    if is_space_free(copy, i):
      make_move(copy, computer_letter, i)
      if is_winner(copy, computer_letter):
        return i

  # Check if the player could win on their next move, and block them.
  for i in range(1, NUM_SPACES):
    copy = get_board_copy(board)
    if is_space_free(copy, i):
      make_move(copy, player_letter, i)
      if is_winner(copy, player_letter):
        return i

  # Try to take one of the corners, if they are free.
  move = choose_random_move_from_list(board, [1, 3, 7, 9])
  if move is not None:
      return move

  # Try to take the center, if it is free.
  if is_space_free(board, 5):
      return 5

  # Move on one of the sides.
  return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
  """
  Return True if every space on the board has been taken. Otherwise return False.
  """
  for i in range(1, NUM_SPACES):
    if is_space_free(board, i):
      return False
  return True

def start_game():
    """starts the tic tac toe game"""
   
    print('Welcome to Tic Tac Toe!')
    
    while True:
        the_board = [' '] * NUM_SPACES
        player_letter, computer_letter = input_player_letter()
        turn = who_goes_first()
        print('The ' + turn + ' will go first.')

        while True:
                if turn == 'player':

                    draw_board(the_board)
                    move = get_player_move(the_board)
                    make_move(the_board, player_letter, move)
                    # player wins
                    if is_winner(the_board, player_letter):
                        draw_board(the_board)
                        print('Hooray! You have won the game!')
                        break

                    if is_board_full(the_board):
                        draw_board(the_board)
                        print('The game is a tie!')
                        break
                    turn = 'computer'

                else:
                    move = get_computer_move(the_board, computer_letter)
                    make_move(the_board, computer_letter, move)
                    # computer wins
                    if is_winner(the_board, computer_letter):
                        draw_board(the_board)
                        print('The computer has beaten you! You lose.')
                        break
                    # game is tie
                    if is_board_full(the_board):
                        draw_board(the_board)
                        print('The game is a tie!')
                        break
                    turn = 'player'

        if not play_again():
            break

start_game()