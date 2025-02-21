from parameters import * 
from initial_population import init_population_optimized
from cross_over import cross_over_optimized
from mutation import mutation_optimized
from fitness import fitness_optimized
from presentation import show
from copy import deepcopy
import time

start = time.time()
# Primary population production
current_population = init_population_optimized(N , PS)
current_population = fitness_optimized(deepcopy(current_population) , N)
current_population = deepcopy(current_population)[deepcopy(current_population)[:,-1].argsort()]
if current_population[0][-1] == 0 :
    print('Solution is found in the initial population stage' , current_population[0])
    show(current_population[0] , N)
else :
    for i in range(EPOCH):
        current_population = cross_over_optimized(deepcopy(current_population) , N , PS)
        current_population = mutation_optimized(deepcopy(current_population) , N , PS , MR)
        current_population = fitness_optimized(deepcopy(current_population) , N)
        current_population = deepcopy(current_population)[deepcopy(current_population)[:,-1].argsort()]
        if current_population[0][-1] == 0 :
            print (i+1 ,'Solution Found' , current_population[0])
            show(current_population[0],N)
            break
        else :
            print (i+1 ,'  ==>  ' , current_population[0][-1]) # The score section displays
    else:
        print ('Sorry , we could not find you a soluution')
        
end = time.time()
print(end-start)        