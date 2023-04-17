import utils

#solve using dfs approach (same as bfs, but different cost)
def solve(start, goal):
    cost = 0
    if utils.is_equal(start, goal):
        return cost, []
    
    #init a visited steps list and a priority queue for dijkstra's
    visited_steps = []
    queue = []
    queue.append(utils.step(state=start, parent=None, cost=0))
    
    while queue:
        curr = queue.pop(0)
        if utils.is_equal(curr.state, goal):
            #returns count, step_list as a tuple
            return utils.get_step_list_DIJ(curr)
        else:
            #insert curr into the list of visited states and generate a list of possible moves
            utils.insert_matrix(curr, visited_steps)
            moves, costs = curr.find_moves_and_costs(visited_steps, curr)

            #iterate through possible moves and the cost of each. The cost of moves[i] = costs[i]
            for i in range(len(moves)):
                move = moves[i]
                cost = costs[i]
                temp = utils.step(move, cost=cost, parent=curr)
                #insert into queue sorted by state.cost from lowest to highest
                utils.insert_priority(temp, queue)

    #return default if dijkstra's fails to find a solution 
    return -1, []