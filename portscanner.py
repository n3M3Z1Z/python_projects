#/usr/bin/env python3

#Import Section

import nmap

nm = nmap.PortSchanner()

#specify target and options
#WARNING! Scanning Ports is illegally in most parts of the wolrd unless you have explicit permission to do so!

target = "45.33.32.156"
options = "-sV -sC scan_results"

#funpart

nm.scan(target, arguments=options)

for  host in nm.all_hosts():
	print("Host %s (%s)" % (host, nm[host].hostname()))
	print("State: %s" % nm[host].state())
	for protocol in nm[host].all_protocols():
		print("Protocol: %s" % protocol)
		port_info = nm[host][protocol]
		for port, state in port_info.items():
			print("Port. %s\tState: %s" % (port, state))
