from math import ceil
import numpy as np


#4th order runge-kutta method basic step for function "f"
def rk_step(x,t,h,f):

	k1 = f(x,t)
	assert len(k1) == len(x)
	k2 = f(list(np.sum([x,map(lambda x: x*(h/2.0),k1)],axis=0)),t+(h/2.0))
	assert len(k2) == len(x)
	k3 = f(list(np.sum([x,map(lambda x: x*(h/2.0),k2)],axis=0)),t+(h/2.0))
	assert len(k3) == len(x)
	k4 = f(list(np.sum([x,map(lambda x: x* h,     k3)],axis=0)),t+h)
	assert len(k4) == len(x)
	x_next = [0]*len(x)

	for i in range(0,len(x)):
		x_next[i] = x[i] + h*((1/6.0)*k1[i]+ (1/3.0)*k2[i]+(1/3.0)*k3[i]+(1/6.0)*k4[i])
	assert len(x) == len(x_next)
	return x_next

#4th order runge-kutta method for function "f"
def rk(x0,t0,t1,h,f):
	steps = int(ceil((t1-t0)/h))
	if steps < 100:
		print "Warning less than 100 simulation steps: {0}".format(steps)
	trace = [(x0,t0)]
	
	for i in range(0,steps-1):
		x = trace[i][0]
		t = trace[i][1]
		trace.append((rk_step(x, t, h,f),t+h))
	
	return trace

#basic nonlinear model of lorenz system
def lorenz(x,t,sigma = 10.0, beta= 8.0/3.0, rho = 28.0,debug=False):
	# x,y,z = x[0],x[1],x[2]
	#chaotic parameters
	assert len(x) == 3
	
	dx = sigma*(x[1]-x[0])
	dy = x[0]*(rho-x[2]) -x[1]
	dz = x[0]*x[1] - beta*x[2] 

	return [dx,dy,dz]
