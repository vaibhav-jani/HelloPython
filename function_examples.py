def demonstrate_basic_functions():
    print("\n=== Basic Functions ===")

    # Simple function without parameters
    def greet():
        print("Hello, World!")

    # Function with parameters
    def greet_person(name):
        print(f"Hello, {name}!")

    # Function with return value
    def add(a, b):
        return a + b

    # Calling the functions
    greet()
    greet_person("Alice")
    result = add(5, 3)
    print(f"Sum: {result}")


def demonstrate_default_parameters():
    print("\n=== Default Parameters ===")

    def greet(name="World"):
        print(f"Hello, {name}!")

    # Using default parameter
    greet()

    # Overriding default parameter
    greet("Alice")

    # Multiple default parameters
    def create_user(name, age=18, city="Unknown"):
        print(f"User: {name}, Age: {age}, City: {city}")

    create_user("Bob")
    create_user("Charlie", 25)
    create_user("David", 30, "New York")


def demonstrate_keyword_arguments():
    print("\n=== Keyword Arguments ===")

    def create_profile(name, age, city):
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"City: {city}")

    # Using keyword arguments
    create_profile(name="Alice", age=25, city="New York")

    # Different order with keyword arguments
    create_profile(city="London", name="Bob", age=30)


def demonstrate_arbitrary_arguments():
    print("\n=== Arbitrary Arguments ===")

    # *args for arbitrary positional arguments
    def sum_all(*numbers):
        return sum(numbers)

    print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
    print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")

    # **kwargs for arbitrary keyword arguments
    def print_info(**info):
        for key, value in info.items():
            print(f"{key}: {value}")

    print("\nPrinting info:")
    print_info(name="Alice", age=25, city="New York")


def demonstrate_return_values():
    print("\n=== Return Values ===")

    # Single return value
    def square(n):
        return n * n

    # Multiple return values
    def get_coordinates():
        return 10, 20

    # Return None
    def greet(name):
        print(f"Hello, {name}")
        return None

    # Using the functions
    print(f"Square of 5: {square(5)}")
    x, y = get_coordinates()
    print(f"Coordinates: ({x}, {y})")
    result = greet("Alice")
    print(f"Greet function returns: {result}")


def demonstrate_lambda_functions():
    print("\n=== Lambda Functions and Function Composition ===")

    # Basic lambda functions
    def square(x): return x * x
    def add_one(x): return x + 1
    def double(x): return x * 2

    print("Basic lambda functions:")
    print(f"Square of 5: {square(5)}")
    print(f"Add one to 5: {add_one(5)}")
    print(f"Double 5: {double(5)}")

    # Function composition using lambda
    def compose(f, g): return lambda x: f(g(x))

    # Compose functions
    square_then_add_one = compose(add_one, square)
    add_one_then_square = compose(square, add_one)

    print("\nFunction composition:")
    print(f"Square then add one to 5: {square_then_add_one(5)}")
    print(f"Add one then square 5: {add_one_then_square(5)}")

    # Higher-order function with lambda
    def apply_operations(value, operations):
        result = value
        for op in operations:
            result = op(result)
        return result

    # List of lambda functions
    operations = [
        lambda x: x * 2,    # double
        lambda x: x + 1,    # add one
        lambda x: x * x     # square
    ]

    print("\nHigher-order function:")
    print(f"Apply operations to 5: {apply_operations(5, operations)}")

    # Lambda with filter and map
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Filter even numbers and square them
    even_squares = list(
        map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers)))
    print(f"\nEven numbers squared: {even_squares}")

    # Lambda with reduce
    from functools import reduce
    product = reduce(lambda x, y: x * y, numbers)
    print(f"Product of all numbers: {product}")

    # Lambda with sorted
    students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78}
    ]

    sorted_by_score = sorted(students, key=lambda x: x["score"], reverse=True)
    print("\nStudents sorted by score:")
    for student in sorted_by_score:
        print(f"{student['name']}: {student['score']}")


def demonstrate_recursive_functions():
    print("\n=== Recursive Functions ===")

    # Factorial using recursion
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

    print(f"Factorial of 5: {factorial(5)}")

    # Fibonacci sequence using recursion
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    print("First 5 Fibonacci numbers:")
    for i in range(5):
        print(f"fibonacci({i}) = {fibonacci(i)}")


def demonstrate_function_annotations():
    print("\n=== Function Annotations ===")

    def greet(name: str) -> str:
        return f"Hello, {name}!"

    def add(a: int, b: int) -> int:
        return a + b

    # Using the annotated functions
    result = greet("Alice")
    print(f"Greeting: {result}")
    print(f"Type of result: {type(result)}")

    sum_result = add(5, 3)
    print(f"Sum: {sum_result}")
    print(f"Type of sum: {type(sum_result)}")


def main():
    print("Python Functions Examples")
    print("=" * 30)

    demonstrate_basic_functions()
    demonstrate_default_parameters()
    demonstrate_keyword_arguments()
    demonstrate_arbitrary_arguments()
    demonstrate_return_values()
    demonstrate_lambda_functions()
    demonstrate_recursive_functions()
    demonstrate_function_annotations()


if __name__ == "__main__":
    main()
