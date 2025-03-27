from typing import TypeVar, Generic, List, Dict, Optional, Union, Any
from dataclasses import dataclass


def demonstrate_basic_type_hints():
    print("\n=== Basic Type Hints ===")

    # Basic type hints
    def greet(name: str) -> str:
        return f"Hello, {name}"

    def add(a: int, b: int) -> int:
        return a + b

    def process_data(data: Union[str, int]) -> str:
        return str(data)

    # Using the functions
    print(f"Greeting: {greet('Alice')}")
    print(f"Sum: {add(5, 3)}")

    # Using process_data with different types
    print("\nUsing process_data with different types:")
    print(f"With integer: {process_data(42)}")
    print(f"With string: {process_data('Hello World')}")
    print(f"With string number: {process_data('123')}")
    print(f"With empty string: {process_data('')}")


def demonstrate_generic_classes():
    print("\n=== Generic Classes ===")

    # Define a type variable
    T = TypeVar('T')

    # Generic class
    class Box(Generic[T]):
        def __init__(self, value: T):
            self.value = value

        def get_value(self) -> T:
            return self.value

        def set_value(self, value: T) -> None:
            self.value = value

    # Using generic class with different types
    int_box = Box[int](42)
    str_box = Box[str]("Hello")

    print(f"Integer box value: {int_box.get_value()}")
    print(f"String box value: {str_box.get_value()}")


def demonstrate_generic_functions():
    print("\n=== Generic Functions ===")

    # Define type variables
    T = TypeVar('T')
    U = TypeVar('U')

    # Generic function with single type variable
    def first_element(items: List[T]) -> Optional[T]:
        return items[0] if items else None

    # Generic function with multiple type variables
    def create_pair(first: T, second: U) -> tuple[T, U]:
        return (first, second)

    # Using generic functions
    numbers = [1, 2, 3, 4, 5]
    names = ["Alice", "Bob", "Charlie"]

    print(f"First number: {first_element(numbers)}")
    print(f"First name: {first_element(names)}")
    print(f"Pair: {create_pair(42, 'Hello')}")


def demonstrate_generic_collections():
    print("\n=== Generic Collections ===")

    # Generic list
    def process_numbers(numbers: List[int]) -> List[int]:
        return [x * 2 for x in numbers]

    # Generic dictionary
    def create_user_map(users: List[str]) -> Dict[str, int]:
        return {name: len(name) for name in users}

    # Using generic collections
    numbers = [1, 2, 3, 4, 5]
    users = ["Alice", "Bob", "Charlie"]

    print(f"Doubled numbers: {process_numbers(numbers)}")
    print(f"User map: {create_user_map(users)}")


def demonstrate_optional_types():
    print("\n=== Optional Types ===")

    @dataclass
    class User:
        name: str
        age: Optional[int] = None
        email: Optional[str] = None

    def get_user_info(user: User) -> str:
        info = f"Name: {user.name}"
        if user.age is not None:
            info += f", Age: {user.age}"
        if user.email is not None:
            info += f", Email: {user.email}"
        return info

    # Using optional types
    user1 = User("Alice", 25, "alice@example.com")
    user2 = User("Bob")  # age and email are None

    print(f"User 1: {get_user_info(user1)}")
    print(f"User 2: {get_user_info(user2)}")


def demonstrate_union_types():
    print("\n=== Union Types ===")

    def process_value(value: Union[int, str, float]) -> str:
        if isinstance(value, int):
            return f"Integer: {value}"
        elif isinstance(value, str):
            return f"String: {value}"
        else:
            return f"Float: {value}"

    # Using union types
    print(f"Process integer: {process_value(42)}")
    print(f"Process string: {process_value('Hello')}")
    print(f"Process float: {process_value(3.14)}")


def demonstrate_any_type():
    print("\n=== Any Type ===")

    def process_any(value: Any) -> str:
        if isinstance(value, (int, float)):
            return f"Number: {value}"
        elif isinstance(value, str):
            return f"String: {value}"
        elif isinstance(value, list):
            return f"List: {value}"
        else:
            return f"Other type: {type(value)}"

    # Using Any type
    print(f"Process number: {process_any(42)}")
    print(f"Process string: {process_any('Hello')}")
    print(f"Process list: {process_any([1, 2, 3])}")
    print(f"Process dict: {process_any({'key': 'value'})}")


def main():
    print("Python Generics and Type Hints Examples")
    print("=" * 30)

    demonstrate_basic_type_hints()
    demonstrate_generic_classes()
    demonstrate_generic_functions()
    demonstrate_generic_collections()
    demonstrate_optional_types()
    demonstrate_union_types()
    demonstrate_any_type()


if __name__ == "__main__":
    main()
