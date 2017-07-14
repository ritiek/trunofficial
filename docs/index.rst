truecaller-unofficial-api
=========================

Unofficial API to the Truecaller phone number search.

Usage Examples

    import truecaller_unofficial as tr

    human = tr.search('<phone number>')
    print(human.name)

    mobile = human.phone
    print(mobile.phone)
    print(mobile.countrycode)
    print(mobile.carrier)

    house = human.address
    print(house.city)
    print(house.timezone)

Installation
------------

Install truecaller-unofficial-api by running:

    pip install truecaller-unofficial-api

or if you like to live on the bleeding edge:

    python setup.py install

Contribute
----------

- Issue Tracker: https://github.com/ritiek/truecaller-unofficial-api/issues
- Source Code: https://github.com/ritiek/truecaller-unofficial-api

Support
-------

If you are having issues, please let us know.

License
-------

MIT
