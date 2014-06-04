import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def main():


    A = [1,2,4]
    Z = [1,2,1]
    N = [1,2,3]

    A = np.asarray(A)
    Z = np.asarray(Z)
    N = np.asarray(N) 

    numframes = 9
    numpoints = 3

    color_data=[]
    
  #  t = np.random.random(numframes) 
  #  t1 = np.random.random(numframes) 
    #print t.shape 

    #color_data=t1

#    for i in range(numframes): 
#        color_data.append([]) 
#        for j in range(numpoints): 
#            color_data[i].append(t[1])
    

    color_data = np.array([[9, 17,3], [2, 2,5], [1,3, 3], [5,54, 4], [1,15, 5], [7,1, 8], [19,3,7], [2,21, 6], [12,2, 3]])

    x = np.array([1,2,3,4,5,6,7,8,9])
    y = np.array([29,3,5,7,9,11,13,15,17])
    z = np.array([1,2,3,4,5,6,7,8,9])

    array1= zip(x,y,z)
    print array1
    array1 = np.asarray(array1)
    print array1
    print type(array1)
    print type(color_data)
    print color_data 
    print color_data.shape
    
    #color_data = np.random.random((numframes, numpoints))
    test1 = array1
  #  print color_data
  #  print color_data.shape
  #  print type(color_data)
    #print color_data

#    numpoints = len(A) 

    c = np.random.random(numpoints)
    #c = O16

    fig = plt.figure()
    scat = plt.scatter(Z, N, c='w', marker='s', s=100)
#
    ani = animation.FuncAnimation(fig, update_plot, frames=xrange(numframes), fargs=(test1, scat))
    plt.show()

def update_plot(i, data, scat):
    scat.set_array(data[i])
    return scat,

main()
