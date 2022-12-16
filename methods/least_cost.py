def calculate_cost(cost_matrix, supply, demand):
  total_cost = 0
  for i in range(len(supply)):
    for j in range(len(demand)):
      total_cost += cost_matrix[i][j] * supply[i][j]
  return total_cost

def find_lowest_cost_cell(cost_matrix, supply, demand):
  min_cost = float("inf")
  min_i = -1
  min_j = -1
  for i in range(len(supply)):
    for j in range(len(demand)):
      if supply[i] > 0 and demand[j] > 0:
        if cost_matrix[i][j] < min_cost:
          min_cost = cost_matrix[i][j]
          min_i = i
          min_j = j
  return min_i, min_j

