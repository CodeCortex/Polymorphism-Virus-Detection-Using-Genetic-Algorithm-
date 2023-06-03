import random
import matplotlib.pyplot as plt


target_string = "4A59E2E67C"

# population
population_size = 100

# generations we want to run
num_generations = 800


mutation_probability = 0.01

# The fitness function, which compares a string to the target string using both


def fitness(string):
    # Subsequencing algorithm
    subsequences = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            subsequences.add(string[i:j])
    subsequence_score = len(subsequences.intersection(set(target_string)))

    # Substring algorithm
    substring_score = 0
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i:j] in target_string:
                substring_score += 1

    # Combine the two scores using a weighted average
    return (0.7 * subsequence_score + 0.3 * substring_score) / len(target_string)


# Load the population from a file of strings
with open("dataset.txt", "r") as f:
    population = [line.strip() for line in f.readlines()]

# Evolve the population for the specified number of generations
fitness_history = []
for generation in range(num_generations):

    # fitness of each member of the population
    fitnesses = [fitness(string) for string in population]

    # best string in the population and printing itts fitness
    best_string = population[fitnesses.index(max(fitnesses))]
    print(f"Generation {generation}: {best_string} ({max(fitnesses)})")
    fitness_history.append(max(fitnesses))

    # Create a new population by selecting parents based on fitness and
    # crossover and mutation
    new_population = []
    for i in range(population_size):
        parent1 = random.choices(population, weights=fitnesses)[0]
        parent2 = random.choices(population, weights=fitnesses)[0]
        child = ""
        for j in range(len(target_string)):
            if random.random() < mutation_probability:
                child += random.choice("0123456789ABCDEF")
            elif random.random() < 0.5:
                child += parent1[j]
            else:
                child += parent2[j]
        new_population.append(child)
    population = new_population


def fitnessb(best_string):

    subsequencesf = set()
    for i in range(len(best_string)):
        for j in range(i + 1, len(best_string) + 1):
            subsequencesf.add(best_string[i:j])
    subsequence_scoreb = len(subsequencesf.intersection(set(target_string)))

    substring_scoreb = 0
    for i in range(len(best_string)):
        for j in range(i + 1, len(best_string) + 1):
            if best_string[i:j] in target_string:
                substring_scoreb += 1

    return (0.7 * subsequence_scoreb + 0.3 * substring_scoreb) / len(target_string)


if (fitnessb(best_string)*100 <= 40):
    print("File status : it's a benign file ")

elif (fitnessb(best_string)*100 > 40 or fitnessb(best_string)*100 <= 65):
    print("File status : Virus with low fidelity")

else:
    print("File status : Pure Virus with high fidelity ")

print(fitnessb(best_string))


with open("final_population.txt", "w") as f:
    for string in population:
        f.write(f"{string}\n")


plt.plot(range(num_generations), fitness_history)
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.show()
