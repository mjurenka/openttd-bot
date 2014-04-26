import subprocess
import os
import shlex

class Fitness(object):
	"""docstring for """
	def __init__(self):
		super(Fitness, self).__init__()

	def evaluate(self, chromo):
		fitness = subprocess.call(['java', '-jar', 'scbot.jar', chromo.toString()])
		print("Fitness: " + str(fitness))
		return fitness

	def evaluateSlow(self, chromo):
		fitness = subprocess.call(['java', '-jar', 'scbot-slow.jar', chromo.toString()])
		print("Fitness: " + str(fitness))
		return fitness

