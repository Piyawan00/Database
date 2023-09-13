from netmiko import ConnectHandler

SW4 = {
    'device_type': 'cisco_ios', 
    'ip': '192.168.1.120', 
    'username': 'cisco',
    'password': 'cisco',
}

SW5 = {
    'device_type': 'cisco_ios', 
    'ip': '192.168.1.121', 
    'username': 'cisco',
    'password': 'cisco',
}

f= open('/Users/watcharachai/Downloads/Tunao/imumou 1_64/Network Programming/W10/swconfig') 
lines = f.read().splitlines() 
print (lines)

all_devices = [SW4, SW5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices) 
    output = net_connect.send_config_set(lines) 
    print (output)