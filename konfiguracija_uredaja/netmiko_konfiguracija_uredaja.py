from netmiko import ConnectHandler

with open('usmjernici.txt', 'r') as f:
   devices = f.read().splitlines()

device_list = list()

for ip in devices:
   cisco_device = {
           'device_type': 'cisco_ios',
           'host': ip,
           'username': 'phabuda',
           'password': 'cisco',
           'port': 22,
           'secret': 'cisco',
           'verbose': True
           }
   device_list.append(cisco_device)

for device in device_list:
    connection = ConnectHandler(**device)

    print('Entering the enable mode ...')
    connection.enable()

    file = input(f'Enter a configuration file (use a valid path) for {device["host"]}:')
    print(f'Running commands from file: {file} on device: {device["host"]}')

    output = connection.send_config_from_file(file)
    print(output)

    save = connection.save_config()
    print(save)

    print(f'Closing connection to {device["host"]}')
    print('#' * 30)

    connection.disconnect()