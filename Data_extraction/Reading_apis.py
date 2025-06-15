'''
What an API is and how it works
How to send a GET request and receive data
How to extract useful info from JSON
How to load that JSON into a Pandas Dataframe

API : Application Programming Interface
- let you pull real-time data from the internet 
(weather, stock prices, COVID stats, etc.) using a URL request

tols used:
import requests: for making api requests
import pandas as pd: for structuring data

'''
"""
import requests
import pandas as pd
# make api request
url = "https://api.covid19api.com/summary"
try:
    response = requests.get(url)
    response.raise_for_status()  # Raises http error for bad responses
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
"""

"""
# check status
print('Status code:', response.status_code)

# load json
data = response.json()

# check keys in returned json
print(data.keys())

# convert country-level data to dataframe
df_countries = pd.DataFrame(data['countries'])

inspect
print(df_countries[['Country', 'TotalConfirmed', 'TotalDeaths']].head())
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt

# make api request 
url = "https://api.open-meteo.com/v1/forecast?latitude=27.7&longitude=85.3&hourly=temperature_2m"
response = requests.get(url)

# check status
print('Status code:', response.status_code)
# status code 200: successful; 404: not found; 500: Server error

# load json
data = response.json()
# convert json content of API into python dictionary

# check keys in returned json
print(data.keys())
# to explore nested content: print(data['hourly'].keys())

# extract
times = data['hourly']['time'] 
temps = data['hourly']['temperature_2m']

"""
data['hourly']: contains all hourly weather data
['time'] is a list of timestamps
['temperature_2m'] is the temperature values corresponding to those times
"""

df = pd.DataFrame({
    'Time': times,
    'Temperature (degree C)': temps
})

# convert time to datatime
df['Time'] = pd.to_datetime(df['Time'])

# plot
plt.plot(df['Time'], df['Temperature (degree C)'])
plt.xticks(rotation = 45)
plt.title('Hourly temperature Forecast (Kathmandu)')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.tight_layout()
plt.show()
