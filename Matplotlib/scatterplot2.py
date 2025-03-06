import matplotlib.pyplot as plt

# create empty lists for the data
x_cores = []
y_rmax = []
y_rpeak = []

# read the data from the file
with open("TOP500_201906.csv") as datafile:
    # read the headers line
    headers = datafile.readline()    
    
    # for each line in the file
    for line in datafile:        
        # split the line into the components
        rank, name, cores, rmax, rpeak  = line.strip().split(",")
        
        # insert into lists 
        if int(cores) < 200000:
            x_cores.append(int(cores))
            y_rmax.append(float(rmax))
            y_rpeak.append(float(rpeak))
        
# create a figure and an axis object
fig, ax = plt.subplots()

# set the labels on the axes
ax.set_xlabel("Total Cores")
ax.set_ylabel("TFlops")

# set the title
ax.set_title("Top 500 Supercomputers")

# do a scatter plot
ax.scatter(x_cores, y_rmax, marker=".")
ax.scatter(x_cores, y_rpeak, marker=".")
ax.legend(["Rmax", "Rpeak"])
plt.show()

# save the image
fig.savefig('scatterplot_supercomputers2.png', bbox_inches='tight')


