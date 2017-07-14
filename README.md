# truecaller-unofficial-api

 Unofficial API to the Truecaller phone number search.

## Installation

 ```
 pip install truecaller-unoffical-api
 ```

or if you like to live on the bleeding edge:

```
python setup.py install
```

## Usage Examples

```
import truecaller_unofficial_api as tr

human = tr.search('<phone number>')
print(human.name)

mobile = human.phone
print(mobile.phone)
print(mobile.countrycode)
print(mobile.carrier)

house = human.address
print(house.city)
print(house.timezone)
```

For more methods, check out the Documentation.

## Disclaimer

This method of accessing Truecaller's database may stop working any day. Use it at your own risk.

## License

`The MIT License`
