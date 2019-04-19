class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def info_csv(self):
        return f"{self.full_name()},{self.age}"

    def display_profile(self):
        return f"Name:{self.full_name()} Age:{self.age}"


if __name__ == "__main__":
    # "Tom Ford"
    tom = Customer("Tom", "Ford", 57)
    print(tom.full_name())
    print(tom.display_profile())  # "Name: Tom Ford, Age: 57"
    # print(tom.first_name + tom.family_name)

    ken = Customer("Ken", "Yokoyama", 49)
    print(ken.full_name())
    print(ken.display_profile())
    # print(ken.first_name + ken.family_name)
