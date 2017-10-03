'''
This code provides the primary support for the functions implemented
in the jupyter notebook

__author__ = "Will Rusell"


'''

import random
import numpy as np
from .Student import Student

'''
	Generates two normally distributed lists of students separated by gender and 
	returns the lists.
'''
def generate_random_student_data(sample_size=2000):
	male_students = []
	female_students = []

	male_weights = np.random.normal(176.1, 20.84, sample_size)
	female_weights = np.random.normal(139.89, 14.88, sample_size)

	male_heights = np.random.normal(5.8, 0.3, sample_size)
	female_heights = np.random.normal(5.2, 0.3, sample_size)

	for i in range(0,sample_size):
	    male_students.append(Student(round(male_heights[i],2,),round(male_weights[i],2),0))
	    female_students.append(Student(round(female_heights[i],2), round(female_weights[i],2),1))

	print("Number of male students : {}".format(len(male_students)))
	print("Number of female students : {}".format(len(female_students)))
	print("-----------")
	print("Sample Data")
	print("-----------")
	print("\nMale id  |   height  | weight ")
	for i in range(0,10):
		print("\t{}|\t{}|\t{}".format(i, male_students[i].height, male_students[i].weight))

	print("\nFemale id |  height  | weight ")
	for i in range(0,10):
		print("\t{}|\t{}|\t{}".format(i, female_students[i].height, female_students[i].weight))
	return male_students, female_students

'''
	Returns the status of a given point based on its position relative
	to a line.
'''
def get_point_status(student, slope=0, intercept=5.5):
	status = (slope*student.weight) + intercept - student.height
	return status

'''
	Takes 2 lists separated by gender and returns a readout of the 
	errors/accuracy of the model based on a dividing line
'''
def get_measures(male_students, female_students, slope=0, intercept=5.5):
	male_error_count = 0
	male_correct_count = 0
	female_error_count = 0
	female_correct_count = 0

	for student in male_students:
	    status = get_point_status(student, slope, intercept)
	    if status > 0:
	        male_error_count+=1
	    if status < 0:
	        male_correct_count += 1
	    
	for student in female_students:
	    status = get_point_status(student, slope, intercept)
	    if status < 0:
	        female_error_count+=1
	    if status > 0:
	        female_correct_count += 1

	print("male correct, true positive : {}".format(male_error_count))
	print("male errors, false positive : {}".format(male_correct_count))
	print("female errors, false negative : {}".format(female_error_count))
	print("female correct, true negative : {}".format(female_correct_count))

	# ACCURACY MEASURE
	accuracy = (male_correct_count + female_correct_count) / (male_error_count + female_error_count + male_correct_count + female_correct_count)
	accuracy = round(accuracy*10000.0)/10000.0
	error = round((1-accuracy)*10000.0)/10000.0

	print("Accuracy : {}".format(accuracy))
	print("Error: {}".format(error))

	measures = {
		"true_positives" : male_correct_count,
		"false_positives": male_error_count,
		"false_negatives": female_error_count,
		"true_negatives" : female_correct_count,
		"accuracy" : round(accuracy*10000.0)/10000.0,
		"error" : round((1-accuracy)*10000.0)/10000.0
	}

	return measures
	

