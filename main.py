from random import randint

def initial_population():
    population = []
    for i in range(0,5):
        sentence = ""
        for k in range(0,30):
            ran = randint(0,1)
            sentence = sentence + str(ran)
        population.append(sentence)
    print(population)
    return population

def eval_fitness(pop):
    list = []
    for s in pop:
        fit = 0
        for n in s:
            fit = fit + int(n)
        fit = s.count('1')
        list.append(fit)
    return list

def sort_population(i):
    return i[1]

def select_best(pop,fit):
    list = []
    output = []
    for n in range(0,len(pop)):
        list.append([pop[n],fit[n]])

    list.sort(key = sort_population,reverse= True)

    for k in list:
        output.append(k[0])
    print(output[0:3])

    return output[0:3]

def crossover():

population = initial_population()
fit = eval_fitness(population)
select_best(population,fit)


