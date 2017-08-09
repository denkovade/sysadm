# OSI and TCP model

| TCP/IP	  | OSI  | Explanation  | Protocols  |
|---|---|---|---|
|  Process/ | Application  | The Application layer provides services to the software through which the user requests network services. Browsers and FTP client are part of this layer.  |  FTP, SMTP, POP3, HTTP, TFTP, SSH, DNS, DHCP, NTP, SNMP,  Telnet |
|   | Presentation  | This layer is concerned with data representation and code formatting.  | SSL, TLS, ASCII, MPEG  |
|  Application | Session  |  The Session layer establishes, maintains, and manages the communication session between computers. | NetBIOS, SIP  |
|  Host to host | Transport   |  The functions defined in this layer provide for the reliable transmission of data segments, as well as the disassembly and assembly of the data before and after transmission.   | TCP,UDP, RTP   |
|  Internet | Network  | This is the layer on which routing takes place, and, as a result. It defines the processes used to route data across the network and the structure and use of logical addressing.  | IP, BGP, RIP  |
|  Network | Data Link  | this layer is concerned with the linkages and mechanisms used to move data about the network, including the topology, such as Ethernet or Token Ring, and deals with the ways in which data is reliably transmitted.  | Ethernet, Token Ring, PPP   |
|  Access |  Physical | This layer defines the electrical and physical specifications for the networking media that carry the data bits across a network.  | ISDN, DSL, 100Base-Tx  |

# TCP model explanations
- Application Layer: Represents data to the user plus encoding and dialog control
- Transport Layer: Supports communication between divers devices accrose diverse networks.
- Internet Layer: Determines the best path through the network
- Network Accesss Layer: Controls the hardware devices and media that make up the network

# Ports
|port number range | port group   |
|---|---|
| 0 to 1023 | well known (contact) port  |
| 1024 to 49151 | registered ports  |
| 49152 to 65535 | private and/or dynamic ports   |

# Common TCP port number
SSH = 22
Telnet - 23
DNS = 53
SMTP = 25
HTTP = 80
HTTPS = 443

# Common TCP port number
DNS = 53
NTP = 123
TFTP = 69

- *Data Encapsulation* - each lower layer append its header to the data prior to sending it to the lower layer
- *Connection - Oriented* - reliable data transfer method that uses acknowledgements ad flow control. An example is TCP
- *Connectionless-Oriented* - Non reliable best efort data transfer metod with very little overhead. An example is UDP
- *Socket Number* - combination of IP address and port number defining a source or destination
- *Port Number* - uniue identifier for both( TCP/UDP) at the transport layer

# Tipical Network Devices
- Hub - connect multiple devices together making them act as one network segment sing shared bandwidth
- Switch - connects multiple devices rogether providing host with dedicated bandwith (work on layer 2)
- Bridge  - similar to a switch but has less ports and is software based
- Router  - connect two or more logical subnets providing path selection and packet switching ( work on layer 3,2,1)

