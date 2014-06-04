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

fhist = open('1sm.hst','r') #file name here   
i=0
time = []
time.append(float(0))

lastframe = 100

for line in fhist:
    if(i > 6):
       # print line,
        temp = line.strip().split()
       # individualtime = float(temp[7])
       # print individualtime
        time.append(float(temp[7]))
        t = np.array(time)
    i=i+1
    
fo = open("zone1.dat", "w")



fo.write('Generic Comment \n');
fo.write('0.0        Start Time\n');
fo.write(str(time[lastframe]) + '        Stop Time \n');
fo.write(str(time[1]) + '        Init Del t\n');

targetzone = 30


j=0
for i in range (0,lastframe+1):
    k = str(i)   
    k = (3-len(k))*'0'+k    
    fl = open('1sm1'+k+'.dat','r') #file name here   
    xr =[] 
    yr =[]
    i = 0
    for roak in fl:        
        broken = roak.strip().split()  
        density = broken[1]
        pressure = broken[2]
        temperature = T_GK(float(density), float(pressure))
        density = rho_cgs(float(density),float(pressure))
        if (i == targetzone-1):
            fo.write(str(time[j]) + ' ' + str(temperature) + ' ' + str(density)  + '\n');
            j=j+1          

        i=i+1



fhist.close()
fo.close()
fl.close()
