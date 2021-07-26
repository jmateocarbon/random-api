import requests
import json
import config

#VT_KEY
#HIBP_key
#Virustotal Scan
VT_key = config.VT_KEY
input_url = input("Please enter URL: ")
scan_url = 'https://www.virustotal.com/vtapi/v2/url/scan'

params = {'apikey': VT_key, 'url': input_url}
response = requests.post(scan_url, data=params)
json_data = response.json()
json_string = json.dumps(json_data)
resp = json.loads(json_string)

scan_id = resp['scan_id']

#Virustotal Retrieve
report_url = 'https://www.virustotal.com/vtapi/v2/url/report'
params = {'apikey': VT_key, 'resource':scan_id}
response_r = requests.get(report_url, params=params)
final_report = json.dumps(response_r.json(), indent=4)
print(final_report)


with open('Virustotal.json', 'w') as json_file:
	json.dump(response_r.json(), json_file, sort_keys = True, indent = 4,
               ensure_ascii = False)





