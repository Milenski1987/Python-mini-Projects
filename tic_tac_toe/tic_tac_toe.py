import time

class InvalidPositionNumber(Exception):
    pass

class PositionTaken(Exception):
    pass


def choose_valid_poistion(player, board, mapper):
    while True:
        try:
            chosen_number = int(input(f"{player} please choose free position from board: "))
            if chosen_number < 1 or chosen_number > 9:
                raise InvalidPositionNumber
            row, column = mapper[chosen_number]
            if board[row][column] != " ":
                raise PositionTaken
            return chosen_number
        except ValueError:
            print("Invalid! Position must be a valid number")
        except InvalidPositionNumber:
            print("Invalid! Position must be a number between 1 and 9")
        except PositionTaken:
            print("Invalid! This position is not free. Please try again.")


def check_for_winner(symbol, board):
    for row in board:
        if all([element == symbol for element in row]):
            return True
    for column_index in range(len(board)):
        if all([board[row_index][column_index] == symbol for row_index in range(len(board))]):
            return True

    if all([board[index][index] == symbol for index in range(len(board))]):
        return True

    if all([board[index][len(board) - 1 -index] == symbol for index in range(len(board))]):
        return True

    return False


def play_turn(symbol, position, board, turn, mapper):

    board[mapper[position][0]][mapper[position][1]] = symbol

    if turn >= 5:
        return check_for_winner(symbol, board)


def show_board(current_board):
    for row in current_board:
        print(f"|  {'  |  '.join(row)}  |")


def get_players_info():
    player_one_name = input("Enter first player name: ")
    player_two_name = input("Enter second player name: ")

    while True:
        symbol = input(f"{player_one_name} please choose your symbol ('X' or 'O'): ")
        if symbol not in "XOxo":
            continue
        break

    player_one_symbol = symbol.upper()
    player_two_symbol = "O" if player_one_symbol == "X" else "X"

    return player_one_name, player_two_name, player_one_symbol, player_two_symbol


def save_game_results(winner):
    with open("result.txt") as file:
        lines = file.readlines()
    content = ""
    new_winner = True
    if lines:
        for line in lines:
            name, score = line.split(':')
            if name.lower == winner.lower():
                score = int(score.strip("\n")) + 1
                new_winner = False
            content += f"{name}:{score}\n"
    if new_winner:
        content += f"{winner}:{1}\n"

    with open("result.txt", "w") as file:
        file.write(content)


def show_stats():
    stats = {}
    with open("result.txt") as file:
        for row in file.readlines():
            name, score = row.split(":")
            stats[name] = int(score.strip("\n"))
    sorted_stats = sorted(stats.items(), key=lambda x: (-x[1],x[0]))
    for name, score in sorted_stats:
        print(f"{name} -> {score}")

def main():
    position_mapper = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2)
    }
    first_player_name, second_player_name, first_player_symbol, second_player_symbol = get_players_info()
    print(f"{first_player_name} choose to play with symbol '{first_player_symbol}'")
    print(f"{second_player_name} will play with symbol '{second_player_symbol}'")
    print()
    positions_field = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    time.sleep(1)
    print("Board positions:")
    show_board(positions_field)
    print()
    time.sleep(1)
    print(f"{first_player_name} starts first.")
    time.sleep(1)
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    turns = 1
    while turns < 10:
        current_player_name = first_player_name if turns % 2 != 0 else second_player_name
        player_symbol = first_player_symbol if current_player_name == first_player_name else second_player_symbol
        chosen_position = choose_valid_poistion(current_player_name, board, position_mapper)
        winner = play_turn(player_symbol, chosen_position, board, turns, position_mapper)
        show_board(board)
        time.sleep(1)
        if winner:
            print(f"\nGame Over! The winner is {current_player_name}")
            save_game_results(current_player_name)
            break
        turns += 1
    else:
        save_game_results("draw")
        print("\nGame Over! Draw")


if __name__ == "__main__":
    print("Available options: \n  => 'stats' to view current stats\n  => 'play' to start new game")
    command = input("Choose an activity: ")
    if command.lower() == "stats":
        show_stats()

    elif command.lower() == "play":
        main()

    else:
        exit(0)