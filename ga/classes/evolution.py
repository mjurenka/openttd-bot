import random
import collections
import gc
from calendar import monthrange
from datetime import date
from copy import deepcopy

from classes.chromosome import Chromosome

class Evolution(object):
    """docstring for Evolution"""

    # CONSTANTS
    PAR_MAX = 1500
    PAR_MIN = -500

    POPULATION_SIZE = 50
    SELECT_BEST_COUNT = 20
    SELECT_WORST_COUNT = 1

    CROSSBREED_SPLIT_COUNT = 5
    MUTATE_PERCENTAGE = 5


    # CLASS VARIABLES
    parameterCount = 0;
    counter = 0
    population = []
    solutions = []
    evalFunction = None

    def __init__(self, parameterCount, evaluationFunction):
        self.parameterCount = parameterCount
        self.evalFunction = evaluationFunction

    def evolveSingle(self):
        # create new population if none present
        self.createFirstPopulation()

        oldPopulation = []
        newPopulation = []
        best = []

        # add old population
        oldPopulation.extend(self.population)

        # selection
        #   evaluate
        oldPopulation = self.evaluateAndSort(oldPopulation)
        #   select best
        best.extend(deepcopy(oldPopulation[0:self.SELECT_BEST_COUNT]))

        # genetic operators
        #   crossover to make size of population
        newPopulation.extend(self.crossbreedGeneration(best, self.POPULATION_SIZE))

        #   mutate new population
        newPopulation = self.mutateGeneration(newPopulation, self.MUTATE_PERCENTAGE)

        # generate new individuals
        newPopulation.extend(self.generatePopulation(self.INITIAL_POPULATION_SIZE - len(self.population)))

        # # evaluate and sort

        # select best
        best = []
        best.extend(deepcopy(newPopulation[0:self.SELECT_BEST_COUNT]))

        # genetic operators
        # mutate
        newPopulation.extend(self.mutate(best, 10, 1))

        # # crossbreed
        newPopulation.extend(self.crossbreed(best, newPopulation, 5))

        # evaluate
        newPopulation = self.evaluateAndSort(newPopulation)

        # substitute
        self.population = []
        self.population = newPopulation[0 : self.TAKEOVER_POPULATION_SIZE]

    def createFirstPopulation(self):
        if(len(self.population) == 0):
            self.population.extend(self.generatePopulation(self.POPULATION_SIZE))

    def evolve(self, evolutionCount):
        for i in range(evolutionCount):
            self.evolveSingle()
            self.exportPopulation()
            self.counter += 1

    def getBestSolution(self, index):
        if(len(self.population) == 0):
            return Chromosome()
        else:
            return self.population[index]

    def generateSingle(self):
        single = Chromosome([0] * self.parameterCount)
        for i in range(self.parameterCount):
        	randomNumber = random.randint(0, 500)
        	single.changeGene(randomNumber, i)

        return single

    def generatePopulation(self, populationSize):
        newPopulation = []
        for i in range(populationSize):
            single = self.generateSingle()
            newPopulation.append(single)

        return newPopulation

    def evaluate(self, chromosome):
        return self.evalFunction(chromosome)

    def evaluateAndSort(self, population):
    	return sorted(population, key=lambda Ch: Ch.setFitness(self.evaluate(Ch)), reverse=True)

    def mutateGeneration(self, population, mutationPercentage):
        for i in range(len(population)):
            chance = random.randint(0, 100)
            if(chance > mutationPercentage):
                self.mutateSingle(population[i])

        return population

    def mutateSingle(self, parent):
        for i in range(int(len(population) * percentage)):
            # choose random chromosome
            randomChromo = random.randint(0, len(population) - 1)
            chromo = deepcopy(population[randomChromo])

            # choose 2 different spots
            while True:
                place1 = random.randint(0, self.parameterCount - 1)
                place2 = random.randint(0, self.parameterCount - 1)
                if(place1 != place2):
                    break

            # swap
            temp = chromo.getGene(place1)
            chromo.changeGene(chromo.getGene(place2), place1)
            chromo.changeGene(temp, place2)

            # add to population
            newPopulation.append(chromo)
        return newPopulation

    def crossbreedGeneration(self, population, childCount):
        children = []
        for i in range(childCount):
            parent1ID = random.randint(0, len(population));
            parent2ID = random.randint(0, len(population));
            while(parent1ID == parent2ID):
               parent2ID = random.randint(0, len(population));

            children.append(self.crossbreedSingle(population[parent1ID], population[parent2ID], self.CROSSBREED_SPLIT_COUNT))

        return children

    def crossbreedSingle(self, parent1, parent2, splitCount):
        child = new Chromosome()
        splitMask = []

        splitMask = [random.randint(0, parent1.getSize() - 1) for _ in range(splitCount)].sort()

        placePointer = 0;
        for index, splitPlace in enumerate(splitMask):
            if(index % 2 == 0):
                child.addGeneSequence(parent1.chromo[placePointer:splitPlace])
            else:
                child.addGeneSequence(parent2.chromo[placePointer:splitPlace])

            placePointer = splitPlace
        return child

        # for individual in bestIndividuals:
        # 	for i in range(int(len(population) * breedPercentage)):
	            
	       #      randomIndividual = random.randint(0, len(population) - 1)
	       #      randomIndividual = population[randomIndividual]

	       #      child = Chromosome([0] * self.parameterCount)

	       #      for index, value in enumerate(splitMask):
	       #          gene = None
	       #          if(value == 0):
	       #              gene = individual.getGene(index)
	       #          else:
	       #              gene = randomIndividual.getGene(index)

	       #          child.changeGene(gene, index)
	       #      newPopulation.append(child)
        # return newPopulation

    def fuseChromos(firstCH, secondCH, fusionPosition):
        fusedChromo = Chromosome()
        for i in range(firstCH.getSize()):
            if(i < fusionPosition):
                fusedChromo.addGene(firstCH.getGene(i))
            else:
                fusedChromo.addGene(secondCH.getGene(i))

        return fusedChromo

    def exportPopulation(self):
        f = open('lastState.txt', 'a')
        f.write(str(self.counter) + ":")
        for chromo in self.population:
            f.write(chromo.toString() + "\n")
        f.close

    def loadPopulation(self):
        f = open('lastState.txt', 'r')
        for line in f:
            single = Chromosome(len(line))
            single.fromString(line)
            self.population.append(single)
