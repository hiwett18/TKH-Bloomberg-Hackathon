# Public APIs
For example purposes, both APIs detailed below are focused on Central Park, NY

## Weather.gov
https://api.weather.gov/stations/KNYC/observations

Provides periodic weather observation information, capturing the following datapoints (example):
```
{
    "@id": "https://api.weather.gov/stations/KJFK/observations/2022-05-06T14:51:00+00:00",
    "@type": "wx:ObservationStation",
    "elevation": {
        "unitCode": "wmoUnit:m",
        "value": 7
    },
    "station": "https://api.weather.gov/stations/KJFK",
    "timestamp": "2022-05-06T14:51:00+00:00",
    "rawMessage": "KJFK 061451Z 15010KT 10SM -RA BKN012 BKN075 OVC090 13/12 A2997 RMK AO2 RAE00B24 SLP148 P0000 60003 T01330117 56009",
    "textDescription": "Light Rain",
    "icon": "https://api.weather.gov/icons/land/day/rain?size=medium",
    "presentWeather": [
        {
            "intensity": "light",
            "modifier": null,
            "weather": "rain",
            "rawString": "-RA"
        }
    ],
    "temperature": {
        "unitCode": "wmoUnit:degC",
        "value": 13.3,
        "qualityControl": "V"
    },
    "dewpoint": {
        "unitCode": "wmoUnit:degC",
        "value": 11.7,
        "qualityControl": "V"
    },
    "windDirection": {
        "unitCode": "wmoUnit:degree_(angle)",
        "value": 150,
        "qualityControl": "V"
    },
    "windSpeed": {
        "unitCode": "wmoUnit:km_h-1",
        "value": 18.36,
        "qualityControl": "V"
    },
    "windGust": {
        "unitCode": "wmoUnit:km_h-1",
        "value": null,
        "qualityControl": "Z"
    },
    "barometricPressure": {
        "unitCode": "wmoUnit:Pa",
        "value": 101490,
        "qualityControl": "V"
    },
    "seaLevelPressure": {
        "unitCode": "wmoUnit:Pa",
        "value": 101480,
        "qualityControl": "V"
    },
    "visibility": {
        "unitCode": "wmoUnit:m",
        "value": 16090,
        "qualityControl": "C"
    },
    "maxTemperatureLast24Hours": {
        "unitCode": "wmoUnit:degC",
        "value": null
    },
    "minTemperatureLast24Hours": {
        "unitCode": "wmoUnit:degC",
        "value": null
    },
    "precipitationLastHour": {
        "unitCode": "wmoUnit:m",
        "value": 0,
        "qualityControl": "C"
    },
    "precipitationLast3Hours": {
        "unitCode": "wmoUnit:m",
        "value": 0,
        "qualityControl": "C"
    },
    "precipitationLast6Hours": {
        "unitCode": "wmoUnit:m",
        "value": null,
        "qualityControl": "Z"
    },
    "relativeHumidity": {
        "unitCode": "wmoUnit:percent",
        "value": 90.036281705393,
        "qualityControl": "V"
    },
    "windChill": {
        "unitCode": "wmoUnit:degC",
        "value": null,
        "qualityControl": "V"
    },
    "heatIndex": {
        "unitCode": "wmoUnit:degC",
        "value": null,
        "qualityControl": "V"
    },
    "cloudLayers": [
        {
            "base": {
                "unitCode": "wmoUnit:m",
                "value": 370
            },
            "amount": "BKN"
        },
        {
            "base": {
                "unitCode": "wmoUnit:m",
                "value": 2290
            },
            "amount": "BKN"
        },
        {
            "base": {
                "unitCode": "wmoUnit:m",
                "value": 2740
            },
            "amount": "OVC"
        }
    ]
}
```

Information is freely available on a rolling 7-day window

## OpenWeatherMap.org
https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=40.78&lon=-73.97&dt=1651536000&appid=API_KEY&units=imperial

Provides hourly weather observation information, capturing the following datapoints (example):
```
{
    "dt":283996800,
    "dt_iso":"1979-01-01 00:00:00 +0000 UTC",
    "timezone":-18000,
    "main": {
        "temp":6.32,
        "temp_min":5.32,
        "temp_max":7.4,
        "feels_like":2.31,
        "pressure":1031,
        "humidity":92,
        "dew_point":5.12
    },
    "clouds": {
        "all":90
    },
    "weather": [{
        "id":741,
        "main":"Fog",
        "description":"fog",
        "icon":"50n"
    },{
        "id":310,
        "main":"Drizzle",
        "description":"light intensity drizzle rain",
        "icon":"09n"
    },{
        "id":500,
        "main":"Rain",
        "description":"light rain",
        "icon":"10n"
    }],
    "visibility":6400,
    "wind":{
        "speed":6.7,
        "deg":170
    },
    "lon":-73.966514,
    "lat":40.78122,
    "city_name":"Central Park"
}
```

Information is available on a rolling 5-day window with a registration for a free API key, and historical data can be purchased
