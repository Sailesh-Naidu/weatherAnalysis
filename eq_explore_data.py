from pathlib import Path as p
import json
import plotly.express as px
from matplotlib.mlab import magnitude_spectrum

path = p("data_files/eq_data_30_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)


# create a more readable version of the data file
path = p("data_files/readable_eq_data.json")
readable_contents = json.dumps(all_eq_data, indent = 4)
path.write_text(readable_contents)

#examine all earthquakes in the dataset
all_eq_dicts = all_eq_data["features"]
magnitudes, longitudes, latitudes, eq_titles = [],[],[],[]
for eq_dict in all_eq_dicts:
    magnitude = eq_dict["properties"]['mag']
    longitude = eq_dict['geometry']['coordinates'][0]
    latitude = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    magnitudes.append(magnitude)
    longitudes.append(longitude)
    latitudes.append(latitude)
    eq_titles.append(eq_title)

title = "Global Earthquakes"
fig = px.scatter_geo(lat = latitudes, lon = longitudes,size = magnitudes, title= title,
                     color = magnitudes,
                     color_continuous_scale="temps",
                     labels={'color':'Magnitude',
                             'size':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles)
fig.show()