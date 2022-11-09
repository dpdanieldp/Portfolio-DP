"""
Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter.
If the board is valid return 'Finished!', otherwise return 'Try again!'
"""


def done_or_not(board):  # board[i][j]
    if len(board) != 9:
        return "Try again!"
    else:
        for line in board:
            if (len(line) != 9) or (len(line) > len(set(line))) or (sum(line) != 45):
                return "Try again!"
        else:
            for i in range(0, 9):
                vert_list = [
                    board[0][i],
                    board[1][i],
                    board[2][i],
                    board[3][i],
                    board[4][i],
                    board[5][i],
                    board[6][i],
                    board[7][i],
                    board[8][i],
                ]
                if sum(vert_list) != 45 or (len(vert_list) > len(set(vert_list))):
                    return "Try again!"
            else:
                for i in range(0, 7, 3):
                    region = [
                        board[i][i],
                        board[i][i + 1],
                        board[i][i + 2],
                        board[i + 1][i],
                        board[i + 1][i + 1],
                        board[i + 1][i + 2],
                        board[i + 2][i],
                        board[i + 2][i + 1],
                        board[i + 2][i + 2],
                    ]
                if sum(region) != 45 or (len(region) > len(set(region))):
                    return "Try again!"
                else:
                    return "Finished!"
