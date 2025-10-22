
#!/usr/bin/env python3

import numpy as np
import sys

sys.setrecursionlimit(5000)

with open('graphene_x_aligned2.xyz', 'r') as file:
    lines = file.readlines()

number_of_atoms = lines[0].strip()        #Extrahiere die Wert fuer die Anzahl der Atome
h=int(number_of_atoms)
print(h)
print()

# Ignoriere die ersten zwei Zeilen (Anzahl der Atome und Kommentar)
data_lines = lines[1:]

# Extrahiere die Werte der zweiten Spalte
x_values = [float(line.split()[1]) for line in data_lines if line.strip()]

# Extrahiere die Werte der dritten Spalte
y_values = [float(line.split()[2]) for line in data_lines if line.strip()]

# Extrahiere die Werte der vierten Spalte
z_values = [float(line.split()[3]) for line in data_lines if line.strip()]

n = len(x_values)
for i in range(n):                 #Durchlaufe alle Koordinaten vom ersten bis zum letzten C Atom
    x=x_values[i]
    y=y_values[i]
    z=z_values[i]
    i=-1
    k=0


    def  dist():                   # Modifiziere xy-Flaeche in eine Gauss-foermige xyz 3D-Flaeche
            global k
            global i
            h=2              #Hoehe der  Kurve
            s=38.34           #Periodicity lenth x, adapt this value by using the bow lenth script, the s value should align with the the x distance value, after using the bow length script
                        #x-Wert der maximalen Hoehe
            d=0.02           #Abstand der einzelnen x-Werte
            i=i+1            #Nachfolger-Abstand
            k=k+((h*(np.sin(d*i/s*2*np.pi)-np.sin(d*(i+1)/s*2*np.pi)))**2+d**2)**0.5
         #print(f'{k}  {d*i}')

            if k <= x :     #Bogenlaenge entspricht dem x-Abstand bei der xy-Ebene
	            
    	        return dist()

            else:
                   x_new = d*i
                   z_new= h*np.sin(d*i/s*2*np.pi)+z
                   return f'C  {x_new:.2f}  {y}  {z_new:.4f}'        #.af  a Nachkomma-Dezimalstellen werden angezeigt
                
    print(dist())
