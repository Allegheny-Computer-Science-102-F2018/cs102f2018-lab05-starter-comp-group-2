import sudokuSolver1 as S1
import sudokuSolver2 as S2
import time
import sys


def output(a):
    sys.stdout.write(str(a))

def print_field(field):
    # end_time = (time.time() - start_time)
    if not field:
        output("No solution")
        return
    for i in range(9):
        for j in range(9):
            cell = field[i][j]
            if cell == 0 or isinstance(cell, set):
                output('.')
            else:
                output(cell)
            if (j + 1) % 3 == 0 and j < 8:
                output(' |')

            if j != 8:
                output(' ')
        output('\n')
        if (i + 1) % 3 == 0 and i < 8:
            output("- - - + - - - + - - -\n")
    # print("\n End time = ", end_time)


if __name__ == "__main__":
    i=0
    j=0
    start_time = time.time()
    while i < 1000:
        # not complex
        field = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
        # very complex
        # field = [[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]]
        S1.solveSudoku(field)
        i+=1
        print(i)
    S1_time = (time.time() - start_time)

    start_time = time.time()
    while j <1000:
        # not complex
        field = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
        # very complex
        # field = [[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]]
        S2.solve(field)
        j+=1
        print(j)
    S2_time = (time.time() - start_time)
    print("Execution time for S1: ", S1_time,"s.")
    print("Execution time for S2: ", S2_time,"s.")

    print("Difference in execution time is: ", (S1_time - S2_time), "s.")
