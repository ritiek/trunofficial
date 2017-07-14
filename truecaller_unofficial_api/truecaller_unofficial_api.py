"""
Unofficial API to the Truecaller phone number search

https://github.com/ritiek/truecaller-unofficial-api

MIT License

Copyright (c) 2017 Ritiek Malhotra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import urllib
import json

class search:
    """ Return a new search instance given a phone number.

    """
    def __init__(self, number):
        URL = 'https://search5.truecaller.com/v2/search?'

        raw_params = {
            'q': number,
            'countryCode': 'IN',
            'type': '4',
            'locAddr': '',
            'placement': 'SEARCHRESULTS,HISTORY,DETAILS',
            'clientId': '1',
            'myNumber': 'lS5757de85c2804a87d452c139OpYeO6gR6qlj0QFJJQMpo1',
            'registerId': '285661581',
            'encoding': 'json',
        }

        params = urllib.urlencode(raw_params)
        url_params = URL + params
        response = urllib.urlopen(url_params).read()
        parsed = json.loads(response)

        basic = parsed['data'][0]
        phone_parsed = parsed['data'][0]['phones'][0]
        address_parsed = parsed['data'][0]['addresses'][0]

        self.id = basic['id']
        self.name = basic['name']
        self.score = basic['score']
        self.access = basic['access']
        self.enhanced = basic['enhanced']
        self.internet_address = basic['internetAddresses']
        self.badges = basic['badges']
        self.tags = basic['tags']
        self.sources = basic['sources']

        self.phone = phone(phone_parsed)
        self.address = address(address_parsed)

        self.provider = parsed['provider']
        self.trace = parsed['trace']
        self.sourcestats = parsed['stats']['sourceStats']

class phone:
    """ Returns information about phone number. """
    def __init__(self, phone):
        self.phone = phone['e164Format']
        self.numbertype= phone['numberType']
        self.national = phone['nationalFormat']
        self.dialcode = phone['dialingCode']
        self.countrycode = phone['countryCode']
        self.carrier = phone['carrier']
        try:
            self.spamscore = phone['spamScore']
            self.spamtype = phone['spamType']
        except KeyError:
            self.spamscore = None
            self.spamtype = None
        self.phonetype = phone['type']

class address:
    """ Returns information about location. """
    def __init__(self, address):
        self.area = address['area']
        self.city = address['city']
        self.countrycode = address['city']
        self.timezone = address['timeZone']
        self.type = address['type']
