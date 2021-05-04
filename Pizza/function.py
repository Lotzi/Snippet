# Funtion PyPizza
import urllib3

# Test Network
def test_network():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
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
    if test_string([first, name, mail, tele]):
        return Customer(first, name, mail, tele)
    else:
        return False


# Create Adress Config as Object
def create_adress(adr, city, state, plz):
    return Address(adr, city, state, plz)
