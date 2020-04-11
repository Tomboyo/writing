def make_guess(game, guess):
    if is_game_already_over(game):
        return game
    elif is_already_guessed(game, guess):
        return game._replace(state = 'already_guessed')
    elif is_winning_guess(game, guess):
        return game._replace(
            state = 'won',
            guessed = game.guessed.union({ guess }))
    elif is_losing_guess(game, guess):
        return game._replace(
            state = 'lost',
            guessed = game.guessed.union({ guess }),
            guesses_left = 0)
    elif is_good_guess(game, guess):
        return game._replace(
            state = 'good_guess',
            guessed = game.guessed.union({ guess }))
    else: # is bad guess
        return game._replace(
            state = 'bad_guess',
            guessed = game.guessed.union({ guess }),
            guesses_left = game.guesses_left - 1)

def is_game_already_over(game):
    return game.state in [ 'won', 'lost' ]

def is_already_guessed(game, guess):
    return guess in game.guessed

def is_winning_guess(game, guess):
    return game.letters.issubset(game.guessed.union({ guess }))

def is_losing_guess(game, guess):
    return guess not in game.letters and game.guesses_left == 1

def is_good_guess(game, guess):
    return guess in game.letters
