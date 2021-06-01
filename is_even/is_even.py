# coding=utf-8

"""
request module
"""
from requests import get


API_URL = "https://api.isevenapi.xyz/api/iseven/"


def is_even(number: int) -> bool:
    """Returns if it is even.

    :param number:
    :type number: int
    """
    r = get(API_URL + str(number))
    return r.json()["iseven"]


def is_odd(number: int) -> bool:
    """Returns if it is odd.

    :param number:
    :type number: int
    """
    return not is_even(number)
