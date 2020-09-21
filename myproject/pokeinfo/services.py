import requests


def get_pokemon(name):
    """
    Fetch and process Pokemon data from an PokeAPI.
    """
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(f"{base_url}{name}")
    pokemon = response.json()
    pokemon_info = {
        "name": pokemon["name"].capitalize(),
        "base_experience": pokemon["base_experience"],
        "height": pokemon["height"],
        "weight": pokemon["weight"],
        "abilities": get_custom_abilities(pokemon["abilities"]),
        "sprites": get_pokemon_img(pokemon["sprites"]),
        "stats": get_custom_stats(pokemon["stats"]),
        "types": get_custom_types(pokemon["types"]),
    }
    return pokemon_info


def get_custom_abilities(abilities):
    """
    Return list of abilities.
    """
    abilities_list = []
    for item in abilities:
        ability = item["ability"]["name"]
        abilities_list.append(ability)
    return abilities_list


def get_pokemon_img(sprites):
    """
    Return list with two images urls.
    """
    return [sprites["front_default"], sprites["back_default"]]


def get_custom_stats(stats):
    """
    Return list stat name and value.
    """
    stats_list = []
    for item in stats:
        stats_list.append([item["stat"]["name"], item["base_stat"]])
    return stats_list


def get_custom_types(types):
    """
    Return list of Pokemon types.
    """
    types_list = []
    for item in types:
        types_list.append(item["type"]["name"])
    return types_list





