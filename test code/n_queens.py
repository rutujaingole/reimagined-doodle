def n_queens(board_size):

    # Occupied Diagonals and Columns
    # For right and left Diagonal respectively

    diagonal1 = {}
    diagonal2 = {}
    Col = {}

    ans = place_queen(
        0,
        [],
        board_size,
        diagonal1,
        diagonal2,
        Col,
        )

    return ans


# Recursive Function to check and place the queens

def place_queen(
    row,
    a,
    n,
    diagonal1,
    diagonal2,
    Col,
    ):

    # If the answer is found, row will be equal to the size of the board i.e. n

    if row == n:
        return a
    R = row + 1

    for C in range(1, n + 1):

        # Check that particular Column is free to place a queen or not

        if C not in Col and R + C not in diagonal1 and R - C \
            not in diagonal2:

            # Add the Column and their respective Diagonals to the dictionary
            # to mark they are Occupied

            Col[C] = 0
            diagonal1[R + C] = 0
            diagonal2[R - C] = 0
            chk = place_queen(
                row + 1,
                a + [(row, C - 1)],
                n,
                diagonal1,
                diagonal2,
                Col,
                )

            # If the answer is found, Stop the recursion

            if chk:
                return chk

            # Deleaating the Column and Diagonals to vacant that place

            del diagonal1[R + C]
            del Col[C]
            del diagonal2[R - C]

            return False


# -------------------------------Driver Code-------------------------------

if __name__ == '__main__':
    n = int(input('Enter the Board Size: '))
    answer = n_queens(n)

    if not answer:
        print ('Queens cannot be placed in the given Chessboard')
    else:

        print ('Queens are Placed in the chessboard')
        print ('Position :', answer)
