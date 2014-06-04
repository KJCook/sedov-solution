#A python script for plotting abundances on the nuclear chart as a function of time
#KJC 2/6/2014


import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter 
import matplotlib.animation as animation 

#Set up the chart. Import the A,Z,N of known nuclei

chart = np.genfromtxt('zna.dat',delimiter=" ", dtype = float) 

Abig = [row[0] for row in chart]
Zbig = [row[1] for row in chart]
Nbig = [row[2] for row in chart]

Abig = np.asarray(Abig)
Zbig = np.asarray(Zbig)
Nbig = np.asarray(Nbig) 


#Import stable isotopes HERE 


#Import the data from XNet ev1 outputs

data = np.genfromtxt('ev1.dat', dtype = float) 

#print type(data)
#print data[1][1]
step = [row[0] for row in data]
t = np.log10([row[1] for row in data])
He4 = np.log10([row[6] for row in data])
C12 = np.log10([row[7] for row in data])
O16 = np.log10([row[8] for row in data])
Ne20 = np.log10([row[9] for row in data])
Mg24 = np.log10([row[10] for row in data])
Si28 = np.log10([row[11] for row in data])
S32 = np.log10([row[12] for row in data])
Ar36 = np.log10([row[13] for row in data])
Ca40 = np.log10([row[14] for row in data])
Ti44 = np.log10([row[15] for row in data])
Cr48 = np.log10([row[16] for row in data])
Fe52 = np.log10([row[17] for row in data])
Ni56 = np.log10([row[16] for row in data])
Zn60 = np.log10([row[17] for row in data])

#Make an array holding Z,N,t and the above abundances
#Do this for 16O first
Z=[2,6,8,10,12,14,16,18,20,22,24,26,28,30]
N=[2,6,8,10,12,14,16,18,20,22,24,26,28,30]

color_data = zip(He4,C12,O16,Ne20,Mg24,Si28,S32,Ar36,Ca40,Ti44,Cr48,Fe52,Ni56,Zn60) 
color_data = np.asarray(color_data)

#---------Plotting begins here------

#Plot a white set of boxes
fig = plt.figure()
ax = fig.add_subplot(111) 
big=ax.scatter(Zbig,Nbig,c='w',marker='s', s=100)
scatt = ax.scatter(Z,N,c='w',marker ='s', s=100)

ax.set_xlim(0,35)
ax.set_ylim(0,45)

def update_plot(i, data, scatt):
    scatt.set_array(data[i])
    return scatt,

ani=animation.FuncAnimation(fig,update_plot,frames=len(He4), interval=50, fargs=(color_data,scatt))


plt.show()


