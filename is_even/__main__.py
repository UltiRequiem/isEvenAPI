import typer
from typing import List

from . import is_even


def main(numbers: List[int], verbose: bool = typer.Option(False, "--verbose", "-v")):
    for number in numbers:
        result = is_even(number)
        typer.echo(
            f"{number} is {'even' if  result else 'odd'}." if verbose else result
        )


if __name__ == "__main__":
    typer.run(main)
