from methods.least_cost import find_lowest_cost_cell
from methods.least_cost import calculate_cost

def solve_unbalanced_transportation_problem(cost_matrix, supply, demand):
  plan = [[0 for j in range(len(demand))] for i in range(len(supply))]
  while sum(supply) > 0 and sum(demand) > 0:
    i, j = find_lowest_cost_cell(cost_matrix, supply, demand)
    min_supply = min(supply[i], demand[j])
    plan[i][j] = min_supply
    supply[i] -= min_supply
    demand[j] -= min_supply
  return plan, calculate_cost(cost_matrix, plan, demand)

## example
cost_matrix = [[10, 15, 20], [5, 10, 15], [20, 10, 5]]
supply = [20, 30, 10]
demand = [30, 20, 30]
plan, total_cost = solve_unbalanced_transportation_problem(cost_matrix, supply, demand)
print(plan)
print(total_cost)

