def demonstrate_none_basics():
    print("\n=== None Basics ===")

    # None is a singleton object
    x = None
    y = None
    print(f"x is None: {x is None}")
    print(f"x == y: {x == y}")
    print(f"x is y: {x is y}")  # True because None is a singleton

    # Type of None
    print(f"Type of None: {type(None)}")

    # None in boolean context
    print(f"bool(None): {bool(None)}")
    print(f"not None: {not None}")


def demonstrate_none_in_functions():
    print("\n=== None in Functions ===")

    # Function that returns None implicitly
    def greet(name):
        print(f"Hello, {name}")
        # No return statement means None is returned

    # Function that returns None explicitly
    def greet_explicit(name):
        print(f"Hello, {name}")
        return None

    # Function that might return None
    def find_user(user_id):
        users = {1: "Alice", 2: "Bob"}
        return users.get(user_id)  # Returns None if key doesn't exist

    # Using the functions
    result1 = greet("Alice")
    print(f"greet() returns: {result1}")

    result2 = greet_explicit("Bob")
    print(f"greet_explicit() returns: {result2}")

    user = find_user(1)
    print(f"find_user(1) returns: {user}")
    user = find_user(3)
    print(f"find_user(3) returns: {user}")


def demonstrate_none_comparison():
    print("\n=== None Comparison ===")

    # Correct way to compare with None
    x = None
    print(f"x is None: {x is None}")  # Correct
    print(f"x == None: {x == None}")  # Less preferred

    # Common mistake
    y = []
    print(f"\ny = []")
    print(f"y is None: {y is None}")  # False
    print(f"y == None: {y == None}")  # False

    # None in conditional statements
    def process_data(data):
        if data is None:
            print("No data provided")
        else:
            print(f"Processing data: {data}")

    process_data(None)
    process_data("Some data")


def demonstrate_none_in_data_structures():
    print("\n=== None in Data Structures ===")

    # None in lists
    numbers = [1, None, 3, None, 5]
    print(f"List with None: {numbers}")
    print(f"Count of None: {numbers.count(None)}")

    # None in dictionaries
    user = {
        "name": "Alice",
        "age": None,
        "email": None
    }
    print(f"\nDictionary with None: {user}")

    # Filtering None values
    filtered_numbers = [x for x in numbers if x is not None]
    print(f"Filtered numbers: {filtered_numbers}")

    # Using None as dictionary value
    cache = {}

    def get_data(key):
        if key in cache:
            return cache[key]
        return None

    # Setting and checking None values
    cache["user1"] = None
    print(f"\nCache: {cache}")
    print(f"get_data('user1'): {get_data('user1')}")
    print(f"get_data('user2'): {get_data('user2')}")


def demonstrate_none_in_oop():
    print("\n=== None in Object-Oriented Programming ===")

    class User:
        def __init__(self, name, age=None, email=None):
            self.name = name
            self.age = age
            self.email = email

        def get_info(self):
            info = f"Name: {self.name}"
            if self.age is not None:
                info += f", Age: {self.age}"
            if self.email is not None:
                info += f", Email: {self.email}"
            return info

    # Creating users with and without optional attributes
    user1 = User("Alice", 25, "alice@example.com")
    user2 = User("Bob")  # age and email are None

    print(f"User 1: {user1.get_info()}")
    print(f"User 2: {user2.get_info()}")


def demonstrate_none_in_error_handling():
    print("\n=== None in Error Handling ===")

    def safe_divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return None
        except TypeError:
            return None

    # Testing safe division
    print(f"safe_divide(10, 2): {safe_divide(10, 2)}")
    print(f"safe_divide(10, 0): {safe_divide(10, 0)}")
    print(f"safe_divide(10, 'a'): {safe_divide(10, 'a')}")

    # Using None to indicate failure
    def find_user_by_id(user_id):
        users = {1: "Alice", 2: "Bob"}
        try:
            return users[user_id]
        except KeyError:
            return None

    user = find_user_by_id(1)
    if user is not None:
        print(f"Found user: {user}")
    else:
        print("User not found")


def main():
    print("Python None Examples")
    print("=" * 30)

    demonstrate_none_basics()
    demonstrate_none_in_functions()
    demonstrate_none_comparison()
    demonstrate_none_in_data_structures()
    demonstrate_none_in_oop()
    demonstrate_none_in_error_handling()


if __name__ == "__main__":
    main()
