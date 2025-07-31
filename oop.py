# Assignment 1: Design Your Own Class - Superhero Example with Inheritance

class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def show_identity(self):
        print(f"Hero: {self.name}, Power: {self.power}, Protects: {self.city}")

    def fight(self):
        print(f"{self.name} uses {self.power} to fight evil!")

# Inheritance layer with encapsulation example
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flying_speed):
        super().__init__(name, power, city)
        self.__flying_speed = flying_speed  # private attribute

    def fly(self):
        print(f"{self.name} is flying at {self.__flying_speed} km/h!")

    def get_flying_speed(self):
        return self.__flying_speed

    def set_flying_speed(self, speed):
        if speed > 0:
            self.__flying_speed = speed
        else:
            print("Flying speed must be positive.")

# Activity 2: Polymorphism Challenge

class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing ⛵")

def demonstrate_movement(vehicle):
    vehicle.move()

# Testing our classes
if __name__ == "__main__":
    # Assignment 1 test
    hero = Superhero("MightyMan", "Super Strength", "Metro City")
    hero.show_identity()
    hero.fight()

    flyer = FlyingSuperhero("SkyQueen", "Laser Eyes", "Cloud City", 900)
    flyer.show_identity()
    flyer.fight()
    flyer.fly()
    print(f"Flying speed is {flyer.get_flying_speed()} km/h.")
    flyer.set_flying_speed(950)
    flyer.fly()

    print("\nPolymorphism Challenge:")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        demonstrate_movement(v)