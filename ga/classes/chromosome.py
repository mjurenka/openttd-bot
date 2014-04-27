import random
import collections

class Chromosome(object):
	chromo = []
	fitness = 0
	def __init__(self, ch = []):
		self.chromo = ch

	def getSize(self):
		return len(self.chromo)

	def changeGene(self, singleGene, position):
		self.chromo[position] = singleGene

	def addGene(self, singleGene):
		self.chromo.append(singleGene)

	def addGeneSequence(self, geneSequence):
		self.chromo.extend(geneSequence)

	def getGene(self, position):
		return self.chromo[position]

	def getRandomPositionByGene(self, desiredGene):
		while True:
			randomPosition = random.randint(0, self.getSize() - 1)
			if(self.getGene(randomPosition) == desiredGene):
				return randomPosition

	def countGenes(self, needleGene):
		return self.chromo.count(needleGene)

	def equals(self, otherChromosome):
		compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
		return compare(self.chromo, otherChromosome)

	def toString(self):
		out = ''
		for i in self.chromo:
			out = out + str(i) + ','
		return out[:-1]

	def fromString(self, chString):
		self.chromo = []
		for i in chString.split(","):
			self.addGene(int(i))

	def setFitness(self, newFitness):
		self.fitness = newFitness
		return self.fitness

	def getFitness(self):
		return self.fitness

	def destroy(self):
		self.chromo = []