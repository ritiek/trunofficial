trunofficial
============

|pypi.python.org| |readthedocs.org| |build Status|

Unofficial API to the Truecaller phone number search.

Installation
------------

::

    pip install trunofficial

or if you like to live on the bleeding edge:

::

    python setup.py install

Command-line Usage
------------------

::

    usage: trunofficial [-h] [-c COUNTRYCODE] [NUMBER [NUMBER ...]]

    Unofficial API to the Truecaller phone number search.

    positional arguments:
      NUMBER                phone numbers to lookup on Truecaller

    optional arguments:
      -h, --help            show this help message and exit
      -c COUNTRYCODE, --countrycode COUNTRYCODE
                            prioritize search by country

Example:

::

    $ trunofficial 2024561111

Library Usage
-------------

.. code:: python

    >>> import trunofficial

    >>> owner = trunofficial.search('2024561111')
    >>> print(owner.name)

    >>> mobile = owner.phone
    >>> print(mobile.number)
    >>> print(mobile.countrycode)
    >>> print(mobile.carrier)

    >>> house = owner.address
    >>> print(house.city)
    >>> print(house.timezone)

For more examples, check the `examples directory <examples>`__ or read
the full
`Documentation <http://trunofficial.readthedocs.io/en/latest/>`__.

Running Tests
-------------

::

    python -m pytest test

Disclaimer
----------

This method of accessing Truecaller's database may stop working any
moment. Use it at your own risk.

License
-------

``The MIT License``

.. |pypi.python.org| image:: https://img.shields.io/pypi/v/trunofficial.svg
   :target: https://pypi.org/project/trunofficial/
.. |readthedocs.org| image:: https://readthedocs.org/projects/trunofficial/badge/?version=latest
   :target: http://trunofficial.readthedocs.io/en/latest/
.. |build Status| image:: https://travis-ci.org/ritiek/trunofficial.svg?branch=master
   :target: https://travis-ci.org/ritiek/trunofficial/
