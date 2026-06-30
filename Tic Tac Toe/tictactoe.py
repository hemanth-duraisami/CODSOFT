def create_board():
    return [" " for _ in range(9)]


def print_board(board):
    for row in range(3):
        cells = []
        for col in range(3):
            index = row * 3 + col
            if board[index] == " ":
                cells.append(str(index + 1))
            else:
                cells.append(board[index])
        print(" " + cells[0] + " | " + cells[1] + " | " + cells[2] + " ")
        if row < 2:
            print("---+---+---")


def get_winner(board):
    winning_lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for line in winning_lines:
        a, b, c = line
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board):
    if get_winner(board) is not None:
        return False
    for cell in board:
        if cell == " ":
            return False
    return True


def is_game_over(board):
    return get_winner(board) is not None or is_draw(board)


def get_human_move(board):
    while True:
        user_input = input("Enter your move (1-9): ").strip()
        if not user_input.isdigit():
            print("Invalid input. Please enter a number from 1 to 9.")
            continue
        position = int(user_input) - 1
        if position < 0 or position > 8:
            print("Invalid position. Please choose a number from 1 to 9.")
            continue
        if board[position] != " ":
            print("That position is already taken. Choose another.")
            continue
        return position


def minimax(board, is_ai_turn, alpha, beta):
    winner = get_winner(board)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if is_draw(board):
        return 0

    if is_ai_turn:
        best_score = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False, alpha, beta)
                board[i] = " "
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score

    best_score = float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, True, alpha, beta)
            board[i] = " "
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
    return best_score


def get_ai_move(board):
    best_score = float("-inf")
    best_move = 0
    alpha = float("-inf")
    beta = float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False, alpha, beta)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
            alpha = max(alpha, best_score)
    return best_move


def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are X. The AI is O.")
    print("Empty cells show their position number (1-9).")
    print()

    while not is_game_over(board):
        print_board(board)
        print()
        move = get_human_move(board)
        board[move] = "X"
        if is_game_over(board):
            break
        print()
        print("AI is thinking...")
        ai_move = get_ai_move(board)
        board[ai_move] = "O"
        print()

    print_board(board)
    print()
    winner = get_winner(board)
    if winner == "X":
        print("Congratulations! You win!")
    elif winner == "O":
        print("The AI wins! Better luck next time.")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    play_game()
