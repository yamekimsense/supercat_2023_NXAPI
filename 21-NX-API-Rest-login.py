import requests, json

url1 ='https://sandbox-nxos-1.cisco.com'
url2 = "/api/class/aaaLogin.json"

payload =   {
    "aaaUser" : {
      "attributes" : {
        "name" : "admin",
        "pwd" : "Admin_1234!"
      }
    }
  }

#myheaders={'content-type':'application/json'}

response = requests.post (url1+url2, data=json.dumps(payload),  verify=False)
response_json = json.loads(response.text)
token = response_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
print (token)

'''
{"imdata":[{"aaaLogin": {"attributes": {"token": "spBJQo6ALtUuRzB/x3/hGeMDMNVtpkPo+1IV0APGjqrvsKRTrPkJiknL+kdef3JeT7zJ+jA0dA9wIyxhsTfDNRxRdLydzUGHTT7GmrUz7h8s6DAjezg/x8QP+KZsv3CvgMSmJ4rcWJcDJA4RbYw1kMiCZHW64kMxWvI2NAcum1Q=","siteFingerprint": "","refreshTimeoutSeconds": "600","guiIdleTimeoutSeconds": "1200","restTimeoutSeconds": "300","creationTime": "1689529276","firstLoginTime": "1689529276","userName": "admin","remoteUser": "false","unixUserId": "0","sessionId": "iZru/k+JwFssTYnOVteVDg==","lastName": "","firstName": "","version": "0.9(14HEAD${version.patch})","buildTime": "Sun Dec 22 01:23:53 PST 2019","controllerId": "0"},"children": [{"aaaUserDomain": {"attributes": {"name": "all","rolesR": "admin","rolesW": "admin"},"children": [{"aaaReadRoles": {"attributes": {}}},{"aaaWriteRoles": {"attributes": {},"children": [{"role": {"attributes": {"name": "network-admin"}}}]}}]}}]}}]}
'''

#url2 = "/api/mo/sys/showversion.json"
#url2 = "/api/mo/sys/intf/phys-[eth1/1].json"
#url2= "/api/node/mo/sys/intf.json?query-target=children"
url2= "/api/node/mo/sys/intf.json?rsp-subtree=full"

myheaders = { 'Cookie': "APIC-cookie=" + token }
response = requests.get (url1+url2, data=json.dumps(payload), headers=myheaders, verify=False)
print ("\n\n")
print (response.text)

