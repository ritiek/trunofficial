# trunofficial

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
print(mobile.phone)
print(mobile.countrycode)
print(mobile.carrier)

house = human.address
print(house.city)
print(house.timezone)
```

For more methods, check out the Documentation.

## Disclaimer

This method of accessing Truecaller's database may stop working any moment. Use it at your own risk.

## License

`The MIT License`
