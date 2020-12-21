import matplotlib.pyplot as plt

squares = [x ** 2 for x in range(50, 100)]

plt.style.use('bmh') #Use builtin styles. view with print(plt.style.available)
fig, ax = plt.subplots()
ax.plot(squares, linewidth = 4)



#Set chart title and label axes.
ax.set_title("Square Numbers", fontsize= 24)
ax.set_xlabel("Value", fontsize = 16)
ax.set_ylabel("Square of Values", fontsize = 16)

#Set size of tick labels.
ax.tick_params(axis = "both", labelsize = 14)

plt.show()