import numpy as np

fo = open("zone1.dat", "w")

fo.write('Flat Profile at 2.5 GK \n');
fo.write('Blah Blah        Start Time\n');
fo.write('Beep Boop        Stop Time \n');
fo.write('Borp Blep        Init Del t\n');

targetzone = 30

lastframe = 45
for i in range (0,lastframe+1):
    k = str(i)   
    k = (3-len(k))*'0'+k 
    print "k: ", k
    fl = open('LAG1000sedov1'+k+'.dat','r') #file name here   
    xr =[] 
    yr =[]
    i = 0
    for roak in fl:        
        broken = roak.strip().split()
        xr.append(float(broken[0])) # x column
        yr.append(float(broken[1])) # y column 
        if (i == targetzone-1):
            fo.write('time: ' + broken[0] + ' density: ' + broken[1] + ' pressure: ' + broken[2] + '\n');
            x=np.array(xr)
            y=np.array(yr)

        i=i+1



