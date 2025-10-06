#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Goods:
    def __init__(
        self,
        name: str = "",
        date: str = "",
        price: float = 0.0,
        quantity: int = 0,
        number: int = 0,
    ) -> None:
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        if number < 0:
            raise ValueError("Номер накладной не может быть отрицательным")

        self.name: str = name
        self.date: str = date
        self.price: float = price
        self.quantity: int = quantity
        self.number: int = number

    def read(self) -> None:
        self.name = input("Введите наименование товара: ")
        self.date = input("Введите дату оформления: ")

        self.price = float(input("Введите цену товара: "))
        if self.price < 0:
            raise ValueError("Цена не может быть отрицательной")

        self.quantity = int(input("Введите количество единиц товара: "))
        if self.quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

        self.number = int(input("Введите номер накладной: "))
        if self.number < 0:
            raise ValueError("Номер накладной не может быть отрицательным")

    def display(self) -> None:
        print(f"Наименование: {self.name}")
        print(f"Дата оформления: {self.date}")
        print(f"Цена: {self.price}")
        print(f"Количество: {self.quantity}")
        print(f"Номер накладной: {self.number}")
        print(f"Общая стоимость: {self.total_cost()}")

    def change_price(self, amount: float) -> None:
        new_price = self.price + amount
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.price = new_price

    def change_quantity(self, amount: int) -> None:
        new_quantity = self.quantity + amount
        if new_quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        self.quantity = new_quantity

    def total_cost(self) -> float:
        return self.price * self.quantity
