from ncclient import manager

HOST = 'ios-xe-mgmt.cisco.com'
# use the NETCONF port for your CSR1000V device
PORT = 10000
# use the user credentials for your CSR1000V device
USER = 'root'
PASS = 'D_Vay!_10&'

m = manager.connect(host=HOST, port=PORT, username=USER,
                    password=PASS, hostkey_verify=False,
                    device_params={'name': 'default'},
                    allow_agent=False, look_for_keys=False)

for i in m.server_capabilities:
    print i

schema = m.get_schema('ietf-ip')
print schema