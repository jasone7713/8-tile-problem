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
    #get input file if provided, or use default
    input = 'input.txt'
    if len(sys.argv) > 1:
        input = sys.argv[1]

    file = open(input)
    start = read_matrix(file)
    goal = [
        [1, 2, 3], 
        [8, 0, 4], 
        [7, 6, 5]
    ]
    solver.solve(start, goal, 'BFS')

if __name__ == "__main__":
    main()