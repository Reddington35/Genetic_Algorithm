from random import randint
import statistics
# Genetic Algorithm

# Method to establish an initial Population
def initial_population():
    population = []
    for i in range(0,1000):
        sentence = ""
        for k in range(0,30):
            ran = randint(0,1)
            sentence = sentence + str(ran)
        population.append(sentence)
    print("\nInitial Population:\n",population)
    return population

# Evaluate fitness
def eval_fitness(pop):
    list = []
    for s in pop:
        fit = 0
        fit = s.count('1')
        list.append(fit)
    print("Average fitness over the generation: ", statistics.mean(list))
    return list

# sort population
def sort_population(i):
    return i[1]

# select best fit
def select_best(pop,fit):
    list = []
    output = []
    top = 100
    for n in range(0,len(pop)):
        list.append([pop[n],fit[n]])

    list.sort(key = sort_population,reverse= True)

    for k in list:
        output.append(k[0])
    # print("Top", top,"\n",output[0:top])
    return output[0:top]

# Crossover Method
def crossover(s1,s2, point):
    # print("\nCrossover Operations:\nParents")
    c1 = s1[0:point] + s2[point:len(s1)]
    c2 = s2[0:point] + s1[point:len(s1)]
    # print(s1, s2)
    # print("Children")
    # print(c1,c2)
    return c1,c2

# Mutation Method
######
def mutation(s):
    mutate = ""
    bit = randint(0,len(s)-1)
    for i in range(0,len(s)):
        if(i == bit):
            if(s[i] == '0'):
                mutate = mutate + '1'
            else:
                mutate = mutate + '0'
        else:
            mutate = mutate + s[i]
    # print("\nMutation Opperations:")
    # print("Original:          " + s)
    # print("Bit to be mutated: ", bit)
    # print("Mutated String:    "+mutate)
    return mutate

# Methods Used and number of Generations initialised
population = initial_population()
fit = eval_fitness(population)
num_generations = 0

# Loops through Generations to perform
# operations Crossover and Mutate

while max(fit) < 30:
    num_generations = num_generations + 1
    best = select_best(population,fit)

    for i in range(0,len(best)-1):
        cross = crossover(best[i],best[i+1],randint(0,len(best[0])))
        mute = mutation(cross[0])
        population.append(mute)
    fit = eval_fitness(population)


print("Solution found in: ",num_generations)



