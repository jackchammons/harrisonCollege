import json
import urllib
import urllib2
import re
import sys



def makeJSONRequest(state):
    URL = "http://api.sba.gov/geodata/city_county_links_for_state_of/QQQ.json".replace('QQQ', state)
    req = urllib2.Request(URL)
    response = urllib2.urlopen(req)
    json_object = response.read()
    countyInfo = json.loads(json_object)
    return countyInfo



def printState(dict):
	f = open('this.txt', 'a')
	for thus in dict:
		for this in thus.keys():
			f.write(str(this))
			f.write(' : ')
			try: #Print to file
				f.write(str(thus[this]))
				f.write('\n')
			except: #In the case of a Unicode error
				f.write("???????\n")

	f.close()


def fetchCountyInfo():
	states = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]
	for state in states:
		print state
		countyInfo = makeJSONRequest(state)
		printState(countyInfo)
	#print 'done'


fetchCountyInfo()


