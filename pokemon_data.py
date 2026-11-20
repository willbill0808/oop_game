# One move per pokemon, all power 10, so type matchups decide fights.
MOVES = {
    "water gun":  {"element": "water",  "power": 10},
    "bubble":     {"element": "water",  "power": 30},
    "ember":      {"element": "fire",   "power": 10},
    "flame wisp": {"element": "fire",   "power": 30},
    "vine whip":  {"element": "nature", "power": 10},
    "leaf cut":   {"element": "nature", "power": 30},
}


Pokemon_data = {
    "squirtle":   {"PokeId": 1, "element": "water",  "moves": ["water gun"], "base_stats": {"hp": 42, "attack": 10, "defense": 13, "speed": 9},  "starter": True},
    "psyduck":    {"PokeId": 2, "element": "water",  "moves": ["bubble"], "base_stats": {"hp": 38, "attack": 13, "defense": 8,  "speed": 11}},
    "charmander": {"PokeId": 3, "element": "fire",   "moves": ["ember"], "base_stats": {"hp": 38, "attack": 14, "defense": 8,  "speed": 10}, "starter": True},
    "vulpix":     {"PokeId": 4, "element": "fire",   "moves": ["flame wisp"], "base_stats": {"hp": 36, "attack": 11, "defense": 9,  "speed": 12}},
    "bulbasaur":  {"PokeId": 5, "element": "nature", "moves": ["vine whip"], "base_stats": {"hp": 44, "attack": 10, "defense": 12, "speed": 10}, "starter": True},
    "oddish":     {"PokeId": 6, "element": "nature", "moves": ["leaf cut"], "base_stats": {"hp": 40, "attack": 12, "defense": 9,  "speed": 11}},
}