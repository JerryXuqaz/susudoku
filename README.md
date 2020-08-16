# susudoku: 
 This is a cade that can help you to sovle sudoku, with in a little amount of time, or if you do not known how to solve it.
 
## introduction:
  Many people do not known how to solve a sudoku, or might want to check if they did it right or not so people can input their sudoku board
 into the file and it will automaticlly gives out the board that is filled up.
 
 ### used_in_row
  This is the code for find out the num did or did not appear at the particular arr in the row
  
 ### used_in_col
  This is the code for find out the num did or did not appear at the particular arr in the col
  
 ### used_in_box
  find if the number had been appeared in the arr or not

 ### check_location_is_safe
  check if the number was safe at that place, row, col, and arr
 
 ### solve_sudoku
  
  l = [0, 0] to find place without number
  and then give the place a row and col
 
 if a num make the list do not have result then the num is not available and give the place a 0 and repeat the previous step 
 
 ### print_board
  print the boad, as the roght sudoku form. looks better
  
 ### get_empty
  gets the first empty space
    :param board: A 9x9 list of ints sudoku board
    :return: the indices of the first empty space in the board
    
    
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

the board and step up the code and let it work
   and then solve it
