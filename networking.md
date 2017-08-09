#OSI and TCP model

| TCP/IP	  | OSI  | Explanation  | Protocols  |
|---|---|---|---|
|  Process/ | Application  | The Application layer provides services to the software through which the user requests network services. Browsers and FTP client are part of this layer.  |  FTP, SMTP, POP3, HTTP, TFTP, SSH, DNS, DHCP, NTP, SNMP,  Telnet |
|   | Presentation  | This layer is concerned with data representation and code formatting.  | SSL, TLS, ASCII, MPEG  |
|  Application | Session  |  he Session layer establishes, maintains, and manages the communication session between computers. | NetBIOS, SIP  |
|  Host to host | Transport   |  The functions defined in this layer provide for the reliable transmission of data segments, as well as the disassembly and assembly of the data before and after transmission.   | TCP,UDP, RTP   |
|  Internet | Network  | This is the layer on which routing takes place, and, as a result. It defines the processes used to route data across the network and the structure and use of logical addressing.  | IP, BGP, RIP  |
|  Network | Data Link  | this layer is concerned with the linkages and mechanisms used to move data about the network, including the topology, such as Ethernet or Token Ring, and deals with the ways in which data is reliably transmitted.  | Ethernet, Token Ring, PPP   |
|  Access |  Physical | This layer defines the electrical and physical specifications for the networking media that carry the data bits across a network.  | ISDN, DSL, 100Base-Tx  |


