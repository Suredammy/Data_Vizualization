import json

##Explore the structure of the data.
filename = 'data/2020-Week-51-Earthquakes.json'
with open(filename, encoding= 'utf-8', errors = 'ignore') as f: #encoding helps to decode file and 
        all_eq_data = json.load(f)


readable_file = 'data/readable_week51_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f , indent = 4)
filename = 'data/readable_week51_eq_data.json'
with open(filename, encoding= 'utf-8', errors = 'ignore') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

#Extract the mag of the earthquakes.

mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
print(mags[:20])

#Extract the longtitude and latitudes of earthquakes. geodata are in (long, latitude) format

lon = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lat = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]

print(lon[:5], "\n", lat[:5])