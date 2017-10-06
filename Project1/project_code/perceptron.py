'''
	__author__ = "Will Russell"
'''

from math import exp
import numpy as np

'''
	This code should contain all that is required 
	to create and run the Perceptron model

	Needs to iterate until error is below e < 10^-5
		- Needs a stopping criterion

	Should also have a limit on the number of iterations
		- ni < 1000

	Use unipolar version of:
		- Hard activation function
		- Soft activation function

	Splits : 3 splits - train/test
		- 75/25
		- 50/50
		- 25/75

'''

class Perceptron:
	def __init__(self, ite=1000, alpha=0.1):
		self.ite = ite
		self.alpha = alpha

	def predict_hard(self, row, weights):
		net = weights[0] # set the net to the bias
		for i in range(len(row)-1): # for the other weights
			net += weights[i+1] * row[i] # increase the net
		if net >= 0: 
			return 1.0 #predict female
		return 0.0 #else predict male

	# This does not work
	def predict_soft(self, row, weights=[0.,0.,0.], k=3):
		net = weights[0]
		for i in range(len(row)-1):
			net += weights[i+1] * row[i]
		# Utilize the sigmoid function
		output = 1.0/(1.0 + np.exp(-net))
		return output


	#TODO: Major issue --> weights are not updating
	# First set of weights are repeated...
	def train(self, inputs, weights, activation="hard", save=False):
		evolution = []
		for i in range(0, self.ite):
			iteration = [] #keep track of values
			predictions = []
			sum_err = 0.0
			for row in inputs:
				if activation == "hard":
					guess = self.predict_hard(row, weights)
				else:
					guess = self.predict_soft(row, weights)
				predictions.append(guess)
				err = row[-1] - guess
				sum_err += err**2
				learn = self.alpha * err
				weights[0] = weights[0] + learn # Adjust the bias
				for j in range(len(row)-1): # Adjust the other weights
					weights[j+1] = weights[j+1] + learn * row[j]
			iteration.append(predictions)
			iteration.append(list(weights))
			iteration.append(sum_err)
			evolution.append(iteration)
		return evolution



#df2 = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)



