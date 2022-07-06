from plotly.graph_objs import Bar, Layout
from plotly import offline
import matplotlib.pyplot as plt
import numpy as np

from die import Die
die_sides = int(input("Enter the number of sides in your die: "))
#die_1 = Die(6)
#die_2 = Die(6)
#die_3 = Die(6)
tries = [Die(die_sides) for i in range(6)]

# Make some roll and store result in list.

result_1 = [tries[0].roll() + tries[1].roll() + tries[2].roll() for num in range(50000)]
result_2 = [tries[3].roll() + tries[4].roll() + tries[5].roll() for num in range(50000)]
#max_value = die_1.num_sides + die_2.num_sides + die_3.num_sides
max_value = max(result_1)
min_value = min(result_1)



# Analyze the result_1.
freq = [result_1.count(values) for values in range(3, max_value +1)]
freq_2 = [result_2.count(values) for values in range(3, max_value +1)]

#Plot bar chart with matplotlib
plt.style.use("fivethirtyeight") #set the plot style
fig, ax = plt.subplots(figsize = (12, 9))
n_groups = len(range(3, max_value +1))
x_index = (str(i) for i in range(3, max_value +1))


index = np.arange(start = min_value, stop = max_value + 1, step = 1)

bar_width = 0.4
opacity = 0.6


plot_1 = plt.bar(index, freq, bar_width, alpha = opacity, color = 'b', label = "Trial 1")
plot_2 = plt.bar(index + bar_width, freq_2, bar_width, alpha = opacity, color = 'red', label = "Trial 2")

plt.title(f"Frequencies of score of three rolls of {str(die_sides)} sides die", fontsize = 16)
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.xticks(index + bar_width/2, x_index, rotation = 0, color = 'black')
plt.legend()

plt.tight_layout()
plt.show()



# Visualize the result_1 with plotly

x_values = list(range(3, max_value + 1))
data = [Bar(x=x_values, y=freq)]

x_axis_config = {"title": "Result", 'dtick' : 1}
y_axis_config = {"title": "Frequency of result"}
my_layout = Layout(
    title="Result of rolling  D6 and D10 dice 50000 times.",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)
offline.plot({"data": data, "layout": my_layout}, filename="Dice6_and_Dice10.html")
