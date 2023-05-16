from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    instance = Dish("Alexoa", 55.98)

    assert instance.name == "Alexoa"
    assert instance.price == 55.98
    assert instance.__repr__() == "Dish('Alexoa', R$55.98)"
    assert instance.__hash__() == hash("Dish('Alexoa', R$55.98)")
    assert instance == Dish("Alexoa", 55.98)

    instance.add_ingredient_dependency(Ingredient('cacau'), 5)

    assert instance.recipe == {Ingredient('cacau'): 5}
    assert not instance.get_restrictions()

    assert instance.get_ingredients() == {Ingredient('cacau')}

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Alexoa", "a")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero"
    ):
        Dish("Alexoa", -1)
