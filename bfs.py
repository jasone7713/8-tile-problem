import utils

#solve using bfs approach
def solve(start, goal):
    cost = 0
    if utils.is_equal(start, goal):
        return cost, []
    
    visited_steps = []
    steps = []
    queue = []
    #first = utils.step(start)
    queue.append(utils.step(start))
    count = 1
    
    while queue:
        curr = queue.pop(0)
        cost += 1
        if utils.is_equal(curr.state, goal):
            return cost, utils.get_step_list(curr)
        else:
            #if utils.is_visited(curr.state, visited_steps):
                #continue
            visited_steps.append(curr)
            moves = curr.find_moves(visited_steps)
            for i in range(len(moves)):
                move = moves[i]
                temp = utils.step(move, curr)
                queue.append(temp)

    return -1, []