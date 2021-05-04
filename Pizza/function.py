# Funtion PyPizza
import urllib3
from  pizzapi import * 

# Test Network
def test_network():
    try:
        urllib2.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib2.URLError as err:
        return False

# Test String
def test_string(x):
    if len(x) == 0 or type(x) is str:
        return False
    else:
        return True

# Create User Config as Object
def create_customer(first, name, mail, tele):
        return pizzapi.Customer(first, name, mail, tele)


# Create Adress Config as Object
def create_address(adr, city, state, plz):
    return Address(adr, city, state, plz)


# Create store
def create_store():
    return closest_store()