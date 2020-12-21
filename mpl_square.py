import matplotlib.pyplot as plt

squares = [x ** 2 for x in range(50, 100)]

fig, ax = plt.subplots()
ax.plot(squares, linewidth = 4)



#Set chart title and label axes.
ax.set_title("Square Numbers", fontsize= 32)
ax.set_xlabel("Value", fontsize = 16)
ax.set_ylabel("Square of Values", fontsize = 16)

#Set size of tick labels.
ax.tick_params(axis = "both", labelsize = 14)

plt.show()