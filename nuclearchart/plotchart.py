#A python script for plotting abundances on the nuclear chart as a function of time
#KJC 2/6/2014


import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter 
import matplotlib.animation as animation 
#from itertools import islice 

#Set up the chart. Import the A,Z,N of known nuclei

chart = np.genfromtxt('zna.dat',delimiter=" ", dtype = float) 

Abig = [row[0] for row in chart]
Zbig = [row[1] for row in chart]
Nbig = [row[2] for row in chart]

Abig = np.asarray(Abig)
Zbig = np.asarray(Zbig)
Nbig = np.asarray(Nbig) 


#Import 150 isotopes from netwinv 

#with open('netwinv') as fin, open('output','w') as fout: 
#    fout.writelines(islice(fin,None,None,4))

#print fout

network = np.genfromtxt('150network.dat',delimiter=" ", dtype = float) 
Znetwork = [row[2] for row in network]
Nnetwork = [row[3] for row in network]

#print Znetwork
#print Nnetwork

#Import the data from XNet ev1 outputs

data = np.genfromtxt('ev1.dat', dtype = float) 

#print type(data)
#print data[1][1]
#step = [row[0] for row in data]
#t = [row[1] for row in data]
#He4 = [row[6] for row in data]
#C12 = [row[7] for row in data]
#O16 = [row[8] for row in data]
#Ne20 = [row[9] for row in data]
#Mg24 = [row[10] for row in data]
#Si28 = [row[11] for row in data]
#S32 = [row[12] for row in data]
#Ar36 = [row[13] for row in data]
#Ca40 = [row[14] for row in data]
#Ti44 = [row[15] for row in data]
#Cr48 = [row[16] for row in data]
#Fe52 = [row[17] for row in data]
#Ni56 = [row[16] for row in data]
#Zn60 = [row[17] for row in data]

abundance=[]
for i in range (6,156):
    a = [row[i] for row in data]
    abundance.append(a) 

print type(abundance)

color_data = np.asarray(abundance) 

#print color_data[1]
#print type(color_data)
#print color_data.shape

#transpose the graph

#color_data=zip(*abundance) 
color_data=np.transpose(color_data) 
#print type(color_data)
color_data = np.asarray(color_data) 
color_data=color_data+0.000000000000000000000000000000001
color_data = np.log10(color_data)
#print color_data.shape


#Make an array holding Z,N,t and the above abundances
#Do this for 16O first
#Z=[2,6,8,10,12,14,16,18,20,22,24,26,28,30]
#N=[2,6,8,10,12,14,16,18,20,22,24,26,28,30]

#color_data = zip(He4,C12,O16,Ne20,Mg24,Si28,S32,Ar36,Ca40,Ti44,Cr48,Fe52,Ni56,Zn60) 
#color_data = np.asarray(color_data)

#---------Plotting begins here------

#Plot a white set of boxes
fig = plt.figure()
ax = fig.add_subplot(111) 
big=ax.scatter(Zbig,Nbig,c='w',marker='s', s=100)
scatt = ax.scatter(Znetwork,Nnetwork,c='w',marker ='s', s=100)

ax.set_xlim(-2,35)
ax.set_ylim(-2,45)

def update_plot(i, data, scatt):
    scatt.set_array(data[i])
    return scatt,

ani=animation.FuncAnimation(fig,update_plot,frames=len(color_data), interval=1, fargs=(color_data,scatt))


plt.show()


