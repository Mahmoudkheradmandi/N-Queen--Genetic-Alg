from numba import  jit

@jit  # It makes the function run at the CPU level and increases the speed
def cross_over_optimized(population_list , n , ps):
    half = n//2
    for i in range(0 , ps , 2): 
        # create child 1 
        population_list[ps+i][:half] = population_list[i][:half]
        population_list[ps+i][half:n] = population_list[i+1][half:n]
        # create child 2
        population_list[ps+i+1][:half] = population_list[i+1][:half]
        population_list[ps+i+1][half:n] = population_list[i][half:n]

    return  population_list