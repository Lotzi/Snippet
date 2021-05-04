from pizzapi import *
customer = Customer('Donald', 'Trump', 'donald@whitehouse.gov', '2024561111')
address = Address('700 Pennsylvania Avenue NW', 'Washington', 'DC', '20408')
store = address.closest_store()
menu = store.get_menu()
print(menu.search(Name='Coke'))
