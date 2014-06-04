#Base animation code written by Nathan Parzuchowski

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0.0, 1.0), ylim=(0, 15.0)) # change the axis limits here
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    k = str(i) 
    k = (3-len(k))*'0'+k 
    fl = open('1sm1'+k+'.dat','r') #file name here
    
    xr =[] 
    yr =[]
    for roak in fl: 
        broken = roak.strip().split()
        xr.append(float(broken[0])) # x column
        yr.append(float(broken[1])*float(broken[0])*float(broken[0])*4*np.pi) # y column 
 

    x=np.array(xr)
    y=np.array(yr)
    line.set_data(x, y)
    fl.close()
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
# number of frames needs to be input.  Interval will determine the framerate
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=50, blit=True) 

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
