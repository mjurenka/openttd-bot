from classes.evolution import Evolution
from classes.fitness import Fitness
from classes.chromosome import Chromosome

switcher = 1

def testSlow():
	string = "40,80,80,100,40,100,50,400,720,1000,15,4,350,50,17,85,100,50,400,720,100,60,85,17,20,100,60,50,150,720,400,250,64,10,85,17,10,35,75,75,100,100,1000,200,50,400"
	chromo = Chromosome()
	chromo.fromString(string)
	fitness.evaluateSlow(chromo)

if  __name__ =='__main__':
	fitness = Fitness()

	if(switcher == 0):
		evolution = Evolution(69, fitness.evaluate)
		evolution.evolve(10)

		best = evolution.getBestSolution(0)
		print(best.toString())
		print(best.getFitness())
	else:
		testSlow()

