import trunofficial

owner = trunofficial.search('2024561111', cc='IN')
owners = trunofficial.search('2067093100', '2024561111', cc='IN')

def test_basic():
    assert owner.id == 'uLByRJydv5fh+1nHPzemqg=='
    assert owner.name == 'Obama'
    assert owner.access == 'PUBLIC'
    assert owner.enhanced == True
    assert owner.internet_address == []
    assert owner.badges == []
    assert owner.tags == ['3', '41']
    assert owner.sources == []

def test_phone():
    mobile = owner.phone
    assert mobile.number == '+912024561111'
    assert mobile.numbertype == 'FIXED_LINE'
    assert mobile.carrier == 'BSNL'


def test_address():
    house = owner.address
    assert house.area == 'Pune, Maharashtra'
    assert house.city == 'Pune, Maharashtra'
    assert house.timezone == 'GMT+05:30'

def test_multiple():
    assert owner.name == owners[1].name
