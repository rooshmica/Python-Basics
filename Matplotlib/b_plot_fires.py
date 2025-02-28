
import matplotlib.pyplot as plt

# Set the data
fires = { "Jan":12, "Feb":5, "Mar":0, "Apr":0, "May":21, "Jun":87,
          "Jul":533, "Aug":2188, "Sep":3586, "Oct":509, "Nov":46, "Dec":6}

# Create the figure and axes
fig, ax = plt.subplots()

# Set the title
ax.set_title("Fires per Month in Acre, 2016")

# set the axis labels
#ax.set_xlabel("Months")
#ax.set_ylabel("Number of Fires")

# plot the values
#ax.plot(list(fires.keys()), list(fires.values()))
ax.plot(fmt= "go--", data=fires)

# show the plot
plt.show()

# Save the figure (bbox = "tight" eliminates whitespace padding)
fig.savefig("acre_fires_2016.png", bbox_inches="tight")
