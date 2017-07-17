import trunofficial

owner = trunofficial.search('2024561111')

def test_basic():
    assert owner.id == 'uLByRJydv5fh+1nHPzemqg=='
    assert owner.name == 'Obama'
    assert owner.access == 'PUBLIC'
    assert owner.enhanced == True
    assert owner.internet_address == []
    assert owner.badges == []
    assert owner.tags == ['4', '51']
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
