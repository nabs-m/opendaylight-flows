# Author: Nabil Maadarani
#
# This file allows users to add a flow

from OpenDaylight import OpenDaylight
from OpenDaylight import OpenDaylightFlow

# Initiate connection to the ODL controller
odl = OpenDaylight()
odl.setup['hostname'] = '127.0.0.1' # Replace with the ODL Controller IP addresss
odl.setup['username'] = 'admin' # User ID to login to the ODL Controller
odl.setup['password'] = 'admin' # Password to login to the ODL Controller

flow = OpenDaylightFlow(odl)

# User instructions
print('>> You are about to add a new flow')
flowName = 'sshFlow'
localIp = '10.0.0.1' # Specific to the local host
remoteIp = '10.0.0.3' # Specific to the remote host
dstPort = raw_input('>> Enter the port number: ')

if(dstPort == ''):
	# Build the local flow
	odl_test_flow1 = {
		   'installInHw': 'true',
		   'name': flowName + '1',
		   'node': {'id': '00:00:00:00:00:00:00:01', 'type': 'OF'}, # Specific to the node being used
		   'priority': '500',
		   'nwSrc' : localIp,
		   'nwDst' : remoteIp,
		   'etherType': '0x800',
		   'actions': ['OUTPUT=1']}
	
	# Build the remote flow
	odl_test_flow2 = {
		   'installInHw': 'true',
		   'name': flowName + '2',
		   'node': {'id': '00:00:00:00:00:00:00:02', 'type': 'OF'}, # Specific to the node being used
		   'priority': '500',
		   'nwSrc' : remoteIp,
		   'nwDst' : localIp,
		   'etherType': '0x800',
		   'actions': ['OUTPUT=1']}
else:
	odl_test_flow1 = {
		   'installInHw': 'true',
		   'name': flowName + '1',
		   'node': {'id': '00:00:00:00:00:00:00:01', 'type': 'OF'}, # Specific to the node being used
		   'priority': '500',
		   'nwSrc' : localIp,
		   'nwDst' : remoteIp,
		   'tpDst' : dstPort,
		   'protocol' : 'tcp',
		   'etherType': '0x800',
		   'actions': ['OUTPUT=1']}
		   
	odl_test_flow2 = {
		   'installInHw': 'true',
		   'name': flowName + '2',
		   'node': {'id': '00:00:00:00:00:00:00:02', 'type': 'OF'}, # Specific to the node being used
		   'priority': '500',
		   'nwSrc' : remoteIp,
		   'nwDst' : localIp,
		   'tpSrc' : dstPort,
		   'protocol' : 'tcp',
		   'etherType': '0x800',
		   'actions': ['OUTPUT=1']}
	
# Add flow
flow.add(odl_test_flow1)
flow.add(odl_test_flow2)

# Success message
print('********************************')
print('>> SUCCESS... The following flows have been created:')
print('>> ' + odl_test_flow1['name'] + ' on switch #1')
print('>> ' + odl_test_flow2['name'] + ' on switch #2')
print('********************************')