from ncclient import manager
import xml.etree.ElementTree as ET

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

schema = m.get_schema('ietf-ip')
print schema

root = ET.fromstring(schema.xml)
yang_text = list(root)[0].text
with open('ietf-ip.yang', 'w') as f:
    f.write(yang_text)
#write_file('ietf-ip.yang', yang_text)