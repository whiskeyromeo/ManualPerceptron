import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import HTML, display
import pandas as pd
from pandas.tools.plotting import table
from weather_project_code.fileWorker import retrieve_training_data
from weather_project_code.data import reformatTrainingData
import random



def find_intercepts_for_line(weights):
    y_int = -(weights[0]/weights[1])
    x_int = -(weights[0]/weights[2])
    return [0,y_int], [x_int, 0]

def find_intercepts_for_all_lines(weights_list=[[0.,0.,0.],[0.,0.,0.]]):
    values = []
    for weights in weights_list:
        values.append(find_intercepts_for_line(weights))
    return values

def generate_colors_list(num_points=1, opacity=0.5):
	color_list = []
	for i in range(0, num_points):
		red = random.uniform(0,1)
		green = random.uniform(0,1)
		blue = random.uniform(0,1)
		color_list.append([red,green,blue,opacity])
	return color_list


def plot_weather_data(weather_data, title="Weather data", save=True):
	handles = []
	plt.figure(title)
	plt.title(title)
	for i, day_list in enumerate(weather_data):
		if(i == 3):
			label = "Day_4_predictions"
			day = plt.scatter(day_list[0], day_list[1], marker="x", color=[0.1,0.1,0.1,0.5], label=label )	
		else:
			label = "Day_" + str(i+1)
			day = plt.scatter(day_list[0], day_list[1], marker="o", color=generate_colors_list(), label=label )
		handles.append(day)
	plt.legend(loc="lower right", handles=handles)
	title = title.replace(" ", "_")
	plt.xlabel("Hour")
	plt.ylabel("Temperature")
	plt.savefig(title+".png")

	plt.show()


def plot_error(training_results, title="Error Plot", save=True):
	plt.figure(title)
	plt.title(title)
	error = [x["error"] for x in training_results]
	iter = [x["iter"] for x in training_results]
	plt.plot(iter, error, 'ro')
	plt.ylabel("Error")
	plt.xlabel("Iteration")
	title = title.replace(" ", "_")
	plt.savefig(title+".png")
	plt.show()

def prep_data_for_pandas(results, iteration):
    if(iteration == 1 or iteration > len(results)):
        raise ValueError("Should be a value between 1 and the number of iterations inclusive")
    data = results[iteration-1]
    df_data = {}
    for k in data:
        if (type(data[k]) is list) and (len(data[k]) > 2):
            if( type(data[k][0]) is not list):
                df_data[k] = data[k]
            #elif k == "row_weights":
                #df_data["hour_weight"] = [x[0] for x in data[k]]
                #df_data["temp_weight"] = [x[1] for x in data[k]]
    return df_data

def generate_df_from_dict(table_dict):
    row_df = pd.DataFrame(table_dict)
    return row_df

def display_table_for_iteration(results, iteration, save=False):
    table = prep_data_for_pandas(results,iteration)
    df_table = generate_df_from_dict(table)
    if(save == True):
    	title = "Results for iteration " + str(iteration)
    	ax = plt.subplot(111, frame_on=False)
    	ax.xaxis.set_visible(False)
    	ax.yaxis.set_visible(False)
    	table(ax, df_table)
    	plt.savefig("weather_table_{}.png".format(iteration))
    display(df_table)

def generate_comparison_dataframe(relativeTestPath, testFile, predictions):
	testData = retrieve_training_data(relativeTestPath, files=[testFile])
	testData = reformatTrainingData(testData)
	predTempList = [x for x in predictions[1]]
	errList=[]
	for i in range(0, len(testData[1])):
		errList.append(predTempList[i] - testData[1][i])
	df_dict = {
		"hours": testData[0],
		"predicted_temps": predTempList,
		"actual_temps": testData[1],
		"error": errList
	}
	return pd.DataFrame(df_dict)

    
    
    
