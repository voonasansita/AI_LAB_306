#function to display the board
def print_board(board) :
  for row in board :
    print(" | ".join(row))
    print("---------") # Adjusted length for 3 items joined by ' | '

#function to check the winner
def check_winner(board):
  #check rows
  for row in board:
    if row[0]==row[1]==row[2] != ' ':
      return True
  #check columns
  for col in range(3):
      if board[0][col]==board[1][col]==board[2][col] != ' ':
        return True
  #check diagonals
  if board[0][0]==board[1][1]==board[2][2] != ' ':
    return True
  if board[0][2]==board[1][1]==board[2][0] != ' ':
    return True
  return False

board = [[" " for _ in range(3)] for _ in range(3)]
player = "x"

for turn in range(9):
  print("\ncurrent board:")
  print_board(board)
  print(f"player {player}'s turn")

  while True: # Loop until a valid move is made
    try:
      row = int(input("enter the row (0,1,2):"))
      col = int(input("enter the column (0,1,2):"))
      if 0 <= row < 3 and 0 <= col < 3:
        if board[row][col] == " ":
          board[row][col] = player
          break # Exit while loop if move is valid
        else:
          print("Cell already occupied. Try again.")
      else:
        print("Invalid row or column. Please enter between 0 and 2.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  if check_winner(board):
    print("\ncurrent board:")
    print_board(board)
    print(f"Player {player} wins!")
    break

  # Switch player only if no winner and game continues
  player = "o" if player == "x" else "x"

# This else block executes if the for loop completes without a 'break' (i.e., a draw)
else:
  print("\nFinal board:")
  print_board(board)
  print("Game draw!")
