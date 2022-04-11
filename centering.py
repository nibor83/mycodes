import sys 

def centering(filename):
	"""Center a molecule placed in the lower left corner (0,0,0) of a Supercell. Assumes a POSCAR with Direct (fractional coordinates)"""
	
	#Read POSCAR file into a string, line by line
	string1 = ["Test\n"]
	fo=open(filename,'r')
	for line in fo:
		string1 += fo.readlines()
	fo.close()

	#Strip the original string to only include coordinates of atoms
	string2 = string1[8:]
	
	#Strip the original string to only include lattice vectors
	string3 = string1[2:4]
	
	#read the string with the coordinates of atoms into an array
	array = []
	for line in string2:
		array.append(line)
	
	#read the string with the lattice vectors into an array
	array2 = []
	for line in string3:
		array2.append(line)
		
	#Keep the first 7 lines in the original string, for writing to file later	
	string1str = string1[0:8]
	
	#Open the modified file for writing
	fo=open("POSCARmod",'w')
	
	#Write the first part:
	for line in string1str:
		fo.write(line)
	
	#Write the second part, i.e the coordinates of the atoms:
	
	#For a POSCAR with fractional coordinates-----------------------------------------------
	
	#we want to add 0.5 to each fractional coordinate, so we must split each line in the array to get each of the x,y and z coordinates and add 0.5.
	splitted = ""
	for line in array:
		splitted = str.split(line)
		splitted[0] = round(float(float(splitted[0])+0.5),20)
		splitted[1] = round(float(float(splitted[1])+0.5),17)
		splitted[2] = round(float(float(splitted[2])+0.5),17)
		
		if splitted[0] >= 1:
			splitted[0] = round(splitted[0]-1,17)
		
		if splitted[1] >= 1:
			splitted[1] = round(splitted[1]-1,17)
		
		if splitted[2] >= 1:
			splitted[2] = round(splitted[2]-1,17)
		
		splittedstr = str(splitted)
		splittedstr = splittedstr[1:-1]
		splittedstr = splittedstr.replace(","," ")
		print(splitted)
		fo.write(splittedstr+"\n")
	#-------------------------------------------------------------------------------------
		
	#For a POSCAR with cartesian coordinates----------------------------------------------
		
	#We want to add half a lattice vector to each cartesian coordinate (in the corresponding direction), so we must split each line in the array to get each
	#of the x, y and z coordinates and add half a lattice vector. We must also split each line in array2 to get the lattice vectors (assuming a cubic supercell).
		
	fo.close()
	
if __name__ == "__main__":
	filename=str(sys.argv[1])
	centering(filename)