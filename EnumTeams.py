#!usr/bin/env python3
# Performs username enumeration using the teams API
# Copyright (c) 2020 Frans Hendrik Botes @initroot
# 

import requests
import argparse
import requests
import base64
import urllib3
import time
import json



#colors
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


#We don't want SSL warnings
urllib3.disable_warnings()

### Arguments ###
parser = argparse.ArgumentParser()
parser.add_argument("-u","--users", help="Email list",required=True, dest='users')
parser.add_argument("-a","--authtokens", help="Auth token",required=True, dest='authtokens')
args = parser.parse_args()

### Variables ###
authtokenZ = args.authtokens
proxiesDATA = {"http":"http://127.0.0.1:8080", "https":"https://127.0.0.1:8080"}
headerDATA = {"Authorization": authtokenZ,"x-ms-client-version":"27/1.0.0.2020111144","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36","Content-type": "application/json; charset=UTF-8","Accept": "application/json"}
urlDATA = "/api/mt/emea/beta/users/REPUSERNAME/externalsearchv3"
target = "https://teams.microsoft.com"
#Loop that reads the users
def main(users,authtok):
	print("")
	print("")
	print (OKBLUE  + BOLD +  "Userlist loaded: " + args.users + ENDC)
	print("")
	fusers = open(users,"r")
	users = fusers.readlines()
	print(HEADER  + BOLD + "accountEnabled" + " , " + "userPrincipalName"+ " , " + "givenName"+ " , " + "displayName"+ " , " + "type"+ " , " + "email" + ENDC) 
	for user in users:
		time.sleep(1)
		user = user.replace("\n",'')
		geturlDATA = urlDATA.replace("REPUSERNAME",user)
		with requests.Session() as s:
			try:
				
				response1 = s.get(target + geturlDATA,headers=headerDATA,verify=False)				
				#response1 = s.get(target + geturlDATA,headers=headerDATA,proxies=proxiesDATA,verify=False) #if you want to proxy it
			except Exception as inst:
				print(inst)
				continue

			if ('Checking your credentials') in str(response1.content):
				print(FAIL + "Bearer token has expired..." + ENDC)
				continue
			elif ('Forbidden') in str(response1.content):
				print(OKGREEN + user + " --POTENTIAL VALID NO PERMISSIONS" + ENDC)
			elif (response1.status_code == 401):
				print(FAIL + "Bearer token not valid!" + ENDC)
			elif (response1.status_code == 200) and (len(response1.content)> 10):		
				json_data = json.loads(response1.text)
				json_data = json_data[0]
				accEnabled = parseData(0,json_data)
				usrPrinc =  parseData(1,json_data)
				givName =  parseData(2,json_data)
				dspName =  parseData(3,json_data)
				tpy =  parseData(4,json_data)
				usrMail =  parseData(5,json_data)
				print(OKGREEN + accEnabled+ " , " + usrPrinc + " , " + givName + " , " + dspName + " , " + tpy + " , " + usrMail + ENDC) 
			else:
				print(WARNING + user + " --INVALID" + ENDC)



def parseData(agrument, data):
	try:
			if agrument == 0:
				return str(data["accountEnabled"])
			elif agrument ==  1:
				return str(data["userPrincipalName"])
			elif agrument ==  2:
				return str(data["givenName"])
			elif agrument ==  3:
				return str(data["displayName"])
			elif agrument ==  4:
				return str(data["type"])
			elif agrument ==  5:
				return str(data["email"])

	except:
		return "." 







if __name__ in ('__main__', 'main'):
    main(users=args.users,authtok=args.authtokens)

