#!/usr/bin/env python3
import jwt

PUBKEY_FILE = 'jwt-key.pub'
PRVKEY_FILE = 'jwt-key'
#IPADDR_FILE = '/sys/class/net/wlan0/address'

try:
    ipaddr = open(IPADDR_FILE).read().strip()
    claim = {"deviceId":ipaddr}
except:
    claim = {"deviceId":'my IP address goes here'}

print('claim:', claim)

prvkey = open(PRVKEY_FILE).read()
encoded = jwt.encode(claim, prvkey, algorithm="RS256")
print('encoded:', encoded)

pubkey = open(PUBKEY_FILE).read()
decoded = jwt.decode(encoded, pubkey, algorithms=["RS256"])
print('decoded:', decoded)

