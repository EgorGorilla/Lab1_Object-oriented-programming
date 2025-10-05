from math import sqrt


class RightTrianglePair:
    def __init__(self, first: float = 1, second: float = 1):
        if first <= 0 or second <= 0:
            raise ValueError("Катеты должны быть положительными числами")

        self.__first = float(first)
        self.__second = float(second)

    def read(self):
        self.__first = float(input("Введите первый катет: "))
        self.__second = float(input("Введите второй катет: "))

        if self.__first <= 0 or self.__second <= 0:
            raise ValueError("Катеты должны быть положительными числами")

    def display(self):
        print(f"Первый катет: {self.__first}")
        print(f"Второй катет: {self.__second}")
        print(f"Гипотенуза: {self.hypotenuse():.2f}")

    @property
    def first(self):
        return self.__first

    @property
    def second(self):
        return self.__second

    def hypotenuse(self):
        return sqrt(self.__first**2 + self.__second**2)


def make_right_triangle_pair(first: float, second: float) -> RightTrianglePair:
    if first <= 0 or second <= 0:
        raise ValueError("Катеты должны быть положительными числами")
    return RightTrianglePair(first, second)
