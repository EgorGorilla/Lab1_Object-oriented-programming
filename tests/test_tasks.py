import pytest

from tasks.goods_model import Goods
from tasks.triangle_model import RightTrianglePair, make_right_triangle_pair


# Tests for RightTrianglePair
def test_right_triangle_pair_init_valid_values():
    triangle = RightTrianglePair(3, 4)
    assert triangle.first == 3
    assert triangle.second == 4


def test_right_triangle_pair_init_negative_first():
    with pytest.raises(ValueError, match="Катеты должны быть положительными числами"):
        RightTrianglePair(-3, 4)


def test_right_triangle_pair_init_negative_second():
    with pytest.raises(ValueError, match="Катеты должны быть положительными числами"):
        RightTrianglePair(3, -4)


def test_right_triangle_pair_init_zero_first():
    with pytest.raises(ValueError, match="Катеты должны быть положительными числами"):
        RightTrianglePair(0, 4)


def test_right_triangle_pair_init_zero_second():
    with pytest.raises(ValueError, match="Катеты должны быть положительными числами"):
        RightTrianglePair(3, 0)


def test_right_triangle_pair_hypotenuse_calculation():
    triangle = RightTrianglePair(3, 4)
    assert triangle.hypotenuse() == 5


def test_right_triangle_pair_hypotenuse_calculation_other_values():
    triangle = RightTrianglePair(6, 8)
    assert triangle.hypotenuse() == 10


def test_make_right_triangle_pair_valid():
    triangle = make_right_triangle_pair(6, 8)
    assert triangle.first == 6
    assert triangle.second == 8


def test_make_right_triangle_pair_invalid():
    with pytest.raises(ValueError, match="Катеты должны быть положительными числами"):
        make_right_triangle_pair(0, 4)


# Tests for Goods
def test_goods_init_valid_values():
    goods = Goods("Товар", "2024-01-15", 100.0, 10, 123)
    assert goods.name == "Товар"
    assert goods.date == "2024-01-15"
    assert goods.price == 100.0
    assert goods.quantity == 10
    assert goods.number == 123


def test_goods_init_negative_price():
    with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
        Goods("Товар", "2024-01-15", -100.0, 10, 123)


def test_goods_init_negative_quantity():
    with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
        Goods("Товар", "2024-01-15", 100.0, -10, 123)


def test_goods_init_negative_number():
    with pytest.raises(ValueError, match="Номер накладной не может быть отрицательным"):
        Goods("Товар", "2024-01-15", 100.0, 10, -123)


def test_goods_init_zero_values():
    goods = Goods("Товар", "2024-01-15", 0.0, 0, 0)
    assert goods.price == 0.0
    assert goods.quantity == 0
    assert goods.number == 0


def test_goods_change_price_positive():
    goods = Goods("Товар", "2024-01-15", 100.0, 10, 123)
    goods.change_price(50)
    assert goods.price == 150.0


def test_goods_change_price_negative_valid():
    goods = Goods("Товар", "2024-01-15", 100.0, 10, 123)
    goods.change_price(-30)
    assert goods.price == 70.0


def test_goods_change_price_negative_invalid():
    goods = Goods("Товар", "2024-01-15", 50.0, 10, 123)
    with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
        goods.change_price(-60)


def test_goods_change_price_to_zero():
    goods = Goods("Товар", "2024-01-15", 50.0, 10, 123)
    goods.change_price(-50)
    assert goods.price == 0.0


def test_goods_change_quantity_positive():
    goods = Goods("Товар", "2024-01-15", 100.0, 10, 123)
    goods.change_quantity(5)
    assert goods.quantity == 15


def test_goods_change_quantity_negative_valid():
    goods = Goods("Товар", "2024-01-15", 100.0, 10, 123)
    goods.change_quantity(-3)
    assert goods.quantity == 7


def test_goods_change_quantity_negative_invalid():
    goods = Goods("Товар", "2024-01-15", 100.0, 5, 123)
    with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
        goods.change_quantity(-10)


def test_goods_change_quantity_to_zero():
    goods = Goods("Товар", "2024-01-15", 100.0, 5, 123)
    goods.change_quantity(-5)
    assert goods.quantity == 0


def test_goods_total_cost():
    goods = Goods("Товар", "2024-01-15", 100.0, 5, 123)
    assert goods.total_cost() == 500.0


def test_goods_total_cost_zero_quantity():
    goods = Goods("Товар", "2024-01-15", 100.0, 0, 123)
    assert goods.total_cost() == 0.0


def test_goods_total_cost_zero_price():
    goods = Goods("Товар", "2024-01-15", 0.0, 5, 123)
    assert goods.total_cost() == 0.0
