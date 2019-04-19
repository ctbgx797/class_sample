class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def info_csv(self):
        return f"{self.full_name()},{self.age}"

    # 自分の考え
    def display_profile(self):
        return f"Name:{self.full_name()} Age:{self.age}"

    def display_profile_2(self):
        print(f"Name:{self.full_name()} Age:{self.age}")


if __name__ == "__main__":
    # "Tom Ford"
    tom = Customer("Tom", "Ford", 57)
    print(tom.full_name())
    print(tom.display_profile())  # 自分の考え # "Name: Tom Ford, Age: 57"
    tom.display_profile_2()
    # print(tom.first_name + tom.family_name)

    # "Ken Yokoyama"
    ken = Customer("Ken", "Yokoyama", 49)
    print(ken.full_name())
    print(ken.display_profile())
    ken.display_profile_2()
    # print(ken.first_name + ken.family_name)
