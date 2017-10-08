'''
    This should contain the methods used for graphing the functions 
    for the project

    __author__ = "Will Russell"
    
'''
import matplotlib.pyplot as plt 
from matplotlib import animation
x1,x2 = 210,100
y1,y2,y3 = 4.8,6.2,5.55

male_color = [ .4196,0.957,0.259,.5]
female_color = [ .7, .1843, .6, .5]


def find_intercepts_for_line(weights):
    y_int = -(weights[0]/weights[1])
    x_int = -(weights[0]/weights[2])
    return [0,y_int], [x_int, 0]

def find_intercepts_for_all_lines(weights_list=[[0.,0.,0.],[0.,0.,0.]]):
    values = []
    for weights in weights_list:
        values.append(find_intercepts_for_line(weights))
    return values



'''
    This should graph a set of four graphs displaying the characteristics
    of the male and female data.
'''
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


'''
    Plot data using a single feature
'''
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


'''
    Plot data using 2 features --> height vs weight
'''
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



def plot_normalized_data(title, normal_male_students, normal_female_students,results, dimensions=2):
    plt.figure(title)
    weights = results[-1][1]
    err = results[-1][2]
    male_heights = [x[0] for x in normal_male_students]
    female_heights = [x[0] for x in normal_female_students]
    if dimensions == 2:    
        male_weights = [x[1] for x in normal_male_students]
        female_weights = [x[1] for x in normal_female_students]
        x_vals, y_vals = find_intercepts_for_line(weights)
    else:
        male_weights = [i for i,x in enumerate(normal_male_students)]
        female_weights = [i for i,x in enumerate(normal_female_students)]
        y_intercept = -(weights[0]/weights[1])
        x_vals = [0, len(male_weights)]
        y_vals = [y_intercept, y_intercept]
    x1, x2 = x_vals[0], x_vals[1]
    y1, y2 = y_vals[0], y_vals[1]
    plt.title("Final Error Rate: {}".format(err))
    if dimensions == 2:
        plt.xlabel("Weight")
    plt.ylabel("Height")
    plt.scatter(male_weights,male_heights,marker="s",color=male_color, edgecolors="darkgreen")
    plt.scatter(female_weights, female_heights, marker='o', color=female_color, edgecolors="violet")
    plt.plot([x2, x1],[y2, y1], 'k-', lw=2)
    plt.show()

def plot_animated_data(fig, normal_male_students, normal_female_students, results, dimensions=2, iterations=100):
    # Generate points from normalized male and female students
    
    #fig = plt.figure()
    male_heights = [x[0] for x in normal_male_students]
    female_heights = [x[0] for x in normal_female_students]
    if dimensions == 2:
        male_weights = [x[1] for x in normal_male_students]
        female_weights = [x[1] for x in normal_female_students]
        ax = plt.axes(xlim=(0,1), ylim=(0,1))
        ax.set_xlabel("Weight(Normalized)")
        ax.set_ylabel("Height(Normalized)")
    else: # dimensions is assumed to be 1
        #male_weights = [float(i)/(len(normal_male_students)-1) for i,x in enumerate(normal_male_students)]
        male_weights= [i for i,x in enumerate(normal_male_students)]
        female_weights= [i for i,x in enumerate(normal_female_students)]
        #female_weights = [float(i)/(len(normal_female_students)-1) for i,x in enumerate(normal_female_students)]
        ax = plt.axes(xlim=(0,1), ylim=(0,len(male_weights)))
        ax.set_xlabel("Height(Normalized)")
        ax.set_ylabel("Relative Index")

    line, = ax.plot([],[], lw=2)
    weights_list = [x[1] for x in results]
    if dimensions == 2:
        male_points = ax.scatter(male_heights,male_weights,marker="s",color=male_color, edgecolors="darkgreen")
        female_points = ax.scatter(female_heights,female_weights,marker='o', color=female_color, edgecolors="violet")
        line_points = find_intercepts_for_all_lines(weights_list)

    else:
        male_points = ax.scatter(male_heights, male_weights,marker="s",color=male_color, edgecolors="darkgreen")
        female_points = ax.scatter(female_heights, female_weights, marker='o', color=female_color, edgecolors="violet")
        line_points = [([0,len(male_weights)],[-(x[0]/x[1]),-(x[0]/x[1])]) for x in weights_list]
    ttl = ax.text(.1, 1.05, '', transform = ax.transAxes, va='center')


    def init():
        line.set_data([],[])
        ttl.set_text('Iteration : , error :')
        #errText.set_text("Error Sum : ")
        return line

    def animate(i):
        #errText.set_text("Error Sum : {}".format(results[i][2]))
        y_vals, x_vals = line_points[i]
        ttl.set_text("Iteration : {}, current error : {}, final error: {}".format(i, results[i][2], results[-1][2]))        
        line.set_data(x_vals, y_vals)
        return line
    
    return animation.FuncAnimation(fig, animate,init_func=init, frames=iterations, interval=300, blit=True, repeat=False)

    

