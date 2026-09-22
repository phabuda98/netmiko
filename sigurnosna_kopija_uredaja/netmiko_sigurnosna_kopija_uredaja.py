from netmiko import ConnectHandler
from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day

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
    print('Entering the enable mode...')
    connection.enable()
    output = connection.send_command('show running-config')

    prompt = connection.find_prompt()
    hostname = prompt[0:-1]

    filename = (f'{hostname}_{year}-{month}-{day}_sigurnosna_kopija.txt')

    with open(filename, 'w') as backup:
        backup.write(output)
        print(f'Backup of {hostname} completed successfully')

    print(f'Closing connection to {ip}:')
    print('#' * 30)
    connection.disconnect()