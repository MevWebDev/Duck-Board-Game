import pickle
def load_game_state(filename):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f), True
    except FileNotFoundError:
        return {}, False

def save_game_state(game_state, filename):
    with open(filename, 'wb') as f:
        pickle.dump(game_state, f)