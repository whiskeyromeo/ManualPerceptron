from project_code.fileWorker import retrieve_students, write_weights_to_file
import random
import numpy as np
import matplotlib.pyplot as plt
from project_code.data import normalize_student_data, separate_normalized_students, get_measures, separate_and_normalize_students, shuffle_students
from project_code.perceptron import Perceptron
from project_code.graphlib import plot_normalized_data, plot_animated_data, find_intercepts_for_line

from project_code.display import *
import random


# # Retrieve the student data from a file
# students = retrieve_students('./data.txt')
# # Generate a normalized list of student data
# student_list = normalize_student_data(students)
# # Generate a list based solely on heights of the students
# student_height_list = [[x[0],x[2]] for x in student_list]

def displayPerceptron(student_list, ratio=0.75, activation="hard", alpha=0.1, iterations=1000, dimensions=1, weights=None):
	if ratio > 1.0 or ratio < 0.0:
		raise Exception("Ratio of Train/Test must be between 0 and 1 inclusive.")
	activation=activation.lower()
	# Create the perceptron based on iterations and learning rate
	p = Perceptron(ite=iterations, alpha=alpha)
	if weights is None:
		weights = [random.random() for i in range(dimensions+1)]
	if len(weights) != (dimensions+1):
		raise Exception("The number of weights must be the number of dimensions + 1 (for bias)") 
	if ratio == 1.0:	
		if dimensions == 2:
			scenario = "1 Dimensions: No Test, Height x Weight"
			student_train = student_list
		if dimensions == 1:
			scenario = "1 Dimensions: No Test, Height Only,"
			student_train = student_list
		student_test = []
		results = p.train(student_train, weights=weights, activation=activation)
		male_students_test, female_students_test = separate_normalized_students(student_train,gender_idx=dimensions)
	else:
		if dimensions == 1:
			scenario = "1 Dimensions: Height Only, "
			train_val = int(len(student_list)*ratio)
			student_train = student_list[0:train_val]
			student_test = student_list[train_val:len(student_list)]
		if dimensions == 2:
			scenario = "2 Dimensions: Height x Weight, "
			train_val = int(len(student_list)*ratio)
			student_train = student_list[0:train_val]
			student_test = student_list[train_val:len(student_list)]
		# Get the values for plotting
		male_students_test, female_students_test = separate_normalized_students(student_test,gender_idx=dimensions)
		# Train the Perceptron and obtain the resulting weights
		results = p.train(student_train, weights=weights, activation=activation)
	
	train_test = "{} Train:{} Test, ".format(ratio, (1-ratio))
	title = "{} {} {} activation, Alpha={}".format(scenario, train_test, activation, alpha)
	plot_normalized_data(title, male_students_test, female_students_test, results, dimensions=dimensions)
	train_ratio = int(ratio*100)
	test_ratio = 100-train_ratio
	if dimensions == 1:
		# Get the intercept
		mod_weights = results[-1][1]
		y_int = -(mod_weights[0]/mod_weights[1])
		males_measure = [[i,x[0],x[1]] for i,x in enumerate(male_students_test)]
		females_measure = [[i,x[0],x[1]] for i,x in enumerate(female_students_test)]
		measures = get_measures(males_measure, females_measure, intercept=y_int)
		write_weights_to_file(mod_weights, "1Dim_{}train_{}test_{}.txt".format(train_ratio,test_ratio, activation))
	if dimensions == 2:
		# Get the intercept
		mod_weights = results[-1][1]
		x_int, y_int = find_intercepts_for_line(mod_weights)
		slope = (x_int[1] - y_int[1])/(x_int[0] - y_int[0])
		measures = get_measures(male_students_test, female_students_test, slope=slope, intercept=y_int[0])
		write_weights_to_file(mod_weights, "2Dim_{}train_{}test_{}.txt".format(train_ratio, test_ratio, activation))

def runAllSplits(alpha=0.1,iterations=10000,dimensions=1,weights=None, shuffle=False, subset=1.0):
	# Retrieve the student data from a file
	students = retrieve_students('./data.txt')
	# Allow option to choose a subset of the data for analysis
	if subset < 0.001 or subset > 1.0:
		raise Exception("Subset of data to be analyzed must be greater than 0 and 1")
	if subset < 1.0:
		subrange = int(len(students)*subset)
		students = students[0:subrange]
	# Generate a normalized list of student data
	student_list = normalize_student_data(students)
	student_height_list = [[x[0],x[2]] for x in student_list]
	if shuffle==True:
		if dimensions == 1:
			student_list = shuffle_students(student_height_list, dimensions)
		if dimensions == 2:
			student_list = shuffle_students(student_list, dimensions)
	print("Running Hard Splits for {} Dimensions".format(dimensions))
	print("Running 75/25 split")
	displayPerceptron(student_list, ratio=0.75, activation="hard", alpha=alpha, iterations=iterations, dimensions=dimensions,weights=weights)
	print("\nRunning 50/50 split")
	displayPerceptron(student_list, ratio=0.50, activation="hard", alpha=alpha, iterations=iterations, dimensions=dimensions,weights=weights)
	print("\nRunning 25/75 split")
	displayPerceptron(student_list, ratio=0.25, activation="hard", alpha=alpha, iterations=iterations, dimensions=dimensions,weights=weights)

	print("\n\nRunning Soft Splits for {} Dimensions".format(dimensions))
	print("Running 75/25 split")
	displayPerceptron(student_list, ratio=0.75, activation="soft", alpha=alpha, iterations=iterations, dimensions=dimensions,weights=weights)
	print("\nRunning 50/50 split")
	displayPerceptron(student_list, ratio=0.50, activation="soft", alpha=alpha, iterations=iterations, dimensions=dimensions,weights=weights)
	print("\nRunning 25/75 split")
	displayPerceptron(student_list, ratio=0.25, activation="soft", alpha=alpha, iterations=iterations, dimensions=dimensions,weights=weights)



def runSplits(activation="hard", alpha=0.1,iterations=10000,dimensions=1,weights=None, shuffle=False, subset=1.0):
	# Retrieve the student data from a file
	students = retrieve_students('./data.txt')
	# Allow option to choose a subset of the data for analysis
	if subset < 0.001 or subset > 1.0:
		raise Exception("Subset of data to be analyzed must be greater than 0 and 1")
	if subset < 1.0:
		subrange = int(len(students)*subset)
		students = students[0:subrange]
	# Generate a normalized list of student data
	student_list = normalize_student_data(students)
	student_height_list = [[x[0],x[2]] for x in student_list]
	if shuffle==True:
		if dimensions == 1:
			student_list = shuffle_students(student_height_list, dimensions)
		if dimensions == 2:
			student_list = shuffle_students(student_list, dimensions)
		#random.shuffle(student_list)
	# Generate a list based solely on heights of the students
	print("Running 75/25 split")
	displayPerceptron(student_list, ratio=0.75, activation=activation, alpha=alpha, iterations=iterations, dimensions=dimensions,weights=weights)
	print("\nRunning 50/50 split")
	displayPerceptron(student_list, ratio=0.50, activation=activation, alpha=alpha, iterations=iterations, dimensions=dimensions,weights=weights)
	print("\nRunning 25/75 split")
	displayPerceptron(student_list, ratio=0.25, activation=activation, alpha=alpha, iterations=iterations, dimensions=dimensions,weights=weights)



