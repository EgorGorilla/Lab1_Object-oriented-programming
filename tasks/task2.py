class Goods:
    def __init__(self, name="", date="", price=0.0, quantity=0, number=0):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        if number < 0:
            raise ValueError("Номер накладной не может быть отрицательным")

        self.name = name
        self.date = date
        self.price = price
        self.quantity = quantity
        self.number = number

    def read(self):
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

    def display(self):
        print(f"Наименование: {self.name}")
        print(f"Дата оформления: {self.date}")
        print(f"Цена: {self.price}")
        print(f"Количество: {self.quantity}")
        print(f"Номер накладной: {self.number}")
        print(f"Общая стоимость: {self.total_cost()}")

    def change_price(self, amount):
        new_price = self.price + amount
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.price = new_price

    def change_quantity(self, amount):
        new_quantity = self.quantity + amount
        if new_quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        self.quantity = new_quantity

    def total_cost(self):
        return self.price * self.quantity


if __name__ == "__main__":
    goods = Goods()
    goods.read()
    goods.display()

    goods.change_price(100)
    goods.change_quantity(5)
    print("\nПосле увеличения цены и количества:")
    goods.display()
