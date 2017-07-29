# Created by N3V0N <navanchauhan@gmail.com>

import trunofficial
import sys

if sys.version_info > (3, 0):
    raw_input = input

response = raw_input("Please enter the number : ")

owner = trunofficial.search(response)
mobile = owner.phone
house = owner.address

print("Owner Name    : ", owner.name)
print("Mobile Number : ", mobile.number)
print("Country Code  : ", mobile.countrycode)
print("City          : ", house.city)
print("Area          : ", house.area)
print("Mobile Carrier: ", mobile.carrier)
print("TimeZone      : ", house.timezone)
print("Score         : ", owner.score)
print("Spam Score    : ", mobile.spamscore)
print("Spam Type     : ", mobile.spamtype)
print("Phone Type    : ", mobile.phonetype)
print("Owner ID      : ", owner.id)
print("Access        : ", owner.access)
print("Enhanced      : ", owner.enhanced)
print("Internet Addr.: ", owner.internet_address)
print("Badges        : ", owner.badges)
print("Tags          : ", owner.tags)
print("Owner Sources : ", owner.sources)
