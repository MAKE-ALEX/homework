import re

mac = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

vlanid = re.search('(\d+)',mac)
print('VLAN ID    : ', vlanid.group())
# 匹配数字多次


mac1 = re.search('([0-9|a-f]{4}.){2}[0-9|a-f]{4}', mac)
print('MAC        : ', mac1.group())
# 匹配数字或者字母，次数4，重复2次。匹配数字或者字母，次数4

type = re.search('[D].*[C]',mac)
print('Type       : ', type.group())
# 匹配D之后的字母多次，到C


interface = re.search('[G].*',mac)
print('Interface  : ', interface.group())