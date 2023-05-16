from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    instance = Ingredient("farinha")

    assert instance.name == "farinha"
    assert instance.restrictions

    assert instance.__hash__() == hash("farinha")

    assert instance.__repr__() == "Ingredient('farinha')"

    assert instance == Ingredient("farinha")

    instance_2 = Ingredient("Carro")

    assert not instance_2.restrictions
