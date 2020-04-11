import pytest

import hangman
from impl import nested, indexed, indexed_fns

@pytest.fixture(params=[ nested, indexed, indexed_fns ])
def subject(request):
    return request.param

def create_game(**kwargs):
    return hangman.Game(
        state = '',
        guessed = set([]),
        letters = set([]),
        guesses_left = 1
    )._replace(**kwargs)

def test_already_won(subject):
    given = create_game(state = 'won')
    assert given == subject.make_guess(given, 'm')

def test_already_lost(subject):
    given = create_game(state = 'lost')
    assert given == subject.make_guess(given, 'm')

def test_already_guessed(subject):
    given = create_game(guessed = set(['a']))

    assert given._replace(
        state = 'already_guessed'
    ) == subject.make_guess(given, 'a')

def test_winning_guess(subject):
    given = create_game(letters = set(['a']))

    assert given._replace(
        state = 'won',
        guessed = set(['a'])
    ) == subject.make_guess(given, 'a')

def test_losing_guess(subject):
    given = create_game(letters = set(['a']), guesses_left = 1)

    assert given._replace(
        state = 'lost',
        guessed = set(['b']),
        guesses_left = 0
    ) == subject.make_guess(given, 'b')

def test_bad_guess(subject):
    given = create_game(letters = set(['a']), guesses_left = 3)

    assert given._replace(
        state = 'bad_guess',
        guessed = set(['b']),
        guesses_left = 2
    ) == subject.make_guess(given, 'b')

def test_good_guess(subject):
    given = create_game(letters = set(['a', 'b']))

    assert given._replace(
        state = 'good_guess',
        guessed = set(['a'])
    ) == subject.make_guess(given, 'a')
