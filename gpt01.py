from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_nxos',
    'ip': 'sandbox-nxos-1.cisco.com',
    'username': 'admin',
    'password': 'Admin_1234!',
    'port': 22,  # SSH port (기본값은 22입니다)
}

try:
    # 장치에 연결
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show ip int br')
    print(output)

    # 연결 종료
    net_connect.disconnect()

except Exception as e:
    print(f"오류가 발생했습니다: {str(e)}")