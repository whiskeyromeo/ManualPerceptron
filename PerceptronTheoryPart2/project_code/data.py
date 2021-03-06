'''
This code provides the primary support for the functions implemented
in the jupyter notebook

__author__ = "Will Rusell"


'''

import random
import numpy as np
from .Student import Student


'''
	Should normalize whatever data is put in
'''
def normalize_data(data=[]):
    normalized_data = []
    min_v = min(data)
    max_v = max(data)
    for x in data:
        normalized_data.append((x - min_v)/(max_v - min_v))
    return normalized_data

'''
	Converts a list of students into normalized data form
	[[norm_height, norm_weight, gender]...]
'''
def normalize_student_data(students=[]):
	normalized_dataset = []
	student_heights = [x.height for x in students]
	student_heights = normalize_data(student_heights)
	student_weights = [x.weight for x in students]
	student_weights = normalize_data(student_weights)

	student_genders = [x.gender for x in students]
	for i in range(0, len(students)):
		student = [student_heights[i], student_weights[i], student_genders[i]]
		normalized_dataset.append(student)
	return normalized_dataset



def shuffle_students(students, dim=2):
	male_students = [i for i in students if i[dim] == 0]
	female_students = [i for i in students if i[dim] == 1]
	random.shuffle(male_students)
	random.shuffle(female_students)
	new_student_list = []
	if(len(male_students) == len(male_students)):
		for i in range(0, len(male_students)):
			new_student_list.append(male_students[i])
			new_student_list.append(female_students[i])
	return new_student_list





def separate_normalized_students(dataset=[], gender_idx=2):
    male_students = [x for x in dataset if x[gender_idx] == 0]
    female_students = [x for x in dataset if x[gender_idx] == 1]
    return male_students, female_students






def separate_and_normalize_students(dataset=[]):
    students = normalize_student_data(dataset)
    return separate_normalized_students(students)



    
def train_set(students, percentage):
	value = percentage/100
	value = value*float(len(students))
	return_list = random.sample(students, int(value))
	for student in students:
		for retlist in return_list:
			if student == retlist:
				student[3] = True
	return students

def split_set(students):
	training_set = []
	testing_set = []
	for student in students:
		if student[3] == True:
			training_set.append(student)
		else:
			testing_set.append(student)
	return training_set, testing_set

def tecalc(predicted_results, actual_results):
    sub_results = []
    for i in range(0,len(predicted_results)):
        sub_results.append(predicted_results[i] - actual_results[i])
    total_error = 0
    for i in range(0,len(sub_results)):
        total_error += sub_results[i]*sub_results[i]
    return total_error

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
# '''
# Used for project 1
# def get_point_status(student, slope=0, intercept=5.5):
# 	status = (slope*student.weight) + intercept - student.height
# 	return status

# Used for project 2
def get_point_status(student, slope=0, intercept=5.5):
	status = (slope * student[0]) + intercept - student[1]
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

	true_pos = round((male_correct_count/len(male_students))*100000.0)/100000.0
	false_pos = round((male_error_count/len(male_students))*100000.0)/100000.0
	false_neg = round((female_error_count/len(female_students))*100000.0)/100000.0
	true_neg = round((female_correct_count/len(female_students))*100000.0)/100000.0

	print("male correct, true positive : {}".format(true_pos))
	print("male errors, false positive : {}".format(false_pos))
	print("female errors, false negative : {}".format(false_neg))
	print("female correct, true negative : {}".format(true_neg))

	# ACCURACY MEASURE
	accuracy = (male_correct_count + female_correct_count) / (male_error_count + female_error_count + male_correct_count + female_correct_count)
	accuracy = round(accuracy*10000.0)/10000.0
	error = round((1-accuracy)*10000.0)/10000.0

	print("Accuracy : {}".format(accuracy))
	print("Error (Misclassification) Rate: {}".format(error))

	measures = {
		"true_positives" : male_correct_count/len(male_students),
		"false_positives": male_error_count/len(male_students),
		"false_negatives": female_error_count/len(female_students),
		"true_negatives" : female_correct_count/len(female_students),
		"accuracy" : round(accuracy*10000.0)/10000.0,
		"error" : round((1-accuracy)*10000.0)/10000.0
	}

	return measures
	


