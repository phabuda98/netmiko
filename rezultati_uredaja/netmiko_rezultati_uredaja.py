from netmiko import ConnectHandler

with open('usmjernici.txt', 'r') as f:
   devices = f.read().splitlines()

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
        connection = ConnectHandler(**cisco_device)
        print('Entering the enable mode ...')
        connection.enable()
        output1 = connection.send_command('show ip interface brief')
        output2 = connection.send_command('show ip protocol')

        prompt = connection.find_prompt()
        hostname = prompt[0:-1]

        filename = (f'{hostname}_rezultati.txt')

        with open(filename, 'w') as rezultati:
                rezultati.write(output1)
                rezultati.write('\n')
                rezultati.write('\n')
                rezultati.write(output2)
                print(f'Results of {hostname} completed successfully')

        print(f'Closing connection to {cisco_device["host"]}')
        print('#' * 30)

        connection.disconnect()