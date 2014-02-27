opendaylight-flows
==================

This project contains python scripts that allow users to add and remove flows, in the OpenDaylight controller, based on the source and destination IP addresses, and optionally the port number (to re-direct ssh only for example). For these scripts to work, we assume that the user has a topology with the concept of a "local" LAN and a "remote" LAN.

The “AddFlow.py” file is used to add new flows. It is using source and destination IP addresses, as well as a port number. Though, these parameters can be modified, and other parameters are supported as well (VLAN tags, source and destination MAC addresses, etc). To find the correct name of each of these parameters, refer to the graphical view of the OpenDaylight flows. You can try creating flows from there to figure out the correct attributes to use.
There are many actions that can be performed on each flow, and by default it is being output’ed on (redirected to) port 1. This can be changed to anything else, including dropping the flow. The OpenDaylight UI has the list of all actions available.
Please note that this file is using generic values for things such as the node ID, so you will need to change that to your specific uses.

The “DeleteFlow.py” file is used to delete flows. The parameters needed for that are the node ID (which node the flow corresponds to), and its name.

By default, the first script creates 2 flows: one on the source node, and one on the destination node. The flows are using generic IPs, and a port number that the user specifies when the script file is called. The second script is deleting these two flows.

All the magic happens in the “OpenDaylight.py” file: this is where the interaction with the controller happens. This library is written by Dale W. Carder from the  University of Wisconsin. Here’s the origin of it:
http://github.com/dwcarder/python-OpenDaylight
This library is outdated though, and I had to bring it up to date to match the current OpenDaylight parameters. So I recommend using the version included in this project instead. You do not need to touch this library if you’re just adding/deleting flows. If you’re going to be interacting with nodes directly (since this library supports it), some updates might be needed to its last class. Feel free to contribute if needed!

For any questions or comments, my name is Nabil Maadarani, and you can reach me via email: nabil.maadarani@hotmail.com