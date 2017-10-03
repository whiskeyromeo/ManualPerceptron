'''
	This file should contain code needed to interact with the data files used for projects 1 and 2 in CMSC 409
	
	__author__ = "Will Russell"

'''
import csv
from .Student import Student

'''
	Should return a dict of students with characteristics separated
	into lists
'''
def retrieve_students(fileName="./data.txt"):
	students = []
	with open(fileName, newline="\n") as csvfile:
		csvreader = csv.reader(csvfile, delimiter=",")
		for row in csvreader:
			students.append(Student(row[0], row[1], row[2]))
	return students

'''
	Should write a list of students to a file
'''
def write_students(students=[], fileName="./data2.txt"):
	with open(fileName, newline="\n") as csvfile:
		csvwriter = csv.writer(csvfile, delimiter=",")
		for s in students:
			csvwriter.writerow(s.height, s.weight, s.gender)

'''
	Used to create the coefficient sep_line_a/b.txt files for Project1
'''
def write_coefficients_to_file(x1,x2,y1,y2, fileName):
	f = open(fileName, "w+")
	slope = (y2-y1)/(x2-x1)
	slope = round(slope*10000.0)/10000.0
	if slope != 0:
		intercept = -y2/(slope*x2)
	else:
		intercept = y2
	f.write("{}\n".format(slope))
	f.write("{}\n".format(intercept))
	f.write("{}\n".format(-1))
	f.close()


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