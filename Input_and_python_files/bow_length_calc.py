

#!/usr/bin/env python3

import numpy as np
import sys

sys.setrecursionlimit(5000)
k=0
i=-1
def  dist():                   # Modifiziere xy-Flaeche in eine Gauss-foermige xyz 3D-Flaeche
        global k
        global i
        h=2              #Hoehe der  Kurve
        s=38.34           #Periodicity in x direction
                        #x-Wert der maximalen Hoehe
        d=0.02           #Abstand der einzelnen x-Werte
        i=i+1            #Nachfolger-Abstand
        k=k+((h*(np.sin(d*i/s*2*np.pi)-np.sin(d*(i+1)/s*2*np.pi)))**2+d**2)**0.5
         #print(f'{k}  {d*i}')

        if k <= 39.36 :     #Bogenlaenge entspricht dem x-Abstand bei der xy-Ebene, 39.36 ist die Laenge der Grapheneschicht
	            
    	    return dist()

        else:
                x_new = d*i
                return f'C  {x_new:.6f}  '        #x wert nach anwendung des bogenlaengen rechner muss mit dem eingebenen s wert uebereinstimmen
                
print(dist())
