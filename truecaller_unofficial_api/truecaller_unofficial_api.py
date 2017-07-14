import urllib
import json

class search:
    """ Return a new search instance given a phone number.

    Attributes:
        |id                  The truecaller id of the user.
        |name                The name of the owner of the phone number.
        |score               The score of the user.
        |access              The public accessibility state of the user.
        |enhanced            The enhanced state of the user.
        |internet_address    The internet address of the user.
        |badges              The badges owned by the user.
        |tags                The tags of the user.
        |sources             The sources available.
        |provider            The provider of the phone number.
        |trace               The trace of the user.
        |sourcestats         The source stats of the user.
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
    """ Returns information about phone number.

    Attributes:
        |phone               The phone number of the user.
        |numbertype          The type of phone number.
        |national            The phone number in national form.
        |dialcode            The dial code of the country.
        |carrier             The carrier of the phone number.
        |spamscore           The spam score of the user.
        |spamtype            The spam type of the user.
        |phonetype           The phone type of the user.
    """
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
    """ Returns information about location.

    Attributes:
        |area                The area where the phone number resides.
        |city                The city where the phone number resides.
        |countrycode         The country code of the location.
        |timezone            The time zone of the location.
        |type                The type of location.
    """
    def __init__(self, address):
        self.area = address['area']
        self.city = address['city']
        self.countrycode = address['city']
        self.timezone = address['timeZone']
        self.type = address['type']
