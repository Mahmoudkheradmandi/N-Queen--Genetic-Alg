from random import randint as rnd

# Initial population Function
def init_population(n , ps):
    population_list = []
    for i in range(ps):
        member = []
        for j in range(n):
           member.append(rnd(0 , n-1))

        population_list.append(member + [None]) # The last column [None] is our scores section
    return population_list