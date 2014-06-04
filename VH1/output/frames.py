import numpy as np

def rho_cgs(rho_code, P_code):
    Msun = 1.99e33;
    Rsun = 6.96e10;
    return rho_code * Msun / Rsun**3;

def T_GK(rho_code, P_code):
    kb = 1.380658e-16;
    mu = 0.5;
    mH = 1.6733e-24;
    Msun = 1.99e33;
    Rsun = 6.96e10;
    P = P_code * Msun/Rsun;
    rho = rho_cgs(rho_code, P_code);
    T = mu*mH/kb * P/rho;
    return 1.0e-9 * T;

fhist = open('LAG1000sedov.hst','r') #file name here   
i=0
time = []
time.append(0)


for line in fhist:
    if(i > 6):
        print line,
        time = line.strip().split()
        individualtime = float(time[7])
        print individualtime
        time.append(float(time[7]))
        t = np.array(time)
    i=i+1
    

fo = open("zone1.dat", "w")

print 'TIME! ' , t

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
            fo.write('time: ' + broken[0] + ' temp: ' + broken[1] + ' density: ' + broken[2] + '\n');
            x=np.array(xr)
            y=np.array(yr)

        i=i+1



fhist.close()
fo.close()
fl.close()
