# Eight Puzzle Solver

This GitHub repository contains Python code for solving the Eight Puzzle problem using various state-space search algorithms. The Eight Puzzle is a classic sliding puzzle with eight numbered tiles and an empty space, often found in puzzle games and brain teasers.

## Problem Description

The objective of this project is to find a sequence of moves that solves the Eight Puzzle. Starting from an initial board configuration, the goal is to reach a predefined target state. This problem has applications in artificial intelligence, game theory, and optimization.

The following search algorithms have been implemented to tackle the Eight Puzzle:

- **Random Search**: A randomized approach that explores the search space through random moves.
- **Breadth-First Search (BFS)**: A systematic approach that explores all possible moves at each level of the search tree.
- **Depth-First Search (DFS)**: A strategy that explores as far down the tree as possible before backtracking.
- **Greedy Search**: An informed search using heuristics to prioritize moves that appear to be closer to the solution.
- **A(*) Search**: An advanced informed search algorithm that combines a cost function with heuristics to efficiently reach the solution.

## Code Structure

The repository consists of several Python classes and functions that work together to solve the Eight Puzzle:

- `state.py`: Defines the `State` class, representing the state of the Eight Puzzle. It manages the current board configuration, predecessor states, moves, and more.
- `searcher.py`: Contains classes for different search algorithms, such as `Searcher`, `BFSearcher`, `DFSearcher`, `GreedySearcher`, and `AStarSearcher`. It also includes a function to create an appropriate searcher object based on algorithm choice.
- `eight_puzzle.py`: A driver script for solving Eight Puzzles. It allows users to specify the initial board configuration, search algorithm, and parameters. The script reports the time taken and the number of states tested, and it can display the solution path.
- `board.py`: Defines the `Board` class, which represents the game board of an Eight Puzzle. It includes methods for moving tiles, creating string representations of the board, copying the board, and counting misplaced tiles.
- `timer.py`: Provides a timer class to measure code execution time.

## Usage

To run the Eight Puzzle Solver, follow these steps:

1. Clone the repository to your local machine.
2. Open the command line or terminal.
3. Navigate to the project directory.
4. Use Python to execute the `eight_puzzle.py` script, providing the desired initial board configuration and search algorithm.

Detailed usage instructions can be found in each script's comments. You can experiment with different initial configurations and algorithms to see how the solver performs.

Feel free to explore the code and contribute to the project. If you have questions, feedback, or suggestions, please don't hesitate to reach out.

## Credits

- Author: Tan Aydemir
- Email: tanaydemir1@gmail.com
