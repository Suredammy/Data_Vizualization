import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

filename = "data/UTD-weather-2019.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
       

    # Get high temperatures from the file.
    dates,  temp_highs, temp_lows, prcp = [], [], [], []
    for row in reader:
        try:

            current_date = datetime.strptime(row[header_row.index("DATE")], "%Y-%m-%d")
            high = int(row[header_row.index("TMAX")]) #use the header row to get index 
            low = int(row[header_row.index("TMIN")])
            p_amount = float(row[header_row.index("PRCP")])
            
            
        except ValueError:
            print("Value missing for this date")
        
        else:

            dates.append(current_date)
            temp_highs.append(high)
            temp_lows.append(low)
            prcp.append(p_amount)
    station_name = (row[header_row.index("NAME")])


print(station_name)
print(current_date)

# Plot the temperature using matplotlib
plt.style.use("bmh")
opacity = 0.5
index = np.arange(len(temp_highs))
fig, ax = plt.subplots(figsize=(12, 9))
ax.plot(dates, temp_highs, c="red", label="High")
ax.plot(dates, temp_lows, c="blue", label="Low")
#ax.plot(dates, prcp, c = "green", alpha = 0.6, linewidth = 2)
# fill the area between the high and low values.
plt.fill_between(dates, temp_highs, temp_lows, facecolor="purple", alpha=0.2)

fig.autofmt_xdate()
plt.title(f"DAILY TEMPERTURE HIGHS AND LOWS FOR {station_name}, IN {str(current_date)[:4]}.", fontsize=16, c="black")
plt.xlabel("DATE", fontsize=16)
plt.ylabel("TEMPERATURE (F)", fontsize=16)


plt.tick_params(axis="both", which="major", labelsize=14)
plt.legend()
plt.tight_layout()
plt.show()