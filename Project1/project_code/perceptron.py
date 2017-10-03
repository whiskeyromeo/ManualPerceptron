'''
	__author__ = "Will Russell"
'''

import numpy as np
import pandas as pd

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
import random


class Perceptron:
	def __init__(self, alpha, w_n):
		self.alpha = alpha
		self.weights = []
		for x in range(0, w_n):
			self.weights.append(random.random()*2-1)

	# this is the net function
	def feed_forward(self, inputs):
		sum = 0
		for x in range(0, len(self.weights)):
			# notice the weights are not updated
			sum += self.weights[x] * inputs[x]
		return self.activate(sum)

	def activate(self, num):
		if num > 0:
			return 1
		return 0

	def train(self, inputs, desired_output):
		guess = self.feed_forward(inputs)
		error = abs(desired_output - guess)
		print("desired_output: {}, guess: {}, error: {}".format(desired_output, guess,error))
		for x in range(0, len(self.weights)):
			self.weights[x] += error*inputs[x]*self.alpha


class Trainer:
	def __init__(self):
		self.perceptron = Perceptron(0.01, 3)
	# This is not correct --> This function should not be hardcoded, objective is to arrive 
	# at the function which acts as the linear separator
	'''
		The net function, weights should be modified over time
	'''
	def f(self, x):
		return -0.0127*x + 4.882

	'''
		training function for the perceptron, based
		on initial weights from project 1
	'''
	def train(self):
		print("training")
		# Need to use the data from sep_line_a and sep_line_b here 
		
		for x in range(0, 1000):
			x_coord = random.random()*500-250
			y_coord = random.random()*500-250
			line_y = self.f(x_coord)
			if y_coord > line_y:
				answer = 1
				self.perceptron.train([x_coord, y_coord,1], answer)
			else:
				answer = 0
				self.perceptron.train([x_coord, y_coord,0], answer)
		return self.perceptron


trainer = Trainer()
#p = trainer.train()








###############


# Need to pull in the amoount of samples being used
# for each set.
# Should be number of rows from data.txt
# sample_size = 120

# class Perceptron(object):
# 	def __init__(self, ite=1000, num_patterns=sample_size, alpha=0.1):
# 		self.ite = ite 		# number of iterations
# 		self.dim = dim		# number of dimensions
# 		self.alpha = alpha	# learning rate

# 	'''
# 	'''
# 	def f(self, x):
# 		return -0.0127*x + 4.882

# 	'''
# 		Should represent the hard activation function
# 	'''
# 	def sign(self, num):
# 		if num > 0:
# 			return 1
# 		return 0

# 	'''
# 		Should represent the function used to train	
# 	'''
# 	def train(self, patterns=[[],[]], weights=[1,3,-3],dout=[-1,1]):
# 		for n in range(0, self.ite):
# 			for p in enumerate(patterns):
# 				net = 0
# 				for i in range(0, len(weights)):
# 					net = net + weights[i] * patterns[p][i]
# 				guess = sign(net)
# 				err = abs(dout[p] - guess)















###############






# class Perceptron(object):
# 	def __init__(self,eta=0.02,t=1000):
# 		self.eta = eta
# 		self.t = t

# 	def train(self, X, y, w_):
# 		self.w_ = w_
# 		self.errors_ = []

# 		for _ in range(self.t):
# 			errors = 0
# 			for xi, target in zip(X, y):
# 				update = self.eta * (target - self.predict(xi))
# 				self.w_[1:] += update * xi
# 				self.w_[0] += update
# 				errors += int(update != 0.0)
# 			self.errors_.append(errors)
# 		return self

# 	def net(self, X):
# 		new_weight = np.dot(X, self.w_[1:]) + self.w_[0]
# 		print(new_weight)
# 		return new_weight

# 	def predict(self, X):
# 		return np.where(self.net(X) >= 0.0, 1, 0)


# import matplotlib.pyplot as plt
# from mlxtend.plotting import plot_decision_regions


# df = pd.read_csv("./data.txt")
# X = df.iloc[0:500,[1,0]].values
# y = df.iloc[0:500, 2].values
# w_ = pd.read_csv("./sep_line_b.txt", header=None).values.flatten()

# ppn = Perceptron(eta=0.02, t=1000)
# ppn.train(X,y,w_)
# print('Weights: %s' % ppn.w_)
# plot_decision_regions(X, y, clf=ppn)
# plt.show()

# plt.plot(range(1, len(ppn.errors_)+1), ppn.errors_, marker='o')
# plt.xlabel('Iterations')
# plt.ylabel('Misclassifications')
# plt.show()



#df2 = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)



