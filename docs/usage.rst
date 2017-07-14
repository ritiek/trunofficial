Usage Examples
==============

A basic example that shows this library in action.

    >>> import truecaller_unofficial as tr

    >>> human = tr.search('<phone number>')
    >>> print(human.name)

    >>> mobile = human.phone
    >>> print(mobile.phone)
    >>> print(mobile.countrycode)
    >>> print(mobile.carrier)

    >>> house = human.address
    >>> print(house.city)
    >>> print(house.timezone)

.. include:: global.rst
