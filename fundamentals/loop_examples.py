def demonstrate_for_loops():
    print("\n=== For Loops ===")

    # Basic for loop with list
    fruits = ["apple", "banana", "cherry"]
    print("Iterating through a list:")
    for fruit in fruits:
        print(fruit)

    # For loop with range
    print("\nUsing range():")
    for i in range(5):  # 0 to 4
        print(f"Count: {i}")

    # For loop with start, stop, and step
    print("\nUsing range with start, stop, and step:")
    for i in range(2, 10, 2):  # Start at 2, stop at 9, step by 2
        print(f"Count: {i}")

    # For loop with enumerate
    print("\nUsing enumerate():")
    for index, fruit in enumerate(fruits):
        print(f"Index {index}: {fruit}")


def demonstrate_while_loops():
    print("\n=== While Loops ===")

    # Basic while loop
    count = 0
    print("Counting up to 5:")
    while count < 5:
        print(f"Count: {count}")
        count += 1

    # While loop with break
    print("\nWhile loop with break:")
    count = 0
    while True:
        if count >= 3:
            break
        print(f"Count: {count}")
        count += 1

    # While loop with continue
    print("\nWhile loop with continue:")
    count = 0
    while count < 5:
        count += 1
        if count == 3:
            continue
        print(f"Count: {count}")


def demonstrate_nested_loops():
    print("\n=== Nested Loops ===")

    # Nested for loops
    print("Multiplication table:")
    for i in range(1, 3):
        for j in range(1, 3):
            print(f"{i} x {j} = {i * j}")

    # Nested while loops
    print("\nNested while loops:")
    i = 0
    while i < 2:
        j = 0
        while j < 2:
            print(f"i={i}, j={j}")
            j += 1
        i += 1


def demonstrate_loop_control():
    print("\n=== Loop Control Statements ===")

    # Break statement
    print("Using break:")
    for i in range(5):
        if i == 3:
            break
        print(f"Count: {i}")

    # Continue statement
    print("\nUsing continue:")
    for i in range(5):
        if i == 2:
            continue
        print(f"Count: {i}")

    # Else clause in loops
    print("\nUsing else clause:")
    for i in range(3):
        print(f"Count: {i}")
    else:
        print("Loop completed successfully")


def demonstrate_list_comprehension():
    print("\n=== List Comprehension ===")

    # Basic list comprehension
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print(f"Original numbers: {numbers}")
    print(f"Squares: {squares}")

    # List comprehension with condition
    even_squares = [x**2 for x in numbers if x % 2 == 0]
    print(f"Even squares: {even_squares}")

    # Nested list comprehension
    matrix = [[1, 2], [3, 4]]
    flattened = [item for row in matrix for item in row]
    print(f"Matrix: {matrix}")
    print(f"Flattened: {flattened}")


def demonstrate_loop_with_zip():
    print("\n=== Loops with zip() ===")

    # Basic zip
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    print("Iterating through multiple lists:")
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old")

    # zip with enumerate
    print("\nUsing zip with enumerate:")
    for i, (name, age) in enumerate(zip(names, ages)):
        print(f"{i+1}. {name} is {age} years old")


def demonstrate_loop_with_dict():
    print("\n=== Loops with Dictionaries ===")

    person = {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }

    # Iterating through keys
    print("Keys:")
    for key in person:
        print(key)

    # Iterating through values
    print("\nValues:")
    for value in person.values():
        print(value)

    # Iterating through items
    print("\nItems:")
    for key, value in person.items():
        print(f"{key}: {value}")


def main():
    print("Python Loops Examples")
    print("=" * 30)

    demonstrate_for_loops()
    demonstrate_while_loops()
    demonstrate_nested_loops()
    demonstrate_loop_control()
    demonstrate_list_comprehension()
    demonstrate_loop_with_zip()
    demonstrate_loop_with_dict()


if __name__ == "__main__":
    main()
