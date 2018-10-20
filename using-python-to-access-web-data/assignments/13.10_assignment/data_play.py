import json

data ='''
[{
    "results": [
        {
            "address_components": [
                {
                    "long_name": "Kennesaw",
                    "short_name": "Kennesaw",
                    "types": [
                        "locality",
                        "political"
                    ]
                },
                {
                    "long_name": "Cobb County",
                    "short_name": "Cobb County",
                    "types": [
                        "administrative_area_level_2",
                        "political"
                    ]
                },
                {
                    "long_name": "Georgia",
                    "short_name": "GA",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                },
                {
                    "long_name": "United States",
                    "short_name": "US",
                    "types": [
                        "country",
                        "political"
                    ]
                }
            ],
            "formatted_address": "Kennesaw, GA, USA",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 34.066902,
                        "lng": -84.5840659
                    },
                    "southwest": {
                        "lat": 33.9854599,
                        "lng": -84.650021
                    }
                },
                "location": {
                    "lat": 34.0234337,
                    "lng": -84.6154897
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 34.066902,
                        "lng": -84.5840659
                    },
                    "southwest": {
                        "lat": 33.9854599,
                        "lng": -84.650021
                    }
                }
            },
            "place_id": "ChIJobC2WeU_9YgRklgWg8E_q5s",
            "types": [
                "locality",
                "political"
            ]
        }
    ],
    "status": "OK"
}]
'''
js = json.loads(data)
print(type(js))
for erthng in js:
    print(erthng["results"][0]["place_id"])

# lat = js["results"][0]["geometry"]["location"]["lat"]
# location = js['results'][0]['formatted_address']
