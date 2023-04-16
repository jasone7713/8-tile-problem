# 8-tile-problem

This file describes how to execute the code, as well as a brief description of each file in the repo. 

-DEPENDENCIES
Python is the only thing required to run this code. 


-RUNNING INSTRUCTIONS
The driver code for this program is the main.py file. To run, you will need to cd into the directory of the main.py file and run the following command:

python main.py <BFS|DFS|DIJ> <input_file>

The program uses command-line arguments to get the algorithm and input file from the user. In the above command, BFS runs Breadth First Search, DFS runs Depth First Search, and DIJ runs Dijkstra's algorithm. 

The program requires an input file to read the starting state of the puzzle. The default filename that the program will use is input.txt but you can optionally include a different filename in the 3rd command-line argument. If you do not include a filename when calling the program it will assume the input file is input.txt.

The input file is expected to be in the following format: 

<tile> <tile> <tile>
<tile> <tile> <tile>
<tile> <tile> <tile>

Each <tile> should be a digit from 0-9. 0 represents the empty space in the puzzle. An example input file would look like this:

1 3 4
8 0 2
7 6 5

The output of the program will be the execution time followed by a list of moves that the algorithm took to find the solution, and finally the overall cost of solving the puzzle. 


-FILES
This section details all of the files in this project and their purpose. 

    main.py: the driver code for the program. Takes in the algorithm to run and the input file from the user. Calls on the Solver to solve the puzzle and perform the output. 

    solver.py: implements the solve function. This function takes in the start state, goal state, the algorithm to run (BFS|DFS|DIJ), and a mode called quiet. The solve function will call on BFS|DFS|DIJ depending on which algorithm is being run. The solve function also gets the ouput and prints the steps taken by the algorithm and te total cost. By passing quiet=True when calling solve we can bypass printing the step list. This an internal fgeature only used for testing the program, so this feature is hidden from the user and can only be activated by modifying the function call in main.py.

    bfs.py: implements the solve function which takes in a start state and goal state and solves the puzzle using a BFS approach. Relies on utils.py for helper classes and functions. 

    dfs.py: implements the solve function which takes in a start state and goal state and solves the puzzle using a DFS approach. Relies on utils.py for helper classes and functions. 

    dijkstra.py: implements the solve function which takes in a start state and goal state and solves the puzzle using a Dijkstra's algorithm approach. Relies on utils.py for helper classes and functions. 

    utils.py: implements several helper functions used by the solving algorithms. The biggest feature is the Step class, which is used by the algorithms to store the state of the puzzle in any given move as well as back-links to the parent, and the cost of the move.