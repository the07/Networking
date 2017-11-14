#! /usr/bin/env python3

import socket
import netifaces

if __name__ == "__main__":

    # Find the host info
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname()
    print ('Hostname: {}'.format(host_name))

    # Get interfaces list
    ifaces = netifaces.interfaces()
    for iface in ifaces:
        ipaddrs = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in ipaddrs:
            ipaddrs_desc = ipaddrs[netifaces.AF_INET]
            ipaddrs_desc = ipaddrs_desc[0]
            print ("Network Interface: {}".format(iface))
            print ("\tIP address: {}".format(ipaddrs_desc['addr']))
            print ("\tNetmask: {}".format(ipaddrs_desc['netmask']))

    # Find the gateways
    gateways = netifaces.gateways
    print ("Default gateway: {}".format(gateways['default'][netifaces.AF_INET][0]))
