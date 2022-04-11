import numpy as np
import tkinter as tk
import sys 

def BuildConventional111(a):
	"""Building diamond primitive cell with (110)-direction along z-axis"""
	
	a1 = np.array([a*np.sqrt(3/2), 0, 0])
	a2 = np.array([0, a/np.sqrt(2), 0])
	a3 = np.array([0,0,a*np.sqrt(3)])
	
	numberofatoms = 0
	l=([]) #for xyz-file
	m=([])  #for POSCAR-file
	
	#Append the first lines in the POSCAR. Those are not present in a xyz-file.
	m.append("Test" + "\n")
	m.append("1.00" + "\n")
	
	m.append("%2.5f  %2.5f  %2.5f  \n" % (a1[0], a1[1], a1[2]))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (a2[0], a2[1], a2[2]))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (a3[0], a3[1], a3[2]))
				
	#Setting the coordinates for the 12 atoms in the translated 111-diamond primitive basis
	xcoord1=0.333333671*a1[0]
	ycoord1=0.000000000*a2[1]
	zcoord1=0.870176256*a3[2]
				
	xcoord2=0.833334208*a1[0]
	ycoord2=0.500001132*a2[1]
	zcoord2=0.870176256*a3[2]
				
	xcoord3=0.666667342*a1[0]
	ycoord3=0.000000000*a2[1]
	zcoord3=0.786842823*a3[2]
				
	xcoord4=0.166666836*a1[0]
	ycoord4=0.500001132*a2[1]
	zcoord4=0.786842823*a3[2]
	
	xcoord5=0.666667342*a1[0]
	ycoord5=0.000000000*a2[1]
	zcoord5=0.536844194*a3[2]
	
	xcoord6=0.166666836*a1[0]
	ycoord6=0.500001132*a2[1]
	zcoord6=0.536844194*a3[2]
	
	xcoord7=0.000000000*a1[0]
	ycoord7=0.000000000*a2[1]
	zcoord7=0.453510731*a3[2]
	
	xcoord8=0.500000536*a1[0]
	ycoord8=0.500001132*a2[1]
	zcoord8=0.453510731*a3[2]
	
	xcoord9=0.000000000*a1[0]
	ycoord9=0.000000000*a2[1]
	zcoord9=0.203510463*a3[2]
	
	xcoord10=0.500000536*a1[0]
	ycoord10=0.500001132*a2[1]
	zcoord10=0.203510463*a3[2]
	
	xcoord11=0.333333671*a1[0]
	ycoord11=0.000000000*a2[1]
	zcoord11=0.120177053*a3[2]
	
	xcoord12=0.833334208*a1[0]
	ycoord12=0.500001132*a2[1]
	zcoord12=0.120177053*a3[2]
				
	numberofatoms += 12
				
	#Appending the coordinates for POSCAR and xyz files
	l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord1, ycoord1, zcoord1))
	l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord2, ycoord2, zcoord2))
	l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord3, ycoord3, zcoord3))
	l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord4, ycoord4, zcoord4))
	l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord5, ycoord5, zcoord5))
	l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord6, ycoord6, zcoord6))
	l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord7, ycoord7, zcoord7))
	l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord8, ycoord8, zcoord8))
	l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord9, ycoord9, zcoord9))
	l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord10, ycoord10, zcoord10))
	l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord11, ycoord11, zcoord11))
	l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord12, ycoord12, zcoord12))
					
	m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord1, ycoord1, zcoord1))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord2, ycoord2, zcoord2))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord3, ycoord3, zcoord3))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord4, ycoord4, zcoord4))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord5, ycoord5, zcoord5))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord6, ycoord6, zcoord6))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord7, ycoord7, zcoord7))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord8, ycoord8, zcoord8))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord9, ycoord9, zcoord9))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord10, ycoord10, zcoord10))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord11, ycoord11, zcoord11))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord12, ycoord12, zcoord12))
				
	#Inserting some extra lines needed near the top of the POSCAR and xyz files
	m.insert(5, " C " + "\n")
	m.insert(6, "  " + str(numberofatoms) + "\n")
	m.insert(7,"Cartesian\n")
	
	l.insert(0, numberofatoms)
	l.insert(1, "\nTest\n")
	
	print(m)

	#Write to the files
	fo=open('coord.xyz','w')
	for line in l:
		fo.write(str(line))
	fo.close()
	fo=open('POSCAR','w')
	for line in m:
		fo.write(str(line))
	fo.close()
	
	return m
	

def BuildConventional110(a11,a22,a33,a):
	"""Building diamond primitive cell with (110)-direction along z-axis"""
	
	a1 = np.array([a*a11, 0, 0])
	a2 = np.array([0, a*a22/np.sqrt(2), 0])
	a3 = np.array([0,0,a*a33/np.sqrt(2)])
	
	numberofatoms = 0
	l=([]) #for xyz-file
	m=([])  #for POSCAR-file
	
	#Append the first lines in the POSCAR. Those are not present in a xyz-file.
	m.append("Test" + "\n")
	m.append("1.00" + "\n")
	
	m.append("%2.5f  %2.5f  %2.5f  \n" % (a1[0], a1[1], a1[2]))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (a2[0], a2[1], a2[2]))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (a3[0], a3[1], a3[2]))
	
	for i in range(a11):
		for j in range(a22):
			for k in range(a33):
				
				#Setting the coordinates for the 4 atoms in the translated 110-diamond primitive basis
				xcoord1=i*a1[0]
				ycoord1=j*a2[1]
				zcoord1=k*a3[2]
				
				xcoord2=0.74997963719*a+i*a1[0]
				ycoord2=0.35354379147*a+j*a2[1]
				zcoord2=k*a3[2]
				
				xcoord3=0.49998642479*a+i*a1[0]
				ycoord3=0.35354379147*a+j*a2[1]
				zcoord3=0.35354379147*a+k*a3[2]
				
				xcoord4=0.24999321239*a+i*a1[0]
				ycoord4=j*a2[1]
				zcoord4=0.35354379147*a+k*a3[2]
				
				numberofatoms += 4
				
				#Appending the coordinates for POSCAR and xyz files
				l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord1, ycoord1, zcoord1))
				l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord2, ycoord2, zcoord2))
				l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord3, ycoord3, zcoord3))
				l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord4, ycoord4, zcoord4))
					
				m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord1, ycoord1, zcoord1))
				m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord2, ycoord2, zcoord2))
				m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord3, ycoord3, zcoord3))
				m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord4, ycoord4, zcoord4))
				
	#Inserting some extra lines needed near the top of the POSCAR and xyz files
	m.insert(5, " C " + "\n")
	m.insert(6, "  " + str(numberofatoms) + "\n")
	m.insert(7,"Cartesian\n")
	
	l.insert(0, numberofatoms)
	l.insert(1, "\nTest\n")
	
	print(m)

	#Write to the files
	fo=open('coord.xyz','w')
	for line in l:
		fo.write(str(line))
	fo.close()
	fo=open('POSCAR','w')
	for line in m:
		fo.write(str(line))
	fo.close()
	
	return m

def BuildConventionalUCell(a11,a22,a33,a):
	"""Building a diamond conventional unit cell ((001)-direction along z-axis) 
	from a primitive unit cell.
	"""

	#Lattice vectors of diamond primitive unit cell
	a1 = np.array([0, a/2, a/2])
	a2=np.array([a/2, 0, a/2])
	a3=np.array([a/2, a/2, 0])
	
	numberofatoms = 0
	l=([]) #for xyz-file
	m=([])  #for POSCAR-file
	
	#Append the first lines in the POSCAR. Those are not present in a xyz-file.
	m.append("Test" + "\n")
	m.append("1.00" + "\n")
	
	m.append("%2.5f  %2.5f  %2.5f  \n" % (0, a1[1], a1[2]))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (a2[0], 0, a2[2]))
	m.append("%2.5f  %2.5f  %2.5f  \n" % (a3[0], a3[1], 0))
	
	for i in range(a11):
		for j in range(a22):
			for k in range(a33):
				
				#Setting the coordinates for the 2 atoms in the translated diamond primitive basis
				xcoord1=i*a1[0]+j*a2[0]+k*a3[0]
				ycoord1=i*a1[1]+j*a2[1]+k*a3[1]
				zcoord1=i*a1[2]+j*a2[2]+k*a3[2]
				
				xcoord2=0.25*a+i*a1[0]+j*a2[0]+k*a3[0]
				ycoord2=0.25*a+i*a1[1]+j*a2[1]+k*a3[1]
				zcoord2=0.25*a+i*a1[2]+j*a2[2]+k*a3[2]
				
				#We don't want any atoms outside the box with latticeparameter a"
				if (xcoord1 < a and ycoord1 < a and zcoord1 < a):
					numberofatoms += 2
					
					#Appending the coordinates for POSCAR and xyz files
					l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord1, ycoord1, zcoord1))
					l.append(" C  %2.5f  %2.5f  %2.5f \n" % (xcoord2, ycoord2, zcoord2))
					
					m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord1, ycoord1, zcoord1))
					m.append("%2.5f  %2.5f  %2.5f  \n" % (xcoord2, ycoord2, zcoord2))
	
	#Inserting some extra lines needed near the top of the POSCAR and xyz files
	m.insert(5, " C " + "\n")
	m.insert(6, "  " + str(numberofatoms) + "\n")
	m.insert(7,"Cartesian\n")
	
	l.insert(0, numberofatoms)
	l.insert(1, "\nTest\n")

	#Write to the files
	fo=open('coord.xyz','w')
	for line in l:
		fo.write(str(line))
	fo.close()
	fo=open('POSCAR','w')
	for line in m:
		fo.write(str(line))
	fo.close()
	
	return m

def BuildSupercell111(a11, a22, a33, a):
	"""Building a diamond supercell with 111-direction along z-axis, from
	multiple conventional 111 cells"""
	
	a1 = np.array([a*a11*np.sqrt(3/2), 0, 0])
	a2 = np.array([0, a*a22/np.sqrt(2), 0])
	a3 = np.array([0,0,a*a33*np.sqrt(3)])
	
	#Build a conventional unitcell, then use multiples of this to create the supercell
	m = np.array([])
	m = BuildConventional111(a)
	
	o = np.array([])
	for j in range(a11):
		for k in range(a22):
			for l in range(a33):
				#Coordinates in POSCAR file starts at index 8 (line 9)
				for i in m[8:]:
					n = np.array([])
					n = i.strip().split() #Split line at spaces, and strip away blank space in beginning and end of each split
					n[0] = str(float(n[0]) + float(a*j*np.sqrt(3/2))) 
					n[1] = str(float(n[1]) + float(a*k/np.sqrt(2))) 
					n[2] = str(float(n[2]) + float(a*l*np.sqrt(3)))
					o = np.append(o,n)
	
	d= "Test\n1.00\n" + str("%5.5f" % (a*a11*np.sqrt(3/2))) + "  0.00  0.00\n0.00  " +  str("%5.5f" % (a*a22/np.sqrt(2))) + "  0.00\n0.00  0.00  " + str("%5.5f" % (a*a33*np.sqrt(3))) + "\n C\n" + str(12*a11*a22*a33) + "\nCartesian\n"
	for i in range(int(len(o)/3)):
		d += "%5.5f   %5.5f   %5.5f\n" % (float(o[i*3]), float(o[i*3+1]), float(o[i*3+2]))
	#print(d)
	
	fo=open('POSCAR','w')
	for line in d:
		fo.write(str(line))
	fo.close()
	
	BuildIncar('supercell')
	BuildKpoints(8,8,8)
	
	return o
	
def BuildSupercell110(a11, a22, a33, a):
	"""Building a diamond supercell with 110-direction along z-axis, from
	multiple conventional 110 cells"""
	
	#Lattice vectors of the diamond supercell
	a1 = np.array([a*a11, 0, 0])
	a2 = np.array([0, a*a22/np.sqrt(2), 0])
	a3 = np.array([0, 0, a*a33/np.sqrt(2)])
	
	#Build a conventional unitcell, and then use multiples of this to create the supercell
	m = np.array([])
	m = BuildConventional110(1, 1, 1, a)
	
	o = np.array([])
	for j in range(a11):
		for k in range(a22):
			for l in range(a33):
				#Coordinates in POSCAR file starts at index 8 (line 9)
				for i in m[8:]:
					n = np.array([])
					n = i.strip().split() #Split line at spaces, and strip away blank space in beginning and end of each split
					n[0] = str(float(n[0]) + float(a*j)) 
					n[1] = str(float(n[1]) + float(a*k/np.sqrt(2))) 
					n[2] = str(float(n[2]) + float(a*l/np.sqrt(2)))
					o = np.append(o,n)
	
	d= "Test\n1.00\n" + str("%5.5f" % (a11*a)) + "  0.00  0.00\n0.00  " +  str("%5.5f" % (a22*a/np.sqrt(2))) + "  0.00\n0.00  0.00  " + str("%5.5f" % (a33*a/np.sqrt(2))) + "\n C\n" + str(4*a11*a22*a33) + "\nCartesian\n"
	for i in range(int(len(o)/3)):
		d += "%5.5f   %5.5f   %5.5f\n" % (float(o[i*3]), float(o[i*3+1]), float(o[i*3+2]))
	#print(d)
	
	fo=open('POSCAR','w')
	for line in d:
		fo.write(str(line))
	fo.close()
	
	BuildIncar('supercell')
	BuildKpoints(8,8,8)
	
	return o

def BuildSupercell(a11, a22, a33, a):
	"""Building a diamond supercell ((001)-direction along z-axis) 
	from multiple conventional unit cells.
	"""

	#Lattice vectors of the diamond supercell
	a1 = np.array([a*a11, 0, 0])
	a2 = np.array([0, a*a22, 0])
	a3 = np.array([0, 0, a*a33])
	
	#Build a conventional unitcell, and then use multiples of this to create the supercell
	m = np.array([])
	m = BuildConventionalUCell(2, 2, 2, a)
	
	o = np.array([])
	for j in range(a11):
		for k in range(a22):
			for l in range(a33):
				#Coordinates in POSCAR file starts at index 8 (line 9)
				for i in m[8:]:
					n = np.array([])
					n = i.strip().split() #Split line at spaces, and strip away blank space in beginning and end of each split
					n[0] = str(float(n[0]) + float(a*j)) 
					n[1] = str(float(n[1]) + float(a*k)) 
					n[2] = str(float(n[2]) + float(a*l))
					o = np.append(o,n)
	
	d= "Test\n1.00\n" + str("%5.5f" % (a11*a)) + "  0.00  0.00\n0.00  " +  str("%5.5f" % (a22*a)) + "  0.00\n0.00  0.00  " + str("%5.5f" % (a33*a)) + "\n C\n" + str(8*a11*a22*a33) + "\nCartesian\n"
	for i in range(int(len(o)/3)):
		d += "%5.5f   %5.5f   %5.5f\n" % (float(o[i*3]), float(o[i*3+1]), float(o[i*3+2]))
	
	fo=open('POSCAR','w')
	for line in d:
		fo.write(str(line))
	fo.close()
	
	#BuildIncar('supercell')
	#BuildKpoints(8,8,8)
	
	return o
	
def BuildSlab111(a11, a22, a33, h, a, term='false'):
	"""Building a diamond slab ((111)-direction along z-axis)
	from multiple Supercells.
	"""
	
	if term=='false':
		o = BuildSupercell111(a11, a22, a33, a)
		d= "Test\n1.00\n" + str("%5.5f" % (a11*a*np.sqrt(3/2))) + "  0.00  0.00\n0.00  " +  str("%5.5f" % (a22*a/np.sqrt(2))) + "  0.00\n0.00  0.00  " + str("%5.5f" % h) + "\n C\n" + str(12*a11*a22*a33) + "\nCartesian\n"
		for i in range(int(len(o)/3)):
			d += "%5.5f   %5.5f   %5.5f\n" % (float(o[i*3]), float(o[i*3+1]), float(o[i*3+2]))
		#print(d)
		
		fo=open('POSCAR','w')
		for line in d:
			fo.write(str(line))
		fo.close()
		
		BuildIncar('slab')
		BuildKpoints(8,8,1)

def BuildSlab110(a11, a22, a33, h, a, term='false'):
	"""Building a diamond slab ((110)-direction along z-axis) 
	from multiple Supercells.
	"""
	
	if term=='false':
		o = BuildSupercell110(a11, a22, a33, a)
		d= "Test\n1.00\n" + str("%5.5f" % (a11*a)) + "  0.00  0.00\n0.00  " +  str("%5.5f" % (a22*a/np.sqrt(2))) + "  0.00\n0.00  0.00  " + str("%5.5f" % h) + "\n C\n" + str(4*a11*a22*a33) + "\nCartesian\n"
		for i in range(int(len(o)/3)):
			d += "%5.5f   %5.5f   %5.5f\n" % (float(o[i*3]), float(o[i*3+1]), float(o[i*3+2]))
		#print(d)
		
		fo=open('POSCAR','w')
		for line in d:
			fo.write(str(line))
		fo.close()
		
		BuildIncar('slab')
		BuildKpoints(8,8,1)

def BuildSlab(a11, a22, a33, h, a, term='false'):
	"""Building a diamond slab ((001)-direction along z-axis) 
	from multiple Supercells.
	"""
	if term=='false':
		o = BuildSupercell(a11, a22, a33, a)
		d= "Test\n1.00\n" + str("%5.5f" % (a11*a)) + "  0.00  0.00\n0.00  " +  str("%5.5f" % (a22*a)) + "  0.00\n0.00  0.00  " + str("%5.5f" % h) + "\n C\n" + str(8*a11*a22*a33) + "\nCartesian\n"
		for i in range(int(len(o)/3)):
			d += "%5.5f   %5.5f   %5.5f\n" % (float(o[i*3]), float(o[i*3+1]), float(o[i*3+2]))
		print(d)
		
		fo=open('POSCAR','w')
		for line in d:
			fo.write(str(line))
		fo.close()
	else:
		o = BuildSupercell(a11, a22, a33, a)
		d= "Test\n1.00\n" + str("%5.5f" % (a11*a)) + "  0.00  0.00\n0.00  " +  str("%5.5f" % (a22*a)) + "  0.00\n0.00  0.00  " + str("%5.5f" % h) + "\n C " + str(term) + "\n" + str(8*a11*a22*a33) + " " + str(4*a11*a22) + "\nCartesian\n"
		for i in range(int(len(o)/3)):
			d += "%5.5f   %5.5f   %5.5f\n" % (float(o[i*3]), float(o[i*3+1]), float(float(o[i*3+2])+1))
	
		#termination 
		#four atoms per cell, two at the bottom, two at the top.
		#a33=1 gives top atoms at 1.75, a33=2 at 2.75 and so on...
		for j in range(a11):
			for k in range(a22):
				d += "%5.5f   %5.5f   %5.5f\n" % (float(j*a), float(k*a), 0)
				d += "%5.5f   %5.5f   %5.5f\n" % (float(0.5*a + j*a), float(0.5*a + k*a), 0)
				d += "%5.5f   %5.5f   %5.5f\n" % (float(0.25*a + j*a), float(0.75*a + k*a), float((a33-1)*a+4.68))
				d += "%5.5f   %5.5f   %5.5f\n" % (float(0.75*a + j*a), float(0.25*a + k*a), float((a33-1)*a+4.68))
		print(d)
	
		fo=open('POSCAR','w')
		for line in d:
			fo.write(str(line))
		fo.close()
		
		BuildIncar('slab')
		BuildKpoints(8,8,1)

def TerminateSlab100(filename,term="F"):
	"""Open a POSCAR file containing a slab with a clean surface and terminate it with the given termination. This code assumes the z-direction as perpendicular to the surface.
	"""
	
	string1 = ["Test\n"]
	fo=open(filename,'r')
	for line in fo:
		string1 += fo.readlines()
	fo.close()
	string2 = string1[8:]
	
	# string1 = ""
	# fo=open(filename,'r')
	# for line in fo:
		# string1 += line
	# fo.close()
	# string2 = string1.split()
	# string2 = string2[14:]
	
	#Get the max and min z-values in the slab
	max = 0
	min = 20000
	for i in range(0, int(len(string2))-1):
		if (float(string2[i].split()[2]) > max):
			max = float(string2[i].split()[2])
	
	for i in range(0, int(len(string2))-1):
		if (float(string2[i].split()[2]) < min):
			min = float(string2[i].split()[2])
	
	#Get the coordinates of the carbon atoms above/below which the termination should be placed, and add/subtract one Ångström in the z-direction 
	coordsmax = []
	coordsmin = []
	for i in range(0, int(len(string2))-1):
			if (float(string2[i].split()[2]) == max):
				coordsmax.append(string2[i].split()[0])
				coordsmax.append(string2[i].split()[1])
				coordsmax.append(str(float(string2[i].split()[2]) + 1))
	
	for i in range(0, int(len(string2))-1):
			if (float(string2[i].split()[2]) == min):
				coordsmin.append(string2[i].split()[0])
				coordsmin.append(string2[i].split()[1])
				coordsmin.append(str(float(string2[i].split()[2]) - 1))
	
	#Append the coordinates to the POSCAR file
	fo=open(filename,'a')
	for i in range(0, int(len(coordsmax)/3)):
		fo.write("\n" + coordsmax[i*3] + "   " + coordsmax[i*3+1] + "   " + coordsmax[i*3+2])
	for i in range(0, int(len(coordsmin)/3)):
		fo.write("\n" + coordsmin[i*3] + "   " + coordsmin[i*3+1] + "   " + coordsmin[i*3+2])
	fo.close()
	
	#Edit the first few lines in the POSCAR to add the termination
	string3 = ["Test\n"]
	fo=open(filename,'r')
	for line in fo:
		string3 += fo.readlines()
	fo.close()
	string3[5] = string3[5][:-1] + "  " + term + "\n"
	string3[6] = string3[6][:-1] + "  " + str(int(len(coordsmax)/3 + len(coordsmin)/3)) + "\n"
	
	fo=open(filename,'w')
	for line in string3:
		fo.write(line)
	fo.close()
	
def BuildKpoints(x,y,z):
	"""Creating a KPOINTS file for Vasp"""
	d = "Automatic mesh\n" + "0\n" + "gamma\n" + str(x) + " " + str(y) + " " + str(z) + "\n" + "0 0 0"
	
	fo=open('KPOINTS','w')
	for line in d:
		fo.write(str(line))
	fo.close()

def BuildIncar(type):
	"""Creating a INCAR file for Vasp"""
	if type=='slab':
		d = "#Standard settings----------------" + "\n\n" + "LORBIT = 10\n" + "NPAR = 2\n" + "KPAR = 4\n" + "ISTART = 0\n" + "PREC = Normal\n" + "LWAVE = .TRUE\n" + "LCHARG = .TRUE\n" + \
		"#---------------------------------" + "\n\n" + \
		"#Electrons------------------------" + "\n\n" + \
		"ENCUT = 400\n" + "NELM = 500\n" + "NELMIN = 3\n" + "EDIFF = 1E-5\n" + \
		"#---------------------------------" + "\n\n" + \
		"#IONS-----------------------------" + "\n\n" + \
		"EDIFFG = -0.0003\n" + "NSW = 250\n" + "IBRION = 1\n" + "POTIM = 0.2\n" + "ISIF = 1\n" + \
		"#---------------------------------" + "\n\n" + \
		"#DOS related values---------------" + "\n\n" + \
		"ISMEAR = 0\n" + "LREAL = Auto\n" + "SIGMA = 0.2\n" + "ICHARG = 2\n" + \
		"#---------------------------------" + "\n\n" + \
		"#Slab mixing----------------------" + "\n\n" + \
		"AMIX = 0.2\n" + "BMIX = 0.0001\n" + "AMIX_MAG = 0.8\n" + "BMIX_MAG = 0.0001\n" + \
		"#---------------------------------"
	elif type=='supercell':
		d = "#Standard settings----------------" + "\n\n" + "LORBIT = 10\n" + "NPAR = 2\n" + "KPAR = 4\n" + "ISTART = 0\n" + "PREC = Normal\n" + "LWAVE = .TRUE\n" + "LCHARG = .TRUE\n" + \
		"#---------------------------------" + "\n\n" + \
		"#Electrons------------------------" + "\n\n" + \
		"ENCUT = 400\n" + "NELM = 500\n" + "NELMIN = 3\n" + "EDIFF = 1E-5\n" + \
		"#---------------------------------" + "\n\n" + \
		"#IONS-----------------------------" + "\n\n" + \
		"EDIFFG = -0.0003\n" + "NSW = 250\n" + "IBRION = 1\n" + "POTIM = 0.2\n" + "ISIF = 1\n" + \
		"#---------------------------------" + "\n\n" + \
		"#DOS related values---------------" + "\n\n" + \
		"ISMEAR = -5\n" + "LREAL = Auto\n" + "#SIGMA = 0.2\n" + "ICHARG = 2\n" + \
		"#---------------------------------"
	
	fo=open('INCAR','w')
	for line in d:
		fo.write(str(line))
	fo.close()
	
if __name__ == "__main__":
	a1=int(sys.argv[1])
	a2=int(sys.argv[2])
	a3=int(sys.argv[3])	
	a=float(sys.argv[4])
	#h=float(sys.argv[5])
	#term=str(sys.argv[6])
	
	BuildSupercell(a1,a2,a3,a)
	#BuildSupercell111(a1,a2,a3,a)
	
	#BuildSlab(a1,a2,a3,h,a,term)
	#BuildSlab110(a1,a2,a3,h,a,term)
	#BuildSlab111(a1,a2,a3,h,a,term)
	
	#TerminateSlab100('POSCAR4NVf.vasp','f')
	