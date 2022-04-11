'''
Transforms a xmgrace file to a file one can plot with gnuplot.

Next, there is also code for aligning the energy scale to the top of
the valence band instead of the fermi level. This file is saved as
bands_new2.txt

Finally, it creates a gnuplot plotting file with plotting commands for
all the bands (convenient, as there can be a lot of bands). This file
plots the file bands_new2.txt (VBM aligned energy)
'''

#Open modified xmgrace file (top part removed) and read it into the list 'lines'    
f = open("bandsup.agr", "rt")
linesup = f.readlines()
f.close
f = open("bandsdn.agr", "rt")
linesdn = f.readlines()
f.close

#Remove all the xmgrace commands
zup = [x for x in linesup if '&\n' not in x and '@' not in x and '#' not in x]
del zup[0]
zdn = [x for x in linesdn if '&\n' not in x and '@' not in x and '#' not in x]
del zdn[0]

#Save the new, gnuplot formatted list in the file
f = open('bands_newup.txt', 'w')
for element in zup:
    f.write(element)
f.close
f = open('bands_newdn.txt', 'w')
for element in zdn:
    f.write(element)
f.close

#Open bands_new.txt to count the number of bands, and the number of values (k-points) for each band
f = open('bands_newup.txt', 'r')
line_countup = 0
band_countup = 0
for line in f:
    if line!='\n':
        line_countup+=1
    else:
        final_linesup=line_countup
        line_countup=0
        band_countup+=1       
f.close()
f = open('bands_newdn.txt', 'r')
line_countdn = 0
band_countdn = 0
for line in f:
    if line!='\n':
        line_countdn+=1
    else:
        final_linesdn=line_countdn
        line_countdn=0
        band_countdn+=1       
f.close()

#Open bands_new.txt to extract the maximum x-value to put in the plotting file below
f = open('bands_newup.txt', 'r')
for line in f:
    final_line_listup = line 
f.close()
f = open('bands_newdn.txt', 'r')
for line in f:
    final_line_listdn = line 
f.close()

final_line_listup = final_line_listup.split()
x_maxup = final_line_listup[0]
final_line_listdn = final_line_listdn.split()
x_maxdn = final_line_listdn[0]

'''
Align energy to the VBM instead of the fermi-level. The program searches for the highest value
in the valence band. You need to provide the cutoff after looking at the plot (from
the file bands_new.txt) to see what energy the VBM is at compared to E-fermi. 
When you have checked, set the cutoff (below in the code) to a value
slightly higher than the VBM. This is for preventing the program from searching 
past the VBM and into the conduction band, which would be meaningless.
'''
xup=-200
cutoffup=-2.5

xdn=-200
cutoffdn=-2.5

#Get VBM energy
f = open('bands_newup.txt', 'r')
for line in f:
    if line!="\n":
        line2=line.split()
        if float(line2[1])<=cutoffup:
            if float(line2[1])>xup:
                xup=float(line2[1])
print('VBM spin-up energy compared to E-fermi: '+str(xup))
f.close()
f = open('bands_newdn.txt', 'r')
for line in f:
    if line!="\n":
        line2=line.split()
        if float(line2[1])<=cutoffdn:
            if float(line2[1])>xdn:
                xdn=float(line2[1])
print('VBM spin-down energy compared to E-fermi: '+str(xdn))
f.close()

#Load the file into a list
ins = open('bands_newup.txt', 'r')
dataup = []
for line in ins:
    if line!='\n':
        number_strings = line.split() 
        numbers = [float(n) for n in number_strings] 
        dataup.append(numbers)
    else:
        dataup.append('\n')
ins.close() 
ins = open('bands_newdn.txt', 'r')
datadn = []
for line in ins:
    if line!='\n':
        number_strings = line.split() 
        numbers = [float(n) for n in number_strings] 
        datadn.append(numbers)
    else:
        datadn.append('\n')
ins.close() 

#Change all the energy values to align with VBM
i=0
while i < len(dataup):
    if dataup[i][0]!='\n':
        dataup[i][1]-=xup
    i+=1

with open('bands_new2up.txt', 'w') as file:
    for row in dataup:
        if row!='\n':
            file.write(' '.join([str(a) for a in row]) + '\n')
        else:
            file.write(' '.join([str(a) for a in row]))  

i=0
while i < len(datadn):
    if datadn[i][0]!='\n':
        datadn[i][1]-=xdn
    i+=1

with open('bands_new2dn.txt', 'w') as file:
    for row in datadn:
        if row!='\n':
            file.write(' '.join([str(a) for a in row]) + '\n')
        else:
            file.write(' '.join([str(a) for a in row]))  

'''
Create the plotting file. You first need to plot bands_new.txt and see from the plot at what
energy the VBM and CBM is at, so you can set a cutoff (above in the code) 
that is a bit higher than VBM, but lower than CBM. This is so that the program later
can find the VBM energy, and be able to align the energy scale to the VBM instead
of the fermi-level.
When this is done, you can plot bands_new2.txt, and get a plot that is energy aligned
to the VBM.
'''

f = open('bands.plt', 'w')

f.write("set xlabel 'K-points';\n")
f.write("set ylabel 'Energy';\n")
f.write("set ylabel rotate by 90;\n\n")
f.write("set lmargin 13\n\n")
f.write("unset key;\n")
f.write("set grid ytics lt 0 lw 1 lc rgb \"#bbbbbb\"\n")
f.write("set grid xtics lt 0 lw 1 lc rgb \"#bbbbbb\"\n")
f.write("unset grid\n")
f.write("set yrange [-5:5] noreverse\n")
f.write("set xrange [0.00:"+x_maxdn+"] noreverse\n")
f.write("set key default\n\n")

#Add the plotting commands for all the bands. Change to bands_new2.txt for VBM aligned
f.write('plot \"bands_new2up.txt\" every ::1::162 using 1:2 with lines lc "black",\\\n')
for x in range(1,(band_countup)):
    #print(x)
    i = 1+x*final_linesup+xup
    j = final_linesup+xup*162+xup
    f.write('\"bands_new2up.txt\" every ::'+str(i)+'::'+str(j)+' using 1:2 with lines lc "black",\\\n')

f.write('\"bands_new2dn.txt\" every ::1::162 using 1:2 with lines lc "red",\\\n')
for x in range(1,(band_countdn)):
    #print(x)
    i = 1+x*final_linesdn+xdn
    j = final_linesdn+xdn*162+xdn
    f.write('\"bands_new2dn.txt\" every ::'+str(i)+'::'+str(j)+' using 1:2 with lines lc "red",\\\n')

f.write("\n\nset terminal pdf color enhanced linewidth 5\n")
f.write("set output 'bands.pdf'\n")
f.write("replot\n\n")

f.write("set output\n")
f.write("set term windows\n")

f.close()