# ip_network_scanner

is an application designed to probe a server or host for connected devices. Such an application may be used by administrators to verify security policies of their networks and by attackers to identify network ip addresses running on a host and exploit vulnerabilities.

requierment:

scapy: follow This insctruction to install scapy

root@root:~$ pip install --pre scapy[basic]

Usage

root@root:~$ python ip_scan.py -t <exemple: 192.168.1.0/24>
