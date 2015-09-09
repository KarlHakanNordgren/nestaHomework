############################################################
############################################################
# libraries

from __future__ import unicode_literals

import requests
import json
import time
import codecs
import sys
import time
import datetime

############################################################
############################################################
#

api_key= "341015182a3a551179f656a18463b79"

per_page = 2
results_we_got = per_page
offset = 0

def get_results(params):
    request = requests.get("http://api.meetup.com/find/groups", params=params)
    data = request.json()
    return data

while (results_we_got == per_page):
    responses = get_results({"sign":"true", "country":"UK (incl. Northern Ireland)", "key":api_key, "page":per_page, "offset":offset})

    time.sleep(1)
    offset += 1

    results_we_got = len(responses)

    for response in responses:
        created = int(response[u'created'])
        s, ms = divmod(created, 1000)  # (1236472051, 807)
        created = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(s))
        description = response[u'description']
        print(created)
        
    time.sleep(1)


"""

)

print(response)

description = response[0][u'description']

description = x['criteria'][0]['description']
id = x['criteria'][0]['id']
max = x['criteria'][0]['max']

print(response)


                # Meetup.com documentation here: http://www.meetup.com/meetup_api/docs/2/groups/
                response=get_results({"sign":"true","country":"US", "city":city, "state":state, "radius": 10, "key":api_key, "page":per_page, "offset":offset })
                
                results_we_got = response['meta']['count']
                for group in response['results']:
                    category = ""
                    if "category" in group:
                        category = group['category']['name']
                    print "," .join(map(unicode, [city, group['name'].replace(","," "), group['created'], group['city'],group.get('state',""),category,group['members'], group.get('who',"").replace(","," ")]))


            
params

time.sleep(1)
                offset += 1
                results_we_got = response['meta']['count']
                for group in response['results']:
                    category = ""
                    if "category" in group:
                        category = group['category']['name']
                    print "," .join(map(unicode, [city, group['name'].replace(","," "), group['created'], group['city'],group.get('state',""),category,group['members'], group.get('who',"").replace(","," ")]))

            time.sleep(1)

            request = requests.get("http://api.meetup.com/2/groups",params=params)
    data = request.json()






UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def main():

        cities =[("Bridgeport","CT"),("New Haven","CT"),("Hartford","CT"),("Stamford","CT"),("Waterbury","CT")]
        # Get your key here https://secure.meetup.com/meetup_api/key/
        for (city, state) in cities:
            per_page = 200
            results_we_got = per_page
            offset = 0
            while (results_we_got == per_page):
                # Meetup.com documentation here: http://www.meetup.com/meetup_api/docs/2/groups/
                
def get_results():

	
	
	return data


if __name__=="__main__":
        main()


## Run this script and send it into a csv:
## python meetup-pages-names-dates.py > meetup_groups.csv


"""
