import utils

#solve using bfs approach
def solve(start, goal):
    cost = 0
    if utils.is_equal(start, goal):
        return cost, []
    
    visited_steps = []
    steps = []
    queue = []
    queue.append(utils.step(start))
    count = 1
    
    while queue:
        curr = queue.pop(0)
        if utils.is_equal(curr.state, goal):
            #returns count, step_list as a tuple
            return utils.get_step_list(curr)
        else:
            utils.insert_matrix(curr, visited_steps)
            moves = curr.find_moves(visited_steps)
            for i in range(len(moves)):
                move = moves[i]
                temp = utils.step(move, parent=curr)
                queue.append(temp)

    return -1, []