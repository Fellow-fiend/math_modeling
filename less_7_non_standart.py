import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)
 
 
def init():
    line.set_data([], [])
    return line,

def animate(i):
	t = 0.1 * i
	x0 = 