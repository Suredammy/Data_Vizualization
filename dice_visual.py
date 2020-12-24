from plotly.graph_objs import Bar, Layout
from plotly import offline
import matplotlib.pyplot as plt
import numpy as np

from die import Die

die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

# Make some roll and store result in list.

results = [die_1.roll() + die_2.roll() + die_3.roll() for num in range(50000)]
#max_value = die_1.num_sides + die_2.num_sides + die_3.num_sides
max_value = max(results)
min_value = min(results)



# Analyze the results.
freq = [results.count(values) for values in range(3, max_value +1)]
freq_2 = freq[:]

#Plot bar chart with matplotlib
plt.style.use("fivethirtyeight") #set the plot style
fig, ax = plt.subplots(figsize = (16, 9))
n_groups = len(range(3, max_value +1))
x_index = (str(i) for i in range(3, max_value +1))



index = np.arange(start = min_value, stop = max_value + 1, step = 1)
print(index)
bar_width = 0.35
opacity = 0.9



plot_1 = plt.bar(index, freq, bar_width, alpha = opacity, color = 'r')
plot_2 = plt.bar(index + bar_width, freq_2, bar_width, alpha = opacity, color = 'g')

plt.title("Frequencies of score of roll of three, 6 sides dices", fontsize = 16)
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.xticks(index, x_index)

plt.tight_layout()
plt.show()



#frequencies = []
#
#
#for values in range(2, max_value +1):
#    frequency = results.count(values)
#    frequencies.append(frequency)

# Visualize the results with plotly

x_values = list(range(3, max_value + 1))
data = [Bar(x=x_values, y=freq)]

x_axis_config = {"title": "Result", 'dtick' : 1}
y_axis_config = {"title": "Frequency of result"}
my_layout = Layout(
    title="Result of rolling  D6 and D10 dice 50000 times.",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)
#offline.plot({"data": data, "layout": my_layout}, filename="Dice6_and_Dice10.html")
