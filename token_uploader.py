#!/usr/bin/python

import json
import urllib
import urllib2
import httplib
import sys

url = "https://go.urbanairship.com/api/device_tokens/"
base_url = "https://go.urbanairship.com/"

username = "<APP KEY>"
password = "<APP SECRET>"

password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, base_url, username, password)

if(len(sys.argv) < 2):
    print "Format: push_token <Token JSON File>"
    sys.exit(1)


data = ""
with open (sys.argv[1], "r") as myfile:
    data=myfile.read()

json_object = json.loads(data)
ctr = 0;
total = len(json_object);

for currentToken in json_object:
	
	req = urllib2.Request(url+currentToken)
	handler = urllib2.HTTPBasicAuthHandler(password_mgr)
	opener = urllib2.build_opener(handler)
	req.get_method = lambda: 'PUT'
	f = opener.open(req)
	res = urllib2.urlopen(req)
	print res.read()
	ctr=ctr+1
	print str(ctr) + " of " +  str(total) + " Tokens Dumped."
	

print "Completed: "+str(ctr)+"/"+str(total)
