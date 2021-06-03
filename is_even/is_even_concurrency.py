# coding=utf-8

import asyncio
import time
import requests
from functools import lru_cache
from retry import retry


API_URL = "https://api.isevenapi.xyz/api/iseven/"


@lru_cache(maxsize=None)
@retry(ConnectionError, tries=3, delay=2)
async def is_even(session, number: int) -> bool:
    r = requests.get(API_URL + str(number))
    async with session as session:
        if r.status_code == requests.codes.ok:
            return r.json()["iseven"]
        else:
            raise Exception(r.json()["error"])


def is_odd(session, number: int) -> bool:
    return not is_even(session, number)


async def ad(session, number: int) -> str:
    async with session as session:
        r = requests.get(API_URL + str(number))
        return r.json()["ad"]


async def ad_without_number(session) -> str:

    async with session as session:
        r = requests.get(API_URL + str(2))
        return r.json()["ad"]
