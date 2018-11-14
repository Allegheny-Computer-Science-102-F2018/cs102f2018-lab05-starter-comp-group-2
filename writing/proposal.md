### Names:  
Tyler Lyle, Joshua Yee, Brianna Crawford, Zach Something idk bro I dont know your last name and am too lazy to walk next door to get it.
### Group:
1/2 Comp Group

# Sudoku Puzzle Solving Algorithms

## Intro

Sudoku is a puzzle game in which the board is set up into a three by three grid containing nine sub-regions.  Each of these sub-regions then contains another three by three grid.  As it may be a little hard to understand, an example of the standard puzzle is provided in the image below.  The puzzle is considered solved when each of the nine sub-regions contains one unique number (one through nine), as well as each column and row also containing only one unique number.  Although the number of sub-regions and sub-region components are able to be much larger in more complex puzzles.

Our proposed project examines two algorithms used to solve Sudoku puzzles.  The algorithms mentioned in the next section take two different approaches to the solving of Sudoku puzzles.  As such, we plan on examining these algorithms by subject of time to complete puzzles given different inputs, as well as looking at why these algorithms may have different efficiencies with our limited knowledge.  We will accomplish examination by first implementing the algorithms in Python as well as providing different input into each algorithm.  The output will then be a completed puzzle as well as a time to complete.  To ensure that time taken is standardized for both algorithms, we will place the line of code containing the timer directly at the start of the main loop for both programs.

![Sudoku](sudoku.png)

## Algorithms

The first of the two algorithms we plan to implement is Backtracking, AKA Brute Force. This method explores every possible outcome of a single branch until there is a failure of the rules set in place. For this reason Backtracking can be a very long and expensive (computationally) process. This method works by moving cell by cell and placing one of the possible remaining numbers, both for that region as well as the rows the cell is in. If there is no possible number that can be placed in that cell then the algorithm backs up to the previously assigned cell and tries to find a new number that will work. This process repeats until every cell has a number assigned and all cells are legal.

![Backtracking](Backtracking.gif)

In the second algorithm we will be looking at will be a way to solve it in a similar way, but instead of calling them from different methods, just having one method with a condensed idea of solving this code. This is compact and will be able to run effectively. However, we want to test and see which algorithm is more effective and more efficient.

## Conclusion

Sudoku is a fun puzzle game that many people enjoy, the goal of this project is to test two different algorithms and set test cases and benchmarks in order to deduce which code runs more effectively. We can do this by setting a timer for both methods and then running them on the same machine so that different space overhead will not be a variable when testing. This project is going to analyze the algorithms and show reasons why one algorithm may work more efficiently than the other.
