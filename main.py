from random import randint

# Genetic Algorithm
def initial_population():
    population = []
    for i in range(0,5):
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
        for n in s:
            fit = fit + int(n)
        fit = s.count('1')
        list.append(fit)
    return list

# sort population
def sort_population(i):
    return i[1]

# select best fit
def select_best(pop,fit):
    list = []
    output = []
    top = 3
    for n in range(0,len(pop)):
        list.append([pop[n],fit[n]])

    list.sort(key = sort_population,reverse= True)

    for k in list:
        output.append(k[0])
    print("Top", top,"\n",output[0:top])
    return output[0:3]

# Crossover Method
def crossover(s1,s2, point):
    print("\nCrossover Opperations:\nParents")
    c1 = s1[0:point] + s2[point:len(s1)]
    c2 = s2[0:point] + s1[point:len(s1)]
    print(s1, s2)
    print("Children")
    print(c1,c2)
    return

# Methods used by Algorithm
population = initial_population()
fit = eval_fitness(population)
best = select_best(population,fit)
cross = crossover(best[0],best[1],randint(0,len(best[0])))


