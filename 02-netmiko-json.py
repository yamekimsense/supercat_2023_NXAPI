import json

from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

cisco_router = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-nxos-1.cisco.com',
    'username': 'admin',
    'password': 'Admin_1234!',
}

ssh = ConnectHandler(**cisco_router)

result = ssh.send_command('show ip int br | json')

print (type(result))

result_json = json.loads(result)

print (type(result_json))

for content in result_json["TABLE_intf"]["ROW_intf"]:
    print (content['intf-name'])