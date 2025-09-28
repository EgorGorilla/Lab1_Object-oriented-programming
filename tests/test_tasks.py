import pytest

from tasks.task1 import RightTrianglePair, make_right_triangle_pair
from tasks.task2 import Goods


class TestRightTrianglePair:
    def test_init_valid_values(self):
        triangle = RightTrianglePair(3, 4)
        assert triangle.first == 3
        assert triangle.second == 4

    def test_init_negative_first(self):
        with pytest.raises(
            ValueError, match="Катеты должны быть положительными числами"
        ):
            RightTrianglePair(-3, 4)

    def test_init_negative_second(self):
        with pytest.raises(
            ValueError, match="Катеты должны быть положительными числами"
        ):
            RightTrianglePair(3, -4)

    def test_hypotenuse_calculation(self):
        triangle = RightTrianglePair(3, 4)
        assert triangle.hypotenuse() == 5

    def test_make_right_triangle_pair_valid(self):
        triangle = make_right_triangle_pair(6, 8)
        assert triangle.first == 6
        assert triangle.second == 8

    def test_make_right_triangle_pair_invalid(self):
        with pytest.raises(
            ValueError, match="Катеты должны быть положительными числами"
        ):
            make_right_triangle_pair(0, 4)


class TestGoods:
    def test_init_valid_values(self):
        goods = Goods("Товар", "2024-01-15", 100.0, 10, 123)
        assert goods.name == "Товар"
        assert goods.date == "2024-01-15"
        assert goods.price == 100.0
        assert goods.quantity == 10
        assert goods.number == 123

    def test_init_negative_price(self):
        with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
            Goods("Товар", "2024-01-15", -100.0, 10, 123)

    def test_init_negative_quantity(self):
        with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
            Goods("Товар", "2024-01-15", 100.0, -10, 123)

    def test_init_negative_number(self):
        with pytest.raises(
            ValueError, match="Номер накладной не может быть отрицательным"
        ):
            Goods("Товар", "2024-01-15", 100.0, 10, -123)

    def test_change_price_positive(self):
        goods = Goods("Товар", "2024-01-15", 100.0, 10, 123)
        goods.change_price(50)
        assert goods.price == 150.0

    def test_change_price_negative_valid(self):
        goods = Goods("Товар", "2024-01-15", 100.0, 10, 123)
        goods.change_price(-30)
        assert goods.price == 70.0

    def test_change_price_negative_invalid(self):
        goods = Goods("Товар", "2024-01-15", 50.0, 10, 123)
        with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
            goods.change_price(-60)

    def test_change_quantity_positive(self):
        goods = Goods("Товар", "2024-01-15", 100.0, 10, 123)
        goods.change_quantity(5)
        assert goods.quantity == 15

    def test_change_quantity_negative_valid(self):
        goods = Goods("Товар", "2024-01-15", 100.0, 10, 123)
        goods.change_quantity(-3)
        assert goods.quantity == 7

    def test_change_quantity_negative_invalid(self):
        goods = Goods("Товар", "2024-01-15", 100.0, 5, 123)
        with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
            goods.change_quantity(-10)

    def test_total_cost(self):
        goods = Goods("Товар", "2024-01-15", 100.0, 5, 123)
        assert goods.total_cost() == 500.0
