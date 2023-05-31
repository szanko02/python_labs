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
