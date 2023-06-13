'''File: api.py
Author: Bobby Parsons
Date: 10/19/21

Prints data from the API of thebluealliance.com
'''

import http.client # This has to be used instead of Requests with this API for HTTPS and URL headers
import json

appid = "frc4646:PyAssignment:v01"
auth = "E0ANMc6A2uBEkbx4ljiJHjJFCOJNlwXy3JDkmAtY7gqI05xEtShfmuknjDBemKRO" # don't steal this key thx
event = "2018iacf" # 2018 Iowa Regional

url = "/api/v3/event/" + event
keys = {"X-TBA-Auth-Key" : auth, "X-TBA-App-Id" : appid}
c = http.client.HTTPSConnection("www.thebluealliance.com")

c.request("GET", url, headers = keys)
response = c.getresponse()
eventDataRaw = response.read().decode("utf-8")
eventData = json.loads(eventDataRaw)

print(json.dumps(eventData, indent = 4))
