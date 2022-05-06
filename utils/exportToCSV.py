import json
import csv

'''
structure of these weather files is:
{
    @context
    type: "FeatureCollection"
    features {
        id
        type
        geometry
        properties {
            @id
            type
            elevation
            station
            timestamp
            rawMessage
            textDescription
            icon
            presentWeather
            temperature
            dewPoint
            windDirection
            windSpeed
            windGust
            barometricPressure
            seaLevelPressure
            visibility
            maxTemperatureLast24Hours
            minTemperatureLast24Hours
            precipitationLastHour
            precipitationLast3Hours
            precipitationLast6Hours
            relativeHumidity
            windChill
            heatIndex
            cloudLayers
        }
    }
}
'''

with open('./data/source.json') as json_file:
    jsondata = json.load(json_file)

data_file = open('./data/output.csv', 'w', newline='')
csv_writer = csv.writer(data_file)

count = 0
for features in jsondata:
    if (features != "features"):
        continue

    for data in jsondata.get(features):
        for properties in data:
            if (properties != "properties"):
                continue

            if count == 0:
                header = data.get(properties).keys()
                csv_writer.writerow(header)
                count += 1

            csv_writer.writerow(data.get(properties).values())

data_file.close()

'''
How to run this file:

1. Navigate to the root directory
2. Download your desired weather file from https://www.weather.gov/documentation/services-web-api
3. Rename the exported JSON file to 'source.json' and place it in the 'data' directory
4. Run the command with 'python 3 utils/exportToCSV.py'
5. If everything was successful, 'output.csv' should appear in the 'data' directory and have the contents you want
'''
