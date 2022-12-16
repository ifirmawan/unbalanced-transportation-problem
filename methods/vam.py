def vogels_approximation_method(supply, demand, costs):
    # Step 1: Create a list of the differences between the transportation costs
    # for each source
    num_sources = len(supply)
    num_destinations = len(demand)
    differences = [[0 for j in range(num_destinations)] for i in range(num_sources)]
    for i in range(num_sources):
        for j in range(num_destinations):
            if j < num_destinations - 1:
                differences[i][j] = costs[i][j+1] - costs[i][j]
            else:
                differences[i][j] = -float('inf')
    
    # Step 2: Initialize the transportation table with zeros
    table = [[0 for j in range(num_destinations)] for i in range(num_sources)]
    
    # Step 3: While there is still supply or demand to be met, repeat the following:
    while sum(supply) > 0 and sum(demand) > 0:
        # Step 3a: Find the source and destination with the largest positive difference
        max_difference = -float('inf')
        max_source = None
        max_destination = None
        for i in range(num_sources):
            for j in range(num_destinations):
                if differences[i][j] > max_difference:
                    max_difference = differences[i][j]
                    max_source = i
                    max_destination = j
        
        # Step 3b: Allocate as much as possible to the chosen source and destination
        allocation = min(supply[max_source], demand[max_destination])
        table[max_source][max_destination] += allocation
        supply[max_source] -= allocation
        demand[max_destination] -= allocation
        
        # Step 3c: Update the differences for the chosen source and destination
        for j in range(num_destinations):
            if j < num_destinations - 1:
                differences[max_source][j] = costs[max_source][j+1] - costs[max_source][j]
            else:
                differences[max_source][j] = -float('inf')
        for i in range(num_sources):
            differences[i][max_destination] = costs[i][max_destination+1] - costs[i][max_destination]
    
    # Step 4: Return the initial feasible solution
    return table

