from project_code.fileWorker import retrieve_students
import random
import numpy as np
import matplotlib.pyplot as plt
from project_code.data import normalize_student_data, separate_normalized_students, get_measures, separate_and_normalize_students
from project_code.perceptron import Perceptron
from project_code.graphlib import plot_normalized_data, plot_animated_data, find_intercepts_for_line

from project_code.display import *
import random

# Retrieve the student data from a file
students = retrieve_students('./data.txt')
# Generate a normalized list of student data
student_list = normalize_student_data(students)
# Generate a list based solely on heights of the students
student_height_list = [[x[0],x[2]] for x in student_list]

def displayPerceptron(ratio=0.75, activation="hard", alpha=0.1, iterations=1000, dimensions=1, weights=None):
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
			scenario = "Scenario B: No Test, Height x Weight"
			student_train = student_height_list
		if dimensions == 1:
			scenario = "Scenario A: No Test, Height Only,"
			student_train = student_list
		student_test = []
		results = p.train(student_train, weights=weights, activation=activation)
		male_students_test, female_students_test = separate_normalized_students(student_train,gender_idx=dimensions)
	else:
		if dimensions == 1:
			scenario = "Scenario A: Height Only, "
			train_val = int(len(student_height_list)*ratio)
			student_train = student_height_list[0:train_val]
			student_test = student_height_list[train_val:len(student_height_list)]
		if dimensions == 2:
			scenario = "Scenario B: Height x Weight, "
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

	if dimensions == 1:
		# Get the intercept
		mod_weights = results[-1][1]
		y_int = -(mod_weights[0]/mod_weights[1])
		males_measure = [[i,x[0],x[1]] for i,x in enumerate(male_students_test)]
		females_measure = [[i,x[0],x[1]] for i,x in enumerate(female_students_test)]
		measures = get_measures(males_measure, females_measure, intercept=y_int)
	if dimensions == 2:
		# Get the intercept
		x_int, y_int = find_intercepts_for_line(results[-1][1])
		slope = (x_int[1] - y_int[1])/(x_int[0] - y_int[0])
		measures = get_measures(male_students_test, female_students_test, slope=slope, intercept=y_int[0])







