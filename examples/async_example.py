import asyncio
from is_even import is_even_async as ie

def main(number):
    ie.is_even(number)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main(8))
