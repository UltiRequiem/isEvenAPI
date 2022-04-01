# isEvenAPI

The premier Python package for checking the even-ness of a number via an
API. Built-ins are overrated, microservices are always best,
regardless of scope. I read it in a medium article, so...

## Main features

- Cache Memorization
- API Retry Handler

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

## Support

Open an Issue, I will check it a soon as possible 👀

If you want to hurry me up a bit
[send me a tweet](https://twitter.com/intent/tweet?text=%40UltiRequiem%20) 😆

Consider [supporting me on Patreon](https://patreon.com/UltiRequiem) if you
like my work 🚀

Don't forget to start the repo ⭐

## Versioning

We use [SemVer](http://semver.org) for versioning.
For the versions available, see the
[tags](https://github.com/UltiRequiem/REPO/tags).

## Note

I did this because I'm learning how to upload packages to
[PYPI](https://pypi.org/project/isEvenAPI) with GitHub actions.

## Licence

Licensed under the MIT License.
