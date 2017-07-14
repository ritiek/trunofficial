Usage Examples
==============

A basic example that shows this library in action.


Import the module

    >>> import truecaller_unofficial as tr

Search for a phone number

    >>> human = tr.search('<phone number>')
    >>> print(human.name)

Information on phone number

    >>> mobile = human.phone
    >>> print(mobile.phone)
    >>> print(mobile.countrycode)
    >>> print(mobile.carrier)

Information on location

    >>> house = human.address
    >>> print(house.city)
    >>> print(house.timezone)

.. include:: global.rst
