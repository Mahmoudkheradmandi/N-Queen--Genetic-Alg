from random import randint as rnd
from random import shuffle

# Mutation Function

def mutation(population_list , n , ps , mr):
    # In this case, the children are selected randomly
    choosen_ones = list(range(ps , ps*2)) # Inside the main list, we find the children section and add it to the new list
    shuffle(choosen_ones)
    choosen_ones = choosen_ones[:int(ps*mr)]
    for i in choosen_ones:
        cell = rnd(0 , n-1)
        val = rnd(0 , n-1)
        population_list[i][cell] = val
    return population_list