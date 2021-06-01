# coding=utf-8

"""
request module
"""
import requests
from functools import lru_cache
from retry import retry


API_URL = "https://api.isevenapi.xyz/api/iseven/"

@lru_cache(maxsize=None)
@retry(ConnectionError, tries=3, delay=2)
def is_even(number: int) -> bool:
    """Returns if it is even.

    :param number:
    :type number: int
    """
    r = requests.get(API_URL + str(number))

    if r.status_code == requests.codes.ok:
        return r.json()["iseven"]
    else:
        raise Exception(r.json()["error"])

def is_odd(number: int) -> bool:
    """Returns if it is odd.

    :param number:
    :type number: int
    """
    return not is_even(number)


def ad(number: int) -> str:
    """Returns and ad.

    :param number:
    :type number: int
    """
    r = requests.get(API_URL + str(number))
    return r.json()["ad"]


def ad_without_number() -> str:
    """Returns and ad."""

    r = requests.get(API_URL + str(2))
    return r.json()["ad"]
