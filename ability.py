import requests
import pokebase as pb

def ability(pokemonname):
    abilities = []
    pokemonname = pb.APIResource('pokemon', pokemonname)
    for i in range(len(pokemonname.abilities)):
        abilities.append(pokemonname.abilities[i].ability.name)
    return abilities