# Python Pizza 
## RIP API
Unfortunately, it seems that the API has been closed. This means that it can no longer be used. I deeply regret this. 
RIP Domino's API


## Error Handling
Actually, the package should create such an object address. Unfortunately this is not possible. The same applies to the customer. Unfortunately, the object cannot be created either. 

```Python 
def create_address(adr, city, state, plz):
    return Address(adr, city, state, plz)
```

This is a great pity, because these are an elementary part of.


```Python 
create_address(adr, city, state, plz)
create_customer(first_name, name, EMail, Number)
```

## Example
In the test file you can view a complete order once. Look here: [TestOrder.py](test.py).
But unfortunately, it is already clear that it will not work. 

## GitHub 
Here you can show the basic Git. Maybe you can solve the problems. 
[Base Git](https://github.com/ggrammar/pizzapi/)


## PIP Dependencies
Please install the PIP dependencies.

```PowerShell
pip install -r requirements.txt
```

## Syntax
First construct a ``Customer`` object and set the customer's address:

```python

    customer = Customer('Barack', 'Obama', 'barack@whitehouse.gov', '2024561111', '700 Pennsylvania Avenue NW, Washington, DC, 20408')
```
Then, find a store that will deliver to the address.

```python

    my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
```

In order to add items to your order, you'll need the items' product codes.
To find the codes, get the menu from the store, then search for items you want to add.
You can do this by asking your ``Store`` object for its ``Menu``.

``` Python

    menu = my_local_dominos.get_menu()
```

Then search ``menu`` with ``menu.search``. For example, running this command:

.. code-block:: python

    menu.search(Name='Coke')

Should print this to the console:

.. code-block:: text

    20BCOKE    20oz Bottle Coke®        $1.89
    20BDCOKE   20oz Bottle Diet Coke®   $1.89
    D20BZRO    20oz Bottle Coke Zero™   $1.89
    2LDCOKE    2-Liter Diet Coke®       $2.99
    2LCOKE     2-Liter Coke®            $2.99

After you've found your items' product codes, you can create an ``Order`` object add add your items:

.. code-block:: python

    order = Order.begin_customer_order(customer, my_local_dominos)
    order.add_item('P12IPAZA') # add a 12-inch pan pizza
    order.add_item('MARINARA') # with an extra marinara cup
    order.add_item('20BCOKE')  # and a 20oz bottle of coke

You can remove items as well!

.. code-block:: python

    order.remove_item('20BCOKE')

Wrap your credit card information in a ``CreditCard``:

.. code-block:: python

    card = CreditCard('4100123422343234', '0115', '777', '90210')

And that's it! Now you can place your order.

.. code-block:: python

    order.place(card)
    my_local_dominos.place_order(order, card)
