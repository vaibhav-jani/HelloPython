def demonstrate_classes_and_objects():
    print("\n=== Classes and Objects ===")

    class Dog:
        # Class variable (shared by all instances)
        species = "Canis familiaris"

        # Constructor (__init__)
        def __init__(self, name, age):
            # Instance variables (unique to each instance)
            self.name = name
            self.age = age

        # Instance method
        def bark(self):
            return f"{self.name} says Woof!"

        # Instance method with self
        def get_info(self):
            return f"{self.name} is {self.age} years old"

    # Creating objects
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Max", 5)

    print(f"Dog 1: {dog1.get_info()}")
    print(f"Dog 2: {dog2.get_info()}")
    print(f"Species: {Dog.species}")


def demonstrate_encapsulation():
    print("\n=== Encapsulation ===")

    class BankAccount:
        def __init__(self, account_number, balance):
            # Private attributes (using name mangling)
            self.__account_number = account_number
            self.__balance = balance

        # Public method to access private attribute
        def get_balance(self):
            return self.__balance

        # Public method to modify private attribute
        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount
                return True
            return False

    # Creating and using encapsulated object
    account = BankAccount("12345", 1000)
    print(f"Initial balance: {account.get_balance()}")
    account.deposit(500)
    print(f"After deposit: {account.get_balance()}")


def demonstrate_inheritance():
    print("\n=== Inheritance ===")

    # Base class
    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            return "Some sound"

    # Derived class
    class Cat(Animal):
        def speak(self):
            return f"{self.name} says Meow!"

    # Another derived class
    class Dog(Animal):
        def speak(self):
            return f"{self.name} says Woof!"

    # Using inherited classes
    cat = Cat("Whiskers")
    dog = Dog("Buddy")

    print(f"Cat: {cat.speak()}")
    print(f"Dog: {dog.speak()}")


def demonstrate_multiple_inheritance():
    print("\n=== Multiple Inheritance ===")

    class Flyable:
        def fly(self):
            return "Flying high!"

    class Swimmable:
        def swim(self):
            return "Swimming in water!"

    class Duck(Flyable, Swimmable):
        def __init__(self, name):
            self.name = name

        def quack(self):
            return f"{self.name} says Quack!"

    # Using multiple inheritance
    duck = Duck("Donald")
    print(f"Duck: {duck.quack()}")
    print(f"Can fly: {duck.fly()}")
    print(f"Can swim: {duck.swim()}")


def demonstrate_polymorphism():
    print("\n=== Polymorphism ===")

    class Shape:
        def area(self):
            pass

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius ** 2

    # Using polymorphism
    shapes = [Rectangle(5, 3), Circle(2)]
    for shape in shapes:
        print(f"Area: {shape.area()}")


def demonstrate_class_methods():
    print("\n=== Class Methods ===")

    class Student:
        # Class variable
        total_students = 0

        def __init__(self, name, grade):
            self.name = name
            self.grade = grade
            Student.total_students += 1

        # Instance method
        def get_info(self):
            return f"{self.name} is in grade {self.grade}"

        # Class method
        @classmethod
        def get_total_students(cls):
            return cls.total_students

        # Static method
        @staticmethod
        def is_passing_grade(grade):
            return grade >= 60

    # Using class methods
    student1 = Student("Alice", 85)
    student2 = Student("Bob", 75)

    print(f"Total students: {Student.get_total_students()}")
    print(f"Is 85 a passing grade? {Student.is_passing_grade(85)}")


def demonstrate_properties():
    print("\n=== Properties ===")

    class Temperature:
        def __init__(self):
            self._celsius = 0

        @property
        def celsius(self):
            return self._celsius

        @celsius.setter
        def celsius(self, value):
            if value < -273.15:  # Absolute zero
                raise ValueError("Temperature below absolute zero")
            self._celsius = value

        @property
        def fahrenheit(self):
            return (self._celsius * 9/5) + 32

    # Using properties
    temp = Temperature()
    temp.celsius = 25
    print(f"Celsius: {temp.celsius}")
    print(f"Fahrenheit: {temp.fahrenheit}")


def demonstrate_abstract_classes():
    print("\n=== Abstract Classes ===")

    from abc import ABC, abstractmethod

    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

        @abstractmethod
        def perimeter(self):
            pass

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

    # Using abstract class
    rectangle = Rectangle(5, 3)
    print(f"Area: {rectangle.area()}")
    print(f"Perimeter: {rectangle.perimeter()}")


def main():
    print("Python Object-Oriented Programming Examples")
    print("=" * 30)

    demonstrate_classes_and_objects()
    demonstrate_encapsulation()
    demonstrate_inheritance()
    demonstrate_multiple_inheritance()
    demonstrate_polymorphism()
    demonstrate_class_methods()
    demonstrate_properties()
    demonstrate_abstract_classes()


if __name__ == "__main__":
    main()
