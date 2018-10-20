# ---- WRITTEN INSTRUCTION ----
# Write a program that will:
# 1. Prompt for a "location"
# 2. Contact a web service (DB)
# 3. Retrieve JSON for the web service
# 4. Parse that data
# 5. Retrieve the first `place_id` from the JSON.
#
# ----- Playground ----
#
import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

# While Loop - START
while True:
    # User Input - Enter input & assign
    address = input('Enter location: ')
    # IF Loop Statement
    # "if the input was less than one char than break While Loop"
    if len(address) < 1: break

    # assign merged serviceurl with the "address" var to "url" and encode with given string into appropriate sytax
    url = serviceurl + urllib.parse.urlencode(
        {'address': address})
    # Print resulting URL
    print('Retrieving', url)
    # using urllib send request to the new compiled URL, which returns an object "<http.client.HTTPResponse object at 0x106c3b6d8>"
    uh = urllib.request.urlopen(url)
    # read the object returned and place it in "data"
    data = uh.read().decode()
    # the length of the var "data"
    print('Retrieved', len(data), 'characters')

    # initialize try/except for error chatching
    try:
    # try to load data into "js" as readable json
        js = json.loads(data)
    except:
    # except "None" assigned to "js"
        js = None
    # ERROR Handling -
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    # ? -
    #print(json.dumps(js, indent=4))

    # climbing the json tree and assigning result to "lat" & "lng"
    js = json.loads(data)
    print(js)
    reslt = js["results"][0]["place_id"]
    print(reslt)

# While Loop - END
