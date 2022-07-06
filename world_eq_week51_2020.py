
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from plotly import colors


filename = "data/readable_week51_eq_data.json"
with open(filename, encoding="utf-8", errors="ignore") as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]
print(len(all_eq_dicts))

# Extract the mag of the earthquakes.

mags = [eq_dict["properties"]["mag"] for eq_dict in all_eq_dicts]

mags = [mag if mag >= 0 else -1 * mag for mag in mags]

hover_text = [eq_dict["properties"]["title"] for eq_dict in all_eq_dicts]
# Extract the longtitude and latitudes of earthquakes. geodata are in (long, latitude) format

longt = [eq_dict["geometry"]["coordinates"][0] for eq_dict in all_eq_dicts]
latit = [eq_dict["geometry"]["coordinates"][1] for eq_dict in all_eq_dicts]

# Map the earthquakes.
data = [Scattergeo(lon=longt, lat=latit)]
# Another way to represent data

data_2 = [
    {
        "type": "scattergeo",
        "lon": longt,
        "lat": latit,
        "text" : hover_text,
        "marker": {
            "size": [4 * mag for mag in mags],
            "color": mags,
            "colorscale": "Rainbow",
            "reversescale": False,
            "colorbar": {"title": "Magnitude"},
        }, 
    }
]

my_layout = Layout(title="Global Earthquakes, Week 51, 2020")

fig = {"data": data_2, "layout": my_layout}
offline.plot(fig, filename="Global_Earthquakes_Wk_51_2020.html", image_width = 1920, image_height = 1080)

