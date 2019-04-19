class Product:

    # インスタンス変数
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    # インスタンスメソッド
    def discount(self, price):
        self.amount -= price
        # self.amount = self.amount price


if __name__ == "__main__":
    p1 = Product("iphone", 100000)  # Productクラスのインスタンス化
    print(p1)
    print(p1.name)  # name
    print(p1.amount)  # 100000
    p1.discount(5000)
    print(p1.amount)

    p2 = Product("MacBookAir", 150000)
    print(p2.name)
    print(p2.amount)
    p2.discount(9800)
    print(p2.amount)
