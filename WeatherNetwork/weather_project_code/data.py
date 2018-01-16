'''
This code provides the primary support for the functions implemented
in the jupyter notebook

__author__ = "Will Rusell"


'''

from weather_project_code.fileWorker import retrieve_training_data 
import random
import numpy as np
import os



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

'''
def reformatTrainingData(trainingDict={}, normalize=False):
    tempList = [x["temp"] for subList in trainingDict for x in subList ]
    hourList = [x["hour"] for subList in trainingDict for x in subList ]
    if normalize:
        tempList = normalize_data(tempList)
        hourList = normalize_data(hourList)
    return [hourList, tempList]

'''
'''
def zipTrainingData(trainingList):
    return [list(a) for a in zip(trainingList[0], trainingList[1])]

'''
'''
def prep_weather_data_for_graph(relative_path="./", file_list=[]):
	masterTrainingList = []
	for f in file_list:
		data = retrieve_training_data(relative_path, files=[f])
		data_list = reformatTrainingData(data)
		masterTrainingList.append(data_list)
	return masterTrainingList

'''
'''
def zipTrainingList(trainingList=[[],[]]):
	zipList = []
	for t_list in trainingList:
		trainZip = zipTrainingData(t_list)
		zipList += trainZip
	return zipList 

'''
'''
def generatePredictions(perceptron, weight_set1, weight_set2):
	p1_predictions = [[x, p.test(x, weight_set1)] for x in range(5,10)]
	p2_predictions = [[x, p.test(x, weight_set2)] for x in range(9,14)]
	predictions = p1_predictions + p2_predictions
	# In case of line overlap, take the mean of the point at the overlap
	for i in range(0, len(predictions)-1):
	    if predictions[i][0] == predictions[i+1][0]:
	        predictions[i][1] = (predictions[i][1] + predictions[i+1][1])/2 
	        predictions[i+1][1] = predictions[i][1]
	        
	pred_x = [x[0] for x in predictions]
	pred_y = [x[1] for x in predictions if x[1] not in pred_y]

	return [pred_x, pred_y]




