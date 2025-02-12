import pytest
import PokeService

def test_api():
    assert PokeService.getPokemonData("pikachu").json()["name"] == "pikachu"