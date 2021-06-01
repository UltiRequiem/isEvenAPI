# isEven.py

<p>
<a href="https://github.com/UltiRequiem/isEven.py/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://pypi.org/project/isevenapi"><img alt="PyPI" src="https://img.shields.io/pypi/v/isevenapi"></a>
<a href="https://pepy.tech/project/isevenapi"><img alt="Downloads" src="https://pepy.tech/badge/isevenapi"></a>
<a href="https://github.com/UltiRequiem/isEven.py"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

Check if an integer is even using the [isEven API](https://isevenapi.xyz).

## Main features:

- Cache Memorization
- API Retry Handler
- Hide Ads
- Get just the Ads

## Install

```bash
pip install isEvenApi
```

## Usage

You can view some examples in [examples](https://github.com/UltiRequiem/isEven.py/tree/main/examples).
Basic Usage:

```python
from is_even import is_even as ie

print(ie.is_even(10)) # True
print(ie.is_odd(10)) # False

print(ie.ad(78)) # An Ad
print(ie.ad_without_number()) # An Ad without passing a number
```

### Alternatives

This Function:

```python
def is_even(number):
    return False if number & 1 else True
```

Or This other:

```python
def is_even(number):
    return False if number % 2 else True
```

Or a longer one:

```python
def is_even(number):
    if number % 2:
        return False
    else:
        return True
```

### Note:

I did this because I'm learning how to upload packages to [PYPI](https://pypi.org/project/isEvenAPI) with GitHub actions.
