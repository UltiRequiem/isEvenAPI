# isEven.py

Check if an integer is even using the [isEven API](https://isevenapi.xyz).

## Main features

- Cache Memorization
- API Retry Handler
- Hide Ads
- Get just the Ads

## Install

```sh
pip install isEvenApi
```

Or from GitHub 🐱

```sh
pip install git+https:/github.com/UltiRequiem/isEvenAPI
```

## Usage

```python
from is_even import is_even, is_odd, adverstiment

print(is_even(10)) # True
print(is_odd(10)) # False

print(adverstiment()) # An Advertisement
```

## Alternatives

This is a simpler aproach 👇

```python
def is_even(number):
    return number % 2 == 0
```

### Note

I did this because I'm learning how to upload packages to
[PYPI](https://pypi.org/project/isEvenAPI) with GitHub actions.
