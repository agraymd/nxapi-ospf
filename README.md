# nxapi-ospf
Using python and the NX-OS API to Configure OSPF on a device.

This script will authenticate with a Nexus device that has feature nxapi enabled. We store the token received in a variable for later use, and then enable ospf globally, set the router id, and finally configure an interface with an IP address and to participate in our ospf instance in area 0.

Further details are in script comments. There is also a JSON payloads folder so you can examine the payload in a more human readable format. 

Currently, this is just one box, and I have made this for learning purposes. Feel free to add or modify and hit me up :) 

Wishing you all the best! 

