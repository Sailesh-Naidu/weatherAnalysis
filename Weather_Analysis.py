from pathlib import Path
from datetime import  datetime
import  csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#read the csv file from path and get the header
path = Path("data_files/toronto_weather.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
headers = next(reader)
for index, column_header in enumerate(headers):
    print(index, column_header)

t_max, t_min, dates = [], [], []
for row in reader:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high_temp= int(row[headers.index("TMAX")])
        low_temp = int(row[headers.index("TMIN")])
    except:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        t_max.append(high_temp)
        t_min.append(low_temp)

#Plot the high temperature
plt.style.use("classic")
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
ax.plot(dates, t_max, color = 'red')
ax.plot(dates, t_min, color = 'blue')
ax.fill_between(dates, t_max,t_min,facecolor = 'violet', alpha = 0.1)
ax.set_yticks(range(0, 90, 1))
#Format plot
title ='Daily High and Low Temperatures, 2024-2025\nToronto, ON'
ax.set_title(title , fontsize = 24)
ax.set_xlabel(' ', fontsize =16)
fig.autofmt_xdate()
# Set x-axis major ticks to weekly and format dates
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax.set_ylabel('Temperature (F)', fontsize = 16)
ax.tick_params(labelsize = 3)
ax.tick_params(axis='x', labelsize=5)
plt.show()