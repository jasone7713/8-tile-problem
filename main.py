import solver
import sys

#given a file read a matrix from it
def read_matrix(file):
    matrix = []
    for line in file:
        line = line.rstrip()
        s = line.split(' ')
        i = []
        for ch in s:
            i.append(int(ch))
        matrix.append(i)
    return matrix

#print out a matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()

#main function
def main():
    #check if cmd line input was passed
    if len(sys.argv) < 2:
        print('Invalid input. Please provide an input in the form of: python main.py BFS|DFS|DIJ <input_file>')
        return
    
    #get the algo from cmd line input argv[1]
    algo = 'BFS'
    algo = sys.argv[1].upper()

    #get input file if provided, or use default
    input = 'input.txt'
    if len(sys.argv) > 3:
        input = sys.argv[3]

    #open input file and read the matrix 
    file = open(input)
    start = read_matrix(file)

    #default goal matrix
    goal = [
        [1, 2, 3], 
        [8, 0, 4], 
        [7, 6, 5]
    ]

    print('Solving with the input matrix:')
    print_matrix(start)

    #call solver and pass in the algorithm type
    solver.solve(start, goal, algo)

if __name__ == "__main__":
    main()