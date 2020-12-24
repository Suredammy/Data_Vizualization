from plotly.graph_objs import Bar, Layout
from plotly import offline


from die import Die

die = Die()

#Make some roll and store result in list.

results = [die.roll() for num in range(1000)]

#Analyze the results.
frequencies = []

for values in range(1, die.num_sides + 1):
    frequency = results.count(values)
    frequencies.append(frequency)

#Visualize the results.
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y = frequencies)]

x_axis_config = {'title' : 'Result'}
y_axis_config = {"title": "Frequency of result"}
my_layout = Layout(title = 'Result of rolling one D6 1000 times.', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data' : data, 'layout' : my_layout}, filename = 'Dice6.html')
