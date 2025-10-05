from goods_model import Goods

if __name__ == "__main__":
    goods = Goods()
    goods.read()
    goods.display()

    goods.change_price(100)
    goods.change_quantity(5)
    print("\nПосле увеличения цены и количества:")
    goods.display()
