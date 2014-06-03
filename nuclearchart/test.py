import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def main():

    chart = np.genfromtxt('zna.dat',delimiter=" ", dtype = float) 

    A = [row[0] for row in chart]
    Z = [row[1] for row in chart]
    N = [row[2] for row in chart]

    A = np.asarray(A)
    Z = np.asarray(Z)
    N = np.asarray(N) 

    data = np.genfromtxt('ev1.dat', dtype = float) 
    step = np.asarray([row[0] for row in data])
    t = np.asarray([row[1] for row in data])
    He4 = np.asarray([row[6] for row in data])
    C12 = np.asarray([row[7] for row in data])
    O16 = np.asarray([row[8] for row in data])
    Ne20 = np.asarray([row[9] for row in data])
    Mg24 = np.asarray([row[10] for row in data])
    Si28 = np.asarray([row[11] for row in data])
    S32 = np.asarray([row[12] for row in data])
    Ar36 = np.asarray([row[13] for row in data])
    Ca40 = np.asarray([row[14] for row in data])
    Ti44 = np.asarray([row[15] for row in data])
    Cr48 = np.asarray([row[16] for row in data])
    Fe52 = np.asarray([row[17] for row in data])
    Ni56 = np.asarray([row[16] for row in data])
    Zn60 = np.asarray([row[17] for row in data])

   # print O16.shape

    numframes = len(t)
    numpoints = 2
    #print len(A)

    color_data=[]
    
    O16 = np.random.random(numframes)

    #print O16.shape 

    for i in range(numframes): 
        color_data.append([]) 
        for j in range(numpoints): 
            color_data[i].append(O16[i])
    
    #print color_data
    
    testx = [3,2]
    testy =[2,3]

    color_data = np.asarray(color_data)
    print type(color_data)
    print color_data 
    #print color_data.shape
    
    #color_data = np.random.random((numframes, numpoints))
   # print color_data
    #print color_data.shape
   # print type(color_data)
    #print color_data

#    numpoints = len(A) 

    #c = np.random.random(numpoints)
    #c = O16

    fig = plt.figure()
    scat = plt.scatter(testx, testy, c='w', marker='s', s=100)
#
    ani = animation.FuncAnimation(fig, update_plot, frames=xrange(numframes), fargs=(color_data, scat))
    plt.show()

def update_plot(i, data, scat):
    scat.set_array(data[i])
    return scat,

main()
