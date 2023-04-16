import utils

#solve using dfs approach (same as bfs, but different cost)
def solve(start, goal):
    cost = 0
    if utils.is_equal(start, goal):
        return cost, []
    
    visited_steps = []
    queue = []
    queue.append(utils.step(start))
    
    while queue:
        print(len(queue))
        curr = queue.pop(0)
        if utils.is_equal(curr.state, goal):
            #returns count, step_list as a tuple
            return utils.get_step_list_DIJ(curr)
        else:
            utils.insert_matrix(curr, visited_steps)
            moves, costs = curr.find_moves_and_costs(visited_steps, curr)
            for i in range(len(moves)):
                move = moves[i]
                cost = costs[i]
                temp = utils.step(move, cost=cost, parent=curr)
                #queue.append(temp)
                utils.insert_priority(temp, queue)

    return -1, []