class User:
    def __init__(self, name, age, country, hobby, blood_type):
        # インスタンス変数
        self.name = name
        self.age = age
        self.country = country
        self.hobby = hobby
        self.blood_type = blood_type

    def display_profile(self):
        # display_profile は Userクラスの インスタンスメソッド
        print(f"名前:{self.name} 国籍:{self.country} 年齢:{self.age}歳 血液型:{self.blood_type}")

    def hobbys(self):
        # hobbys は Userクラスの インスタンスメソッド
        print(f"趣味は{self.hobby}です｡")

    def change_nationality(self, country_name):
        self.country = country_name


if __name__ == "__main__":
    bob = User("Bob", 15, "USA", "ゲーム", "O型")  # Userクラスをインスタンス化
    bob.display_profile()
    bob.change_nationality("China")
    bob.display_profile()
    bob.hobbys()

    tom = User("Tom", 57, "USA", "Netflixで映画鑑賞", "B型")
    tom.display_profile()
    tom.change_nationality("Spain")
    tom.display_profile()
    tom.hobbys()

    ken = User("Ken", 49, "JPN", "プログラミング", "AB型")
    ken.display_profile()
    ken.change_nationality("Itary")
    ken.display_profile()
    ken.hobbys()
