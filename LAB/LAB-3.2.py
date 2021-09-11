import re

firewall = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

server = re.search('([0-9]|[a-f]{3}.)(.*?)(:[0-9|a-f]{3})', firewall)
protocol = re.search('\w+', firewall)
localserver = re.search('([0-9]|[a-f]{3}.)(.*?)([0-9|a-f]{5})', firewall)
idle = re.search('([0-9]{1}:)([0-9]{2}:)([0-9]{2})', firewall)
bytes_num = re.search('([0-9]{8})', firewall)
flags = re.search('[U].*[O]', firewall)

localserver = localserver.group()[-17:-1]

info = f'''
protocol    :{protocol.group():<20}
server      :{server.group():<20}
localserver :{localserver:<20}
idle        :{idle.group():<20}
bytes       :{bytes_num.group():<20}
flags       :{flags.group():<20}
'''

print(info)
