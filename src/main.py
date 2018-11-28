import sudokuSolver1 as S1
import sudokuSolver2 as S2
import time

if __name__ == "__main__":
    i=0
    j=0

    field = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
    start_time = time.time()
    while i < 1000000:
        S1.solveSudoku(field)
        i+=1
        print(i)
    S1_time = (time.time() - start_time)

    start_time = time.time()
    while j <100000:
        S2.solve(field)
        j+=1
        print(j)
    S2_time = (time.time() - start_time)
    print("Execution time for S1: ", S1_time,"s.")
    print("Execution time for S2: ", S2_time,"s.")

    print("Difference in execution time is: ", (S1_time - S2_time), "s.")
