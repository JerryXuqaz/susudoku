def used_in_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False


# 找出num在该arr的col列是否出现过
def used_in_col(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False


# 找出num在该arr的3x3-box是否出现过，更应注意的是，传参技巧！
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[row + i][col + j] == num:
                return True
    return False


def check_location_is_safe(arr, row, col, num):
    return not used_in_row(arr, row, num) \
           and not used_in_col(arr, col, num) \
           and not used_in_box(arr, row - row % 3, col - col % 3, num)


def solve_sudoku(arr):
    l = [0, 0]
    # 找出还未被填充的位置
    if not find_empty_location(arr, l):
        return True
    # 未被填充的位置，赋值给row，col
    row = l[0]
    col = l[1]

    for num in range(1, 10):
        if check_location_is_safe(arr, row, col, num):
            arr[row][col] = num
            if solve_sudoku(arr):
                return True
            # 若当前num导致未来并没有结果，则当前所填充的数无效，置0后选下一个数测试
            arr[row][col] = 0

    return False


def print_board(jerry):
    for i in range(len(jerry)):

        if i % 3 == 0 and i != 0:
            print("-----------------")
        for j in range(len(jerry[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            print(jerry[i][j], end="")
        #                print_board(board)
        print()

    print()


def get_empty(board):
    """
    This function gets the first empty space
    :param board: A 9x9 list of ints sudoku board
    :return: the indices of the first empty space in the board
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j


def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                l[0] = row
                l[1] = col
                # print("empty: row="+str(row)+" col="+str(col))
                return True
    return False


if __name__ == "__main__":

    example_board = [[0 for x in range(9)] for y in range(9)]
example_board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

if solve_sudoku(example_board):
    print_board(example_board)
