#Part-01

import random

fitness_values = []

def chromosome_creator(population_size = 5):
    chromosomes = []
    for i in range(population_size):
        stop_loss = random.randint(1, 99)
        take_profit = random.randint(1, 99)
        trade_size = random.randint(1, 99)

        chromosome = f"{stop_loss:02d}{take_profit:02d}{trade_size:02d}"

        chromosomes.append(chromosome)

    return chromosomes

def fitness_func(chromosomes,h_price,start_capital=1000):
    fitness_values.clear()
    for i in chromosomes:
        stop_ls = int(i[:2])/100
        trade_pf = int(i[2:4])/100
        trade_sz = int(i[4:6])/100

        capital = start_capital


        for price in h_price:
            trade_amount = start_capital * trade_sz

            if price < (-stop_ls * 100):
                profit_ls = -trade_amount * stop_ls
            elif price > (trade_pf * 100):
                profit_ls = trade_amount * trade_pf
            else:
                profit_ls = trade_amount * (price/100)

            capital += profit_ls
        final_fitness = capital - start_capital
        fitness_values.append(round(final_fitness, 2))

    return fitness_values

def random_parents(chromosomes):
    parents = random.sample(chromosomes,2)
    return parents


def crossover(parent1,parent2):
    x = str(parent1)
    y = str(parent2)
    if len(x) != len(y):
        print("Parent chromosomes should have same length")

    temp = random.randint(1, len(x)-1)
    # print("Random idx of parents:",temp)
    child_1 = x[:temp] + y[temp:]
    child_2 = y[:temp] + x[temp:]

    return child_1, child_2


def mutation(child_1,child_2):
    child1_len = len(child_1)

    mut_point = random.randint(0, child1_len-2)

    child1_seg = child_1[mut_point:mut_point+2]
    child2_seg = child_2[mut_point:mut_point+2]

    new_mut_val_ch1 = round(int(child1_seg)*0.05)
    new_mut_val_ch2 = round(int(child2_seg)*0.05)

    mut_opt = random.randint(0,1)

    if mut_opt==0:
        new_seg_child1 = int(child1_seg) - new_mut_val_ch1
    else:
        new_seg_child1 = int(child1_seg) + new_mut_val_ch1

    if mut_opt==1:
        new_seg_child2 = int(child2_seg) - new_mut_val_ch2
    else:
        new_seg_child2 = int(child2_seg) + new_mut_val_ch2

    new_seg_child1 = max(0, min(99, new_seg_child1))
    new_seg_child2 = max(0, min(99, new_seg_child2))

    new_seg_child1 = f"{new_seg_child1:02d}"
    new_seg_child2 = f"{new_seg_child2:02d}"

    mutated_child1 = child_1[:mut_point] + new_seg_child1 + child_1[mut_point + 2:]
    mutated_child2 = child_2[:mut_point] + new_seg_child2 + child_2[mut_point + 2:]

    return mutated_child1, mutated_child2



def genetic_algorithm(h_price, population_size=4, max_gen=10, elitism_rate=0.1, mutation_rate=0.1):
    population = chromosome_creator(population_size)
    print("Initial Population:", population)

    for i in range(max_gen):
        print(f"\nGeneration {i + 1}:")

        fitness_scores = fitness_func(population, h_price)
        print("Fitness Scores:", fitness_scores)


        sorted_population = [chromosome for _, chromosome in sorted(zip(fitness_scores, population), reverse=True)]


        num_elites = int(elitism_rate * population_size)
        new_population = sorted_population[:num_elites]

        while len(new_population) < population_size:
            parent1, parent2 = random_parents(population)

            child1, child2 = crossover(parent1, parent2)

            if random.random() < mutation_rate:
                child1, child2 = mutation(child1, child2)

            new_population.append(child1)
            if len(new_population) < population_size:
                new_population.append(child2)

        population = new_population
        print("New Population:", population)


    best_chromosome = max(population, key=lambda x: fitness_func([x], h 
    stop_loss = int(best_chromosome[:2])
    take_profit = int(best_chromosome[2:4])
    trade_size = int(best_chromosome[4:6])

    final_profit = fitness_func([best_chromosome], h_price)[0]

    return {
        "best_strategy": {
            "stop_loss": stop_loss,
            "take_profit": take_profit,
            "trade_size": trade_size,
        },
        "final_profit": final_profit,
    }


# Driver Code-1
h_price = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]
result = genetic_algorithm(h_price)
print("\nFinal Result:")
print(result)
print("-------------------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------------------------------------------------------------------

#Part-02
print("Part-02")
def two_point_crossover(parent1, parent2):

    child1, child2 = crossover(parent1, parent2)

    final_child1, final_child2 = crossover(child1, child2)
    print("\nAfter two point Crossover:")
    print("Child 1:", final_child1)
    print("Child 2:", final_child2)

    return final_child1, final_child2


# Driver code-2
population = chromosome_creator()

parent1, parent2 = random.sample(population, 2)
print("\nParent 1:", parent1)
print("Parent 2:", parent2)

final_child1, final_child2 = two_point_crossover(parent1, parent2)