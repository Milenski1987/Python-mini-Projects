import time

ROWS = 6
COLUMNS = 7
CONNECT_WINNER_COUNT = 4

directions = {
    "down": (1, 0),
    "right": (0, 1),
    "top_right": (-1, 1),
    "top_left": (-1, -1)
}


class InvalidColumn(Exception):
    pass


class FullColumn(Exception):
    pass


def get_position(player, board):
    while True:
        try:
            column = int(input(f"{player} please select a column: "))
            if column < 1 or column > 7:
                raise InvalidColumn
            column_index = column - 1
            for row_index in range(ROWS -1 , -1 , -1):
                if board[row_index][column_index] == 0:
                    return row_index, column_index
            raise FullColumn
        except ValueError:
            print(f"Please enter a valid number!")
        except InvalidColumn:
            print("Please enter a number between 1 and 7")
        except FullColumn:
            print("Column is full. Please select another column")


def is_valid_position(row, column):
    return row in range(ROWS) and column in range(COLUMNS)
  

def check_direction_count(row_index, column_index, row_index_move, column_index_move, board, player_symbol):
    count = 0
    for index in range(1, CONNECT_WINNER_COUNT):
        next_row_index = row_index + row_index_move * index
        next_column_index = column_index + column_index_move * index
        if not is_valid_position(next_row_index, next_column_index):
            return count
        if board[next_row_index][next_column_index] == player_symbol:
            count += 1
        else:
            return count
    return count


def is_winner(row_index, column_index, board, player_symbol):

    for direction, movement in directions.items():
        total_count = 1
        row_index_move, column_index_move = movement

        total_count += check_direction_count(
            row_index,
            column_index,
            row_index_move,
            column_index_move,
            board,
            player_symbol)

        if direction != "down":

            total_count += check_direction_count(
                row_index,
                column_index,
                -row_index_move,
                -column_index_move,
                board,
                player_symbol)

        if total_count >= CONNECT_WINNER_COUNT:
            return True
    return False


def show_board(board):
    for row in board:
        print(*row, sep= " ")


def main():
    game_board = []
    for _ in range(ROWS):
        game_board.append([0 for _ in range(COLUMNS)])

    first_player = input("Enter 'Player1' name: ")
    second_player = input("Enter 'Player2' name: ")
    first_player_symbol = 1
    second_player_symbol = 2
    time.sleep(1)
    print("This is current game board:")
    show_board(game_board)
    print()
    time.sleep(1)

    turn = 1

    while True:
        current_player = first_player if turn % 2 != 0 else second_player
        current_player_symbol = first_player_symbol if turn % 2 != 0 else second_player_symbol
        row_index, column_index  = get_position(current_player, game_board)
        game_board[row_index][column_index] = current_player_symbol
        show_board(game_board)
        time.sleep(1)
        print()

        if turn >=7 and is_winner(row_index, column_index, game_board,  current_player_symbol):
            print(f"Game over! The winner is {current_player}")
            break

        turn += 1

        if ROWS * COLUMNS + 1 == turn:
            print(f"Game over! Board is ful and result is DRAW!")
            break


main()