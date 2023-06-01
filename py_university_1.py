#1
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
NAT = NAT.replace('Fast', 'Gigabit')
print(NAT)

#2
MAC = 'AAAA:BBBB:CCCC'
MAC = MAC.replace(':','.')
print(MAC)

#3
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
CONFIG = CONFIG.split()[4].split(',')
print(CONFIG)

#4
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
command1 = command1.split()
command2 = command2.split()
VLAN_set = set(command1[4].split(',')).intersection(set(command2[4].split(',')))
VLAN_set = list(map(intVLAN_set)

print(VLAN_set)

#5
VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
new_VLANS = set(VLANS)
new_VLANS = list(new_VLANS)
new_VLANS.sort()
print(new_VLANS)

#6
ospf_route = 'OSPF 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
values = ospf_route.split()
values.remove('via')
keys = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Interface:']

print(keys)
print(values)

#7
MAC = 'AAAA:BBBB:CCCC'
mac = MAC.split(':')
new_mac = "".join(mac)
print(bin(int(new_mac, 16)))

#8
IP = '192.168.3.1'.split('.')
print (IP[0],'{:>8}'.format(IP[1]),'{:>6}'.format(IP[2]),'{:>8}'.format(IP[3]))
binIp = [bin( int(IP[0]) )[2:], bin( int(IP[1]) )[2:], bin( int(IP[2]) )[2:], bin( int(IP[3]) )[2:]]
print (binIp[0].zfill(8), '{:>2}'.format(binIp[1].zfill(8)), '{:>2}'.format(binIp[2].zfill(8)), '{:>2}'.format(binIp[3].zfill(8)))

#9
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
List = num_list
element = 15
print(List)
print ( List.index(element) )
