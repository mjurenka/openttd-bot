import subprocess
import os
import shlex

class Fitness(object):
	"""docstring for """
	def __init__(self):
		super(Fitness, self).__init__()

	def evaluate(self, chromo):
		temp = sum(chromo.chromo)
		# print(chromo.toString())
		# print(str(temp))
		return temp

	def evaluateSlow(self, chromo):
		temp = sum(chromo.chromo)
		# print(chromo.toString())
		return temp

