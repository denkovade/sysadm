# configuring the network
## Static vs Dynamic:
* DHCP
	* can be statically mapped
	* can set hostname
*Static
	* more work to change
	* one less point of failure
## static configuration steps:
1. set ip -> /etc/sysconfig/network-scripts
	* set to static
2.set gateway ->/etc/sysconfig/network
	* and hostname
	*/etc/hosts
3. set dns -> /etc/resolv.conf

# iptables -> configure linux firewall
- kernel level
- specifies traffic comming and going
- is how we do NAT
```system-confi-firewall-tui``` <br />
```/etc/sysconfig/iptables``` <br />