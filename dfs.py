import utils
import sys
#sys.setrecursionlimit(10000)   #uncomment this if you are using the recursive version

#solve using dfs -- DEPRECATED - THE RECURSION STACK WAS TOO LARGE, USE solve_iterative INSTEAD
def solve(start, goal):
    if utils.is_equal(start, goal):
        return 0, []
    
    #holds sorted list of visited puzzle states
    visited_steps = []
    s = utils.step(start)
    utils.insert_matrix(s, visited_steps)
    
    #recurse for goal state using dgs
    test = recurse(s, goal, visited_steps)
    return test
    
#helper function for DFS to recurse
def recurse(current, goal, visited_steps):
    #goal state found, return
    if utils.is_equal(current.state, goal):
        return utils.get_step_list(current)
    
    #find moves and recurse on the undiscovered ones
    moves = current.find_moves(visited_steps)
    for move in moves:
        child = utils.step(move, current)
        utils.insert_matrix(child, visited_steps)
        found = recurse(child, goal, visited_steps)
        if found is not None:
            return found


#solve using dfs approach
def solve_iterative(start, goal):
    cost = 0
    if utils.is_equal(start, goal):
        return cost, [utils.step(start)]
    
    #sorted list of visited puzzle states
    visited_steps = []

    #standard list behaving like a stack to perform DFS
    stack = []
    stack.append(utils.step(start))
    
    while stack:
        curr = stack.pop(0)
        if utils.is_equal(curr.state, goal):
            #returns count, step_list as a tuple
            return utils.get_step_list(curr)
        else:
            #insert into visited states and find possible moves
            utils.insert_matrix(curr, visited_steps)
            moves = curr.find_moves(visited_steps)

            #add to the stack in a top-down method to preserve the same priority of moves (left, up, right, down)
            for i in range(len(moves)-1, -1, -1):
                move = moves[i]
                temp = utils.step(move, parent=curr)
                stack.insert(0, temp)

    #return default if DFS fails
    return -1, []
