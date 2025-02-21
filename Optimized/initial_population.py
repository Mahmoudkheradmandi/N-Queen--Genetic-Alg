import numpy as np


# Initial population Function
def init_population_optimized(n , ps):
    arr  = np.random.randint(n , size=(ps*2,n+1))
    arr[:,-1] = 0 # for create Point 
    return arr

