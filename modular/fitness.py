# Fitness Function

def fitness(population_list , n):
    length = len(population_list)
    for i in range(length):
        rate = 0
        for j in range(n):
            for k in range(j+1 , n):
                # Column
                if population_list[i][j] == population_list[i][k]:
                    rate+=1
                # diogonal
                if abs(j-k) == abs(population_list[i][j] - population_list[i][k]):
                    rate+=1
        population_list[i][-1] = rate
    return population_list