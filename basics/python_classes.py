class Dog:

    dog_sound = "woof"

    def __init__(self, name="Azor"):
        self.name = name

    def make_a_sound(self):
        print(self.dog_sound)

    def call_by_name(self):
        print(self.name)

    def calculate_food(self, mass):
        return mass / 80


my_dog = Dog(name="Pies")
my_dog.make_a_sound()
my_dog.call_by_name()
food_needed = my_dog.calculate_food(40)
print(food_needed)
