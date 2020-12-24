import matplotlib.pyplot as plt

x_values = [x for x in range(1, 50)]
y_values = [x ** 2 for x in range(1, 50)]

plt.style.use('Solarize_Light2')

fig, ax = plt.subplots()


#ax.scatter(x_values, y_values, c = (0.6, 0.3, 0.1), s=10) # c is RGB values between 0 and 1.
#Use Colorma(light colors for low values and dark color for higher values)
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Greens, s=10)
#Set the range for each axis.


#ax.axis([0, 200, 0, 40000])

#Set chart title and label axes.
ax.set_title("Square Numbers", fontsize= 24)
ax.set_xlabel("Value", fontsize = 16)
ax.set_ylabel("Square of Values", fontsize = 16)

#Set size of tick labels.
ax.tick_params(axis = "both", labelsize = 14)

plt.show()

#Save the plot automativally, replaces plt.show()
#plt.savefig("square_plot1.png", bbox_inches = "tight")
