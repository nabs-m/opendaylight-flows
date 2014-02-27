# Author: Nabil Maadarani
#
# This file allows the deletion of an existing flow

from OpenDaylight import OpenDaylight
from OpenDaylight import OpenDaylightFlow

# Initiate connection to the ODL controller
odl = OpenDaylight()
odl.setup['hostname'] = '127.0.0.1' # Replace with the ODL Controller IP addresss
odl.setup['username'] = 'admin' # User ID to login to the ODL Controller
odl.setup['password'] = 'admin' # Password to login to the ODL Controller

flow = OpenDaylightFlow(odl)

# User instructions
print('>> WARNING... You are about to remove a flow!')
flowName = raw_input('>> Enter the flow name: ')

# Delete flows
flow.delete('00:00:00:00:00:00:00:01', flowName + '1') # The first field is the ID of the node being used
flow.delete('00:00:00:00:00:00:00:02', flowName + '2') # The first field is the ID of the node being used

# Print success message
print('********************************')
print('>> SUCCESS... The following flows have been deleted:')
print('>> ' + flowName + '1 on switch #1')
print('>> ' + flowName + '2 on switch #2')
print('********************************')