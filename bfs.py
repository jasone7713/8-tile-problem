import utils

#solve using bfs approach
def solve(start, goal):
    cost = 0
    if utils.is_equal(start, goal):
        return cost, []
    
    #sorted list of utils.Step objects to store visited puzzle states
    visited_steps = []

    #standard list to be used as a queue in BFS logic
    queue = []
    queue.append(utils.step(start))
    
    #perform BFS on queue until goal state is found
    while queue:
        curr = queue.pop(0)
        if utils.is_equal(curr.state, goal):
            #returns count, step_list as a tuple
            return utils.get_step_list(curr)
        else:
            #insert matrix into visited steps (function handles sorting)
            utils.insert_matrix(curr, visited_steps)

            #iterate through possible moves from given state and add undiscovered to queue
            moves = curr.find_moves(visited_steps)
            for i in range(len(moves)):
                move = moves[i]
                temp = utils.step(move, parent=curr)
                queue.append(temp)

    #return default if BFS fails
    return -1, []