import requests
import sys

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    pokemon = response.json()

    hp = pokemon["stats"][0]["base_stat"]
    hp_str = f"{hp}/{hp}"
    moves = ", ".join(move_data["move"]["name"] for move_data in pokemon["moves"])
    held_items = ", ".join(item["item"]["name"] for item in pokemon["held_items"])
    
    print("Name:", pokemon["name"])
    print("HP:", hp_str)
    print("Attacks:", moves)
    print("Held Items:", held_items)

def main():
    if len(sys.argv) != 7:
        print("Usage: python script.py <pokemon_name1> <pokemon_name2> <pokemon_name3> <pokemon_name4> <pokemon_name5> <pokemon_name6>")
    else:
        pokemon_names = sys.argv[1:]
        for name in pokemon_names:
            search_pokemon(name)

if __name__ == "__main__":
    main()

# sample line python3 pokedex2.py charmander bulbasaur pikachu squirtle jigglypuff meowth