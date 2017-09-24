import random
import numpy as np
import matplotlib.pyplot as plt
from .Student import Student

x2,x1 = 100, 210
y2, y1 = 6.2, 4.8
y3 = 5.55
male_color = [ .4196,0.957,0.259,.5]
female_color = [ .7, .1843, .6, .5]


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

	print("\nMale id  |   height  | weight ")
	for i in range(0,10):
		print("\t{}|\t{}|\t{}".format(i, male_students[i].height, male_students[i].weight))

	print("\nFemale id |  height  | weight ")
	for i in range(0,10):
		print("\t{}|\t{}|\t{}".format(i, female_students[i].height, female_students[i].weight))
	return male_students, female_students

def write_data_to_file(male_students, female_students, fileName="./data.txt"):
	f = open(fileName, "w+")
	
	male_heights = [x.height for x in male_students]
	male_weights = [x.weight for x in male_students]
	
	female_heights = [y.height for y in female_students]
	female_weights = [y.weight for y in female_students]

	for i in range(0, len(male_students)):
		f.write("{},{},{}\n".format(round(male_heights[i],2),round(male_weights[i],2), 0))
		f.write("{},{},{}\n".format(round(female_heights[i],2), round(female_weights[i],2), 1))
	f.close()



def plot_overall_data(male_students, female_students):
	male_heights = [x.height for x in male_students]
	male_weights = [x.weight for x in male_students]
	
	female_heights = [y.height for y in female_students]
	female_weights = [y.weight for y in female_students]
	sample_size = len(male_students)
	# Visually estimated values based on current sample of 60

	plt.figure("Student Sample")


	# Plot estimated decision function for 2 dimensions
	plt.subplot(221)
	plt.title("Student Height/Weight")
	plt.xlabel("Weight")
	plt.ylabel("Height")
	plt.scatter(male_weights,male_heights,marker="s",color=male_color, edgecolors="darkgreen")
	plt.scatter(female_weights, female_heights, marker='o', color=female_color, edgecolors="violet")
	
	# plt.plot(male_weights,male_heights,marker="s", color=[ 0.,0.47843137,0.76078431,1.])
	# plt.plot(female_weights, female_heights, marker='o', color=[ 0.,0.36078431,0.81960784,1.])
	plt.plot([x2, x1],[y2, y1], 'k-', lw=2)

	# Plot Estimated decision function for 1 dimension
	plt.subplot(222)
	plt.title("Student Height")
	plt.scatter([i for i,v in enumerate(male_heights)],male_heights, marker='s',color=male_color, edgecolors="darkgreen")
	plt.scatter([i for i,v in enumerate(female_heights)],female_heights, marker='o',color=female_color, edgecolors="violet")
	plt.plot([0,sample_size],[y3,y3], 'k-', lw=2)

	# Plot normally distributed data for males : weight x height
	plt.subplot(223)
	plt.title("Male Data")
	plt.xlabel("Male Weight")
	plt.ylabel("Male Height")
	plt.scatter(male_weights, male_heights, marker='s',color=male_color, edgecolors="darkgreen")

	# Plot normally distributed data for females : weight x height
	plt.subplot(224)
	plt.title("Female Data")
	plt.xlabel("Female Weight")
	plt.ylabel("Female Height")
	plt.scatter(female_weights, female_heights, marker='o',color=female_color, edgecolors="violet")

	plt.tight_layout()
	plt.show()

def plot_height_data(male_students, female_students, y3=5.5):
	male_heights = [x.height for x in male_students]

	female_heights = [y.height for y in female_students]
	sample_size = len(male_students)
	plt.figure("Scenario A : Height Only")
	plt.title("Student Height")
	plt.ylabel("Height")
	plt.scatter([i for i,v in enumerate(male_heights)],male_heights, marker='s',color=male_color, edgecolors="darkgreen")
	plt.scatter([i for i,v in enumerate(female_heights)],female_heights, marker='o',color=female_color, edgecolors="violet")
	plt.plot([0,sample_size],[y3,y3], 'k-', lw=2)
	plt.show()

def plot_height_weight_data(male_students, female_students, x_vals=[x1,x2], y_vals=[y1,y2]):
	male_heights = [x.height for x in male_students]
	male_weights = [x.weight for x in male_students]

	female_heights = [y.height for y in female_students]
	female_weights = [y.weight for y in female_students]
	x1, x2 = x_vals[0], x_vals[1]
	y1, y2 = y_vals[0], y_vals[1]

	sample_size = len(male_students) 
	plt.figure("Scenario B : Height and Weight")
	plt.title("Student Height/Weight")
	plt.xlabel("Weight")
	plt.ylabel("Height")
	plt.scatter(male_weights,male_heights,marker="s",color=male_color, edgecolors="darkgreen")
	plt.scatter(female_weights, female_heights, marker='o', color=female_color, edgecolors="violet")
	plt.plot([x2, x1],[y2, y1], 'k-', lw=2)
	plt.show()

def get_point_status(student, slope=0, intercept=5.5):
	status = (slope*student.weight) + intercept - student.height
	return status

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

	print("male errors, true positive : {}".format(male_error_count))
	print("male errors, false positive : {}".format(male_correct_count))
	print("female errors, false negative : {}".format(female_error_count))
	print("female errors, true negative : {}".format(female_correct_count))

	# ACCURACY MEASURE
	accuracy = (male_correct_count + female_correct_count) / (male_error_count + female_error_count + male_correct_count + female_correct_count)
	print("Accuracy : {}".format(accuracy))
	print("Error: {}".format(1-accuracy))

	measures = {
		"true_positives" : male_correct_count,
		"false_positives": male_error_count,
		"false_negatives": female_error_count,
		"true_negatives" : female_correct_count,
		"accuracy" : accuracy,
		"error" : (1-accuracy)
	}

	return measures
	


