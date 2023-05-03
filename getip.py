#!/usr/bin/python3
# coding: utf8
import os, json
from urllib.request import urlopen

### By: Argon3x
### Suportted: Debian Based Systems and Termux
### Version: 1.0

# Colors
green = "\033[01;32m"
blue = "\033[01;34m"
red = "\033[01;31m"
purple = "\033[01;35m"
end = "\033[00m"

# Get and process data from the url
url = 'https://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

# Geting Details
IP_PUBLIC = data["ip"]
HOSTNAME = data["hostname"]
CITY = data["city"]
REGION = data["region"]
COUNTRY = data["country"]
LOCATION = data["loc"]
ORG = data["org"]
POSTAL = data["postal"]
TIMEZONE = data["timezone"]
README = data["readme"]

# Show Details
print(f"{blue}-" * 33)
print(f"{purple}   Details about the IP public{end}")
print(f"{blue}-" * 33)
print(f"{blue}IP Public{red}: {green}{IP_PUBLIC}{end}")
#print(f"{blue}Hostname{red}: {green}{HOSTNAME}{end}")
print(f"{blue}City{red}: {green}{CITY}{end}")
#print(f"{blue}Region{red}: {green}{REGION}{end}")
print(f"{blue}Country{red}: {green}{COUNTRY}{end}")
print(f"{blue}Location{red}: {green}{LOCATION}{end}")
#print(f"{blue}Org{red}: {green}{ORG}{end}")
#print(f"{blue}Postal{red}: {green}{POSTAL}{end}")
print(f"{blue}Timezone{red}: {green}{TIMEZONE}{end}")
#print(f"{blue}Readme{red}: {green}{README}{end}")
print(f"{blue}-" * 33)

