"""
演習: 下記のコードが正しく動作するような Counterクラスを実装せよ
"""


class Counter:
    def __init__(self, value):
        self.value = value

    def increase(self):
        self.value += 1

    def increase3(self):
        self.value += 3


if __name__ == "__main__":
    counter_1 = Counter(0)
    print(counter_1.value)  # 0 が出力される

    counter_1.increase()
    print(counter_1.value)  # 1 が出力される <--- 1だけ増えてる

    counter_1.increase()
    print(counter_1.value)  # 2 が出力される <--- さらに1だけ増えている

    counter_2 = Counter(15)
    print(counter_2.value)

    counter_2.increase3()
    print(counter_2.value)  # 3ずつ増える

    counter_2.increase3()
    print(counter_2.value)  # さらに3増える
