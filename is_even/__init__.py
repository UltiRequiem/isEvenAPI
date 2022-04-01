import requests
from functools import lru_cache
from retry import retry


API_URL = "https://api.isevenapi.xyz/api/iseven"


@lru_cache(maxsize=None)
@retry(ConnectionError, tries=3, delay=2)
def is_even(number: int) -> bool:
    """
    Returns if it is even.
    """
    r = requests.get(f"{API_URL}/{number}")

    if r.status_code == requests.codes.ok:
        return r.json()["iseven"]
    else:
        raise Exception(r.json()["error"])


def is_odd(number: int) -> bool:
    """
    Returns if it is odd.
    """
    return not is_even(number)


def adverstiment() -> str:
    """
    Returns and ad.
    """
    r = requests.get(f"{API_URL}/2")
    return r.json()["ad"]
