# isEvenAPI

[![codecov](https://codecov.io/gh/ultirequiem/isEvenAPI/branch/main/graph/badge.svg)](https://codecov.io/gh/ultirequiem/isEvenAPI)

The premier Python package for checking the even-ness of a number via an API.
Built-ins are overrated, microservices are always best, regardless of scope. I
read it in a medium article, so...

> I did this when I was learning Python 😆

## Main features

- Cache Memorization ➿
- API Retry Handler ♻

## Install

From PyPI 🐍

```sh
pip install isEvenApi
```

Or from GitHub 🐱

```sh
pip install git+https:/github.com/UltiRequiem/isEvenAPI
```

## Usage

As simple as possible 🤗

```python
from is_even import is_even, is_odd, adverstiment

print(is_even(10)) # True
print(is_odd(10)) # False

print(adverstiment()) # An Advertisement
```

Check the [`examples/`](./examples) directory for more information.

## Alternatives

A simpler aproach 👇

```python
def is_even(number):
    return number % 2 == 0
```

## CLI Tool

The installation process is the same as before.

The normal way 🧐

```sh
is_even 6 2
True
True
```

Or with the verbose mode 🍹

```sh
is_even 6 2 --verbose
6 is even.
2 is even.
```

## Support

Open an Issue, I will check it a soon as possible 👀

If you want to hurry me up a bit
[send me a tweet](https://x.com/intent/tweet?text=%40UltiRequiem%20) 😆

Don't forget to star the repo ⭐

## Authors

[Eliaz Bobadilla (a.k.a UltiRequiem)](https://ultirequiem.com) - Creator and
Maintainer 💪

See also the full list of
[contributors](https://github.com/UltiRequiem/isEvenAPI/contributors) who
participated in this project.

## Versioning

We use [SemVer](http://semver.org) for versioning. For the versions available,
see the [tags](https://github.com/UltiRequiem/isEvenAPI/tags).

## Note

I did this because I'm learning how to upload packages to
[PYPI](https://pypi.org/project/isEvenAPI) with GitHub actions.

## Licence

Licensed under the MIT License.
