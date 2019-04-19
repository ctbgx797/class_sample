class Product:

    # インスタンス変数
    def __init__(self, name, amount, discount):
        self.name = name
        self.amount = amount
        self.discount = amount - discount


if __name__ == "__main__":
    p1 = Product("iphone", 100000, 5000)  # Productクラスのインスタンス化
    print(p1)
    print(p1.name)  # name
    print(p1.amount)  # 100000
    print(p1.discount)  # 95000

    p2 = Product("MacBookAir", 150000, 5000)
    print(p2.name)
    print(p2.amount)
    print(p2.discount)
