from numba import  jit
from random import randint as rnd
import numpy as np

@jit
# Mutation Function
def mutation_optimized(population_list , n , ps , mr):
    choosen_ones = np.random.randint(ps,ps*2 , size=(1 , int(ps*mr)))
    n_1 = n-1
    for i in choosen_ones[0]:
        cell = rnd(0 , n_1)
        val = rnd(0 , n_1)
        population_list[i][cell] = val
    return population_list