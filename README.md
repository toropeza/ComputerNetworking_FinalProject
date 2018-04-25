# Computer Networking Final Project (Network Monitor)

### Using Scapy for monitoring MAC addresses on a local network
The project will be a command line tool that utilizes Scapy for packet sniffing in order to listen to packets going out on the Network. It is meant to be left as a long running process which will keep track of the MAC addresses on the network, how long they have been actively using the network, and whether they might be currently on the network or not. It can then be used to track a computer on the local network to see their activity.

[Scapy Library](https://scapy.net/)

The commmand line interface will be the following:
```Bash
list (List all known MAC Addresses on the current Network)
stat <MAC> (Lists all of the stored data from the found MAC Address)
track <MAC> (Will start to listen for all packets coming from the given MAC Address)
untrack <MAC> (Will stop listening for packets from the given MAC Address)
```
