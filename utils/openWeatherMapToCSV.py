import json
import csv

'''
current structure of these weather files is"
{
    dt
    dt_iso
    clouds
    weather {
        description
    }
    visibility
    wind {
        speed
        deg
    }
    main {
        temp
        temp_min
        temp_max
        feels_like
        pressure
        humidity
        dew_point
    }
    lon
    lat
    city_name
}
'''

header = [
    "elevation",
    "timestamp",
    "textDescription",
    "temperature",
    "dewPoint",
    "windDirection",
    "windSpeed",
    "windGust",
    "barometricPressure",
    "seaLevelPressure",
    "visibility",
    "maxTemperatureLast24Hours",
    "minTemperatureLast24Hours",
    "precipitationLastHour",
    "precipitationLast3Hours",
    "precipitationLast6Hours",
    "relativeHumidity",
    "windChill",
    "heatIndex"
]

weatherMap = {
    "sky is clear": "Clear",
    "overcast clouds": "Mostly Cloudy",
    "few clouds": "Partly Cloudy",
    "scattered clouds": "Partly Cloudy",
    "broken clouds": "Partly Cloudy",
    "light rain": "Light Precipitation",
    "mist": "Fog/Mist",
    "fog": "Fog/Mist",
    "haze": "Haze",
    "moderate rain": "Precipitation",
    "light snow": "Light Precipitation",
    "light intensity shower rain": "Light Precipitation",
    "heavy intensity rain": "Heavy Precipitation",
    "light intensity drizzle": "Light Precipitation",
    "snow": "Precipitation",
    "smoke": "Haze",
    "drizzle": "Light Precipitation",
    "thunderstorm": "Heavy Precipitation",
    "light shower snow": "Light Precipitation",
    "shower rain": "Precipitation",
    "thunderstorm with rain": "Precipitation",
    "heavy snow": "Precipitation",
    "thunderstorm with light rain": "Light Precipitation",
    "dust": "Haze",
    "proximity thunderstorm": "Precipitation",
    "freezing rain": "Precipitation",
    "very heavy rain": "Heavy Precipitation",
    "thunderstorm with heavy rain": "Heavy Precipitation",
    "light rain and snow": "Light Precipitation",
    "heavy intensity shower rain": "Heavy Precipitation",
    "light intensity drizzle rain": "Light Precipitation",
    "shower snow": "Precipitation",
    "shower drizzle": "Light Precipitation",
    "squalls": "Precipitation",
    "proximity squalls": "Light Precipitation",
    "rain and snow": "Precipitation"
}

def formatRowData(data):
    formattedArray = []

    # elevation
    formattedArray.append(27) # KNYC is 27m elevation
    #timestamp
    formattedArray.append(data.get("dt_iso"))
    #textDescription
    weather = data.get("weather")
    if (len(weather) > 0):
        formattedArray.append(weatherMap[weather[0].get("description")])
    else:
        formattedArray.append(None)
    #temperature
    formattedArray.append(data.get("main").get("temp"))
    #dewPoint
    formattedArray.append(data.get("main").get("dew_point"))
    #windDirection
    formattedArray.append(data.get("wind").get("deg"))
    #windSpeed
    formattedArray.append(data.get("wind").get("speed"))
    #windGust
    formattedArray.append(data.get("wind").get("gust"))
    #barometricPressure
    formattedArray.append(data.get("main").get("pressure"))
    #seaLevelPressure
    formattedArray.append(None)
    #visibility
    formattedArray.append(data.get("visibility"))
    #maxTemperatureLast24Hours
    formattedArray.append(None)
    #minTemperatureLast24Hours
    formattedArray.append(None)
    #precipitationLastHour
    #precipitationLast3Hours
    rain = data.get("rain")
    if (type(rain) == dict):
        formattedArray.append(rain.get("1h"))
        formattedArray.append(rain.get("3h"))
    else:
        formattedArray.append(None)
        formattedArray.append(None)
    #precipitationLast6Hours
    formattedArray.append(None)
    '''
    #snowLastHour
    #snowLast3Hours
    snow = data.get("snow")
    if (type(snow) == dict):
        formattedArray.append(snow.get("1h"))
        formattedArray.append(snow.get("3h"))
    else:
        formattedArray.append(None)
        formattedArray.append(None)
    '''
    #relativeHumidity
    formattedArray.append(data.get("main").get("humidity"))
    #windChill
    formattedArray.append(None)
    #heatIndex
    formattedArray.append(None)

    return formattedArray

with open('./data/owm_source.json') as json_file:
    jsondata = json.load(json_file)

data_file = open('./data/owm_output.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
csv_writer.writerow(header)

for data in jsondata:
    csv_writer.writerow(formatRowData(data))

data_file.close()

'''
How to run this file:

1. Navigate to the root directory
2. Download your desired weather file from https://openweathermap.org/history (this is currently assuming the format from the bulk api, but can be modified accordingly)
3. Rename the exported JSON file to 'owm_source.json' and place it in the 'data' directory
4. Run the command with 'python 3 utils/exportToCSV.py'
5. If everything was successful, 'output.csv' should appear in the 'data' directory and have the contents you want
'''
