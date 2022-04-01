import requests
from functools import lru_cache
from retry import retry

API_URL = "https://api.isevenapi.xyz/api/iseven"


@lru_cache(maxsize=None)
@retry(ConnectionError, tries=3, delay=2)
def raw_request(number: int):
    r = requests.get(f"{API_URL}/{number}")

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        raise Exception(r.json()["error"])


def is_even(number: int) -> bool:
    """
    Returns if it is even.
    """
    return raw_request(number)["iseven"]


def is_odd(number: int) -> bool:
    """
    Returns if it is odd.
    """
    return not is_even(number)


def adverstiment() -> str:
    """
    Returns and ad.
    """
    return raw_request(2)["ad"]
