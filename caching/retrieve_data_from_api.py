import requests
import json
# Import time module
import time

# record start time
start = time.time()


response_API = requests.get('https://gmail.googleapis.com/$discovery/rest?version=v1')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
info = parse_json['description']
print("Info about API:\n", info)
key = parse_json['parameters']['key']['description']
print("\nDescription about the key:\n",key)

# record end time
end = time.time()

# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
