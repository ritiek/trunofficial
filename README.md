# trunofficial

[![pypi.python.org](https://img.shields.io/pypi/v/trunofficial.svg)](https://pypi.org/project/trunofficial/) [![readthedocs.org](https://readthedocs.org/projects/trunofficial/badge/?version=latest)](http://trunofficial.readthedocs.io/en/latest/) [![build Status](https://travis-ci.org/ritiek/trunofficial.svg?branch=master)](https://travis-ci.org/ritiek/trunofficial/)

 Unofficial API to the Truecaller phone number search.

## Installation

 ```
 pip install trunofficial
 ```

or if you like to live on the bleeding edge:

```
python setup.py install
```

## Usage Examples

```
import trunofficial

owner = trunofficial.search('2024561111')
print(owner.name)

mobile = owner.phone
print(mobile.number)
print(mobile.countrycode)
print(mobile.carrier)

house = owner.address
print(house.city)
print(house.timezone)
```

For more methods, check out the [Documentation](http://trunofficial.readthedocs.io/en/latest/).

## Running Tests

```
python -m pytest test
```

## Disclaimer

This method of accessing Truecaller's database may stop working any moment. Use it at your own risk.

## License

`The MIT License`
