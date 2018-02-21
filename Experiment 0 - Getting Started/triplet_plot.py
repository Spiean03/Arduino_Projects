import numpy as np
import matplotlib.pyplot as plt
import sys

# We expect a single parameter, the name of the file t be plotted
#   First check to see if it is supplied
#   Slightly non-intuitively, the name of the script counts as a parameter

argcount = len(sys.argv)
if (argcount != 2):
    print "I was expecting a filename as a parameter"
    raise Exception("argcount = %d" % (argcount))

filename = sys.argv[1]
print 'Data filename = \'%s\''  % (filename)

# Load all the data fromt the file
#   this will result in an NxM array, 
#   where N is the number of rows, 
#   M the number of columns

filedata = np.loadtxt(filename)

# Check the dimensions for sanity
rows,cols = filedata.shape

if (cols != 3):
    raise Exception("Datafile does not contain 3 columns")

print "File contains %d rows, %d columns" % (rows, cols)

# remap the NxM array in to easy to handle vectors
t = filedata[:,0]
v = filedata[:,1]
e = filedata[:,2]

# This allows TeX / LaTeX commands in labels
plt.rc('text', usetex=True)

# Arbitrary font selection
#   other posibilities would include
#   'sans-serif', 'cursive', 'fantasy', 'monospace'
plt.rc('font', family='serif')

# plot the data with y errorbar and dots
plt.errorbar(t, v, yerr=e, fmt='.')

# Add labels
plt.xlabel(r'\textbf{time} (s)')
plt.ylabel(r'\textbf{voltage} (V)')

# Show it on the screen, can save png/eps/pdf from interface
plt.show()
