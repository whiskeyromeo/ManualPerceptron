'''
	__author__ = "Will Russell"
'''

import csv


weatherFiles = ["train_data_1.txt","train_data_2.txt","train_data_3.txt",]


'''

'''
def retrieve_weather_data(fileName):
	weather_data = []
	with open(fileName, newline="\n") as csvfile:
		csvreader = csv.reader(csvfile, delimiter=",")
		for row in csvreader:
			weather_data.append({"hour":int(row[0]), "temp":float(row[1])})
	return weather_data

'''

'''
def retrieve_training_data(relative_path="./", files=weatherFiles):
	total_training_data = []
	for f in files:
		data = retrieve_weather_data(relative_path + f)
		total_training_data.append(data)
	return total_training_data

def get_all_training_data(relative_path="./", files=weatherFiles):
	total_training_data = []
	for f in files:
		data = retrieve_weather_data(relative_path + f)

