# Order a Pizza with Python
from pizzapi import *
import function

# Define User Data
first_name = "DATA"
name = "DATA"
EMail = "DATA"
Number = "DATA"

# Define Customer
adr = "DATA"
city = "DATA"
state = "DATA"
plz = "DATA"

# create Objects
create_address(adr, city, state, plz)
create_customer(first_name, name, EMail, Number)

# Test network
if test_network: 
    print("online")
else: 
    print("offline")
    quit()

# Check next store
print(function.create_store())



