import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    for index, column_header in enumerate(header_row):
        print(index, column_header)

    #Get high temperatures from the file.
    dates, temp_highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        temp_highs.append(high)
    

with open(filename) as f:
    reader = csv.reader(f)
    temp_lows = [int(row[6]) for row in reader if row[6].isdigit()]
    
with open(filename) as f:
    reader = csv.reader(f)
    temp_date = [row[2] for row in reader]


#Plot the temperature using matplotlib
plt.style.use('bmh')
opacity = 0.5
index = np.arange(len(temp_highs))
fig, ax = plt.subplots(figsize = (12, 9))
ax.plot(dates, temp_highs, c = "red", label = "High")
ax.plot(dates, temp_lows, c = "green", label = "Low")
#fill the area between the high and low values.
plt.fill_between(dates, temp_highs, temp_lows, facecolor = "yellow", alpha = 0.2)
#plt.plot(index, temp_highs,  alpha = opacity , marker = "o", linestyle = '-', linewidth = 2, color = 'r', label = "Temp_high")
#plt.plot(index, temp_lows, alpha = opacity , marker = "o", linestyle = '-', linewidth = 2, color = 'purple', label = "Temp_low")
fig.autofmt_xdate()
#plt.xticks(dates, rotation = 90)

#Format the plot.
#x_index = (str(i) for i in temp_highs)
#x_axis = [t[-2:] for t in temp_date] #Get the days from the date


#plt.xticks(dates, x_axis[1:], rotation = 90)

#plt.yticks(np.arange(y_min, y_max, step = 2))
y_max, y_min =  max(temp_highs) + 2, min(temp_lows) - 2

#plt.ylim(y_min, y_max)
plt.yticks(range(y_min, y_max, 2))
plt.title(f"Temperature high and low for days in 2018", fontsize = 18, c = 'blue')
plt.xlabel("DATE", fontsize = 16)
plt.ylabel("TEMPERATURE (F)", fontsize = 16)


plt.tick_params(axis = 'both', which = 'major', labelsize = 14)
plt.legend()
plt.tight_layout()
plt.show()