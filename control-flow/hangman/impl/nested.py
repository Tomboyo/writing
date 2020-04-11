def make_guess(game, guess):
    if game.state not in ['won', 'lost']:
        return accept_guess(game, guess)
    else:
        return game

def accept_guess(game, guess):
    if guess in game.guessed:
        return game._replace(state = 'already_guessed')
    else:
        game = game._replace(guessed = game.guessed.union({ guess }))
        return score_guess(game, guess)

def score_guess(game, guess):
    if guess in game.letters:
        return maybe_won(game)
    else:
        if game.guesses_left == 1:
            return game._replace(
                guesses_left = 0,
                state = 'lost')
        else:
            return game._replace(
                guesses_left = game.guesses_left - 1,
                state = 'bad_guess')

def maybe_won(game):
    if game.letters.issubset(game.guessed):
        return game._replace(state = 'won')
    else:
        return game._replace(state = 'good_guess')
