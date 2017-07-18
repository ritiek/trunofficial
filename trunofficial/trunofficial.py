try:
    from urllib import urlopen
    from urllib import urlencode
except ImportError:
    from urllib.request import urlopen
    from urllib.parse import urlencode
import json


class TruecallerError(Exception):
    def __init__(self, message=None):
        super().__init__(message)

class search:
    def __init__(self, number):
        URL = 'https://search5.truecaller.com/v2/search?'

        raw_params = {
            'q': number,
            'type': '4',
            'locAddr': '',
            'placement': 'SEARCHRESULTS,HISTORY,DETAILS',
            'clientId': '1',
            'myNumber': 'lS5757de85c2804a87d452c139OpYeO6gR6qlj0QFJJQMpo1',
            'registerId': '568140610',
            'encoding': 'json',
        }

        params = urlencode(raw_params)
        url_params = URL + params
        response = urlopen(url_params).read()
        response = response.decode('utf-8')
        parsed = json.loads(response)

        try:
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

        except KeyError:
            raise TruecallerError("Cannot find the number in Truecaller database.")


class phone:
    def __init__(self, phone):
        self.number = phone['e164Format']
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
    def __init__(self, address):
        self.area = address['area']
        self.city = address['city']
        self.countrycode = address['countryCode']
        self.timezone = address['timeZone']
        self.type = address['type']
