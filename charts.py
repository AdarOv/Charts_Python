from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import datetime
import os

board_size = '25'
filename = "formList-"+board_size
file = open("./Data/"+board_size+' experiment/'+filename+".txt", "r")
fitness = file.read()
fitness = fitness.split(",")

results = {'x': [], 'y': []}
for i in range(fitness.__len__()):
    results['x'].append(i)
    results['y'].append(int(fitness[i]))

# plot
plt.plot(results['x'], results['y'])
plt.xlabel("Generation")
plt.ylabel("Min Fitness")
plt.title("LightsUp - "+board_size)
d_now = datetime.datetime.now()
current_time = str(d_now.date()) + '_' + str(d_now.hour) + '_' + str(d_now.minute)
path = "./Results/"+current_time
os.makedirs(path)
plt.savefig(path+'/' + filename + ".pdf")
