# Cross_Over Function

def cross_over(population_list , n , ps):
    for i in range(0 , ps , 2):
    # We produce 2 children from each family
        child1 = population_list[i][:n//2]+population_list[i+1][n//2:n]+ [None] # The last column [None] is our scores section
        child2 = population_list[i+1][:n//2]+population_list[i][n//2:n]+ [None] # The last column [None] is our scores section
        population_list.append(child1)
        population_list.append(child2)
    return population_list