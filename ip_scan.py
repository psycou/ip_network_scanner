import scapy.all as scapy
from colorama import init, Fore
import optparse
#initialize colorama

init()

#define color

GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN
RESET = Fore.RESET

def get_args():
 
    parser = optparse.OptionParser(description="Good Hacking")
    parser.add_option("-t", "--target", help="Put Your target IP")
    (options, argument) = parser.parse_args()
    if not options.target:
        parser.error("Type -h for more help info")    
    else:
        return options

def scan(ip):
    #create arp request 
    arp_request = scapy.ARP(pdst=ip)
    #create ether part to use it and send it
    broadcast = scapy.Ether(dst="FF:FF:FF:FF:FF:FF")
    arp_request_broadcast = broadcast/arp_request
    #get the answered response from srp request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    #create a list 
    client_list = []
    #iterate the answered list 
    for element in answered_list:
        #create a dictionary
        client_dict = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
        #apend a dictionary to client_list
        client_list.append(client_dict)
    return client_list

#show result from a list and get adictionary
def show_result(result_list):
    print(f"{CYAN}IP\t\t\tMac Address\n-----------------------------------------{RESET}")
    for client in result_list:
        print(f"{GREEN}" + client["IP"] + "\t\t" + client["MAC"])

options = get_args()
   
scan_result = scan(options.target)
show_result(scan_result)
