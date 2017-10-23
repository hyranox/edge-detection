import matplotlib.pyplot as plt 
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def plot_point(ax,x,y):
	points, = ax.plot(x,y,marker='o',linestyle='None')
	return points

def plot_3d(data):

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')


	xs = [d[0] for d in data]
	ys = [d[1] for d in data]
	zs = [d[2] for d in data]
	ax.scatter(xs, ys, zs)

	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')

	plt.show()

	return

def plot_timeseries(time,series_data,xlims = None,ylims= None):
	#compute plot limits if they are not set
	if xlims == None:
		xlims = [min(time),max(time)*1.1]
	if ylims == None:
		ymin = min([min(y) for y in series_data])
		ymax = max([max(y) for y in series_data])
		ylims = [ymin,ymax]

	fig, ax = plt.subplots()
	ax.set_xlim(xlims[0], xlims[1])
	print(ylims)
	ax.set_ylim(ylims[0], ylims[1]) 

	for series in series_data:
		ax.plot(time,series)
	plt.show()
	
	return

def xy_animate(traces,xlims,ylims,duration):
	#configure plot
	fig, ax = plt.subplots()
	ax.set_xlim(xlims[0], xlims[1])
	ax.set_ylim(ylims[0], ylims[1]) 

	datapoint_count = len(traces[0][0])
	traces.append([[0]* datapoint_count,[0]* datapoint_count])
	#get number of steps
	datapoint_count = len(traces[0][0])
	points = [0]*len(traces)
	
	for i in range(0, datapoint_count):
		for t in range(0,len(traces)):
			x = traces[t][0][i]
			y = traces[t][1][i]
			
			if i == 0:
				points[t], = ax.plot(x, y, marker='o', linestyle='None')
			else:
				points[t].set_data(x, y)

		plt.pause(float(duration)/datapoint_count)


if __name__ == "__main__":
	
	plot_timeseries([0,1,2], [[0,1,2],[2,3,4]])