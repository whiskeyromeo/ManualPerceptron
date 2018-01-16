'''
	__author__ = "Will Russell"
'''

from math import exp
import numpy as np

'''
	This code should contain all that is required 
	to create and run the Perceptron model

'''

class Perceptron:
	def __init__(self, ite=1000, alpha=0.1, epsilon=10e-5):
		self.ite = ite
		self.alpha = alpha
		self.epsilon  = epsilon
 

	def sigmoid_activation(self, net, k=3):
		# Utilize the sigmoid function
		output = 1.0/(1.0 + np.exp(-net))
		return output

	def tanh_activation(self, net,k=3):
		output = (2/(1+np.exp(-k*net)))-1
		return output

	def sinh_activation(self, net, k=3):
		# Utilize the sinh function
		output = (1-np.exp(-2*net))/(2*(np.exp(-net)))
		return output

	def linear_activation(self, net):
		output = net
		return output

	def train(self, inputs, weights=[0.,0.,0.], activation="linear"):
		evolution = []
		for i in range(0, self.ite):
			iteration = {} #keep track of values
			predictions = []
			desired = []
			row_err= []
			hour_list = []
			row_weights = []
			sum_err = 0.0
			for row in inputs:
				# generate the weights 
				net = weights[0]
				for j in range(len(row)-1):
					net += weights[j+1] * row[j]
				if activation == "sigmoid":
					guess = self.sigmoid_activation(net)
				elif activation == "sinh":
					guess = self.sinh_activation(net)	
				elif activation == "tanh":
					guess = self.tanh_activation(net)	
				#Just for project 3	
				elif activation == "linear":
					guess = self.linear_activation(net)

				err = row[-1] - guess 
				sum_err += abs(err)
				row_weights.append(weights)
				predictions.append(guess)
				hour_list.append(row[0])
				desired.append(row[-1])
				row_err.append(err)
				learn = self.alpha * err
				weights[0] = weights[0] + learn # Adjust the bias
				for j in range(len(row)-1): # Adjust the other weights
					weights[j+1] = weights[j+1] + learn * row[j]

			iteration["iter"] = i
			iteration["input_hour"] = hour_list
			iteration["row_weights"] = row_weights
			iteration["output"] = predictions
			iteration["desired_temp"] = desired
			iteration["row_error"] = row_err
			iteration["weights"] = list(weights)
			iteration["error"] = (round((sum_err/len(inputs))*100000.0)/100000.0)
			evolution.append(iteration)
			if((sum_err) < self.epsilon):
					print("error below epsilon")
					break

		return evolution

	# establish a prediction based off of weights generated in training
	def test(self, inputs, weights=[0.,0.]):
		return weights[1]*inputs + weights[0]

	# generate predictions for two lines, taking the mean of the points established at hour 9
	def generatePredictions(self, weight_set1, weight_set2):
		if(len(weight_set2) == 0):
			predictions = [[x, self.test(x, weight_set1)] for x in range(5,14)]
		else:
			p1_predictions = [[x, self.test(x, weight_set1)] for x in range(5,10)]
			p2_predictions = [[x, self.test(x, weight_set2)] for x in range(9,14)]
			predictions = p1_predictions + p2_predictions

		for i in range(0, len(predictions)-2):
		    if predictions[i][0] == predictions[i+1][0]:
		        predictions[i][1] = (predictions[i][1] + predictions[i+1][1])/2 
		        predictions[i+1][1] = predictions[i][1]
		pred_x = [x[0] for x in predictions]
		pred_y = [x[1] for x in predictions]
		# Poor Hack to get around having duplicate in the list
		if len(pred_y) == 10:
			del pred_y[5]
			del pred_x[5]
		return [pred_x, pred_y]


