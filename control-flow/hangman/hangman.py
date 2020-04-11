from typing import NamedTuple

class Game(NamedTuple):
    state: str
    guessed: set
    letters: set
    guesses_left: int
