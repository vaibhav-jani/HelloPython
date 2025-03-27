def demonstrate_primary_data_structures():
    print("\n=== Primary Data Structures ===")

    # Numbers (int, float)
    integer = 42
    float_num = 3.14
    complex_num = 3 + 4j
    print(f"Integer: {integer}, Type: {type(integer)}")
    print(f"Float: {float_num}, Type: {type(float_num)}")
    print(f"Complex: {complex_num}, Type: {type(complex_num)}")

    # Strings
    string1 = "Hello, World!"
    string2 = 'Single quotes'
    string3 = """Multi-line
    string"""
    print(f"\nString1: {string1}, Type: {type(string1)}")
    print(f"String2: {string2}, Type: {type(string2)}")
    print(f"String3: {string3}, Type: {type(string3)}")

    # Boolean
    true_value = True
    false_value = False
    print(f"\nTrue: {true_value}, Type: {type(true_value)}")
    print(f"False: {false_value}, Type: {type(false_value)}")


def demonstrate_sequence_data_structures():
    print("\n=== Sequence Data Structures ===")

    # Lists (mutable)
    numbers = [1, 2, 3, 4, 5]
    mixed_list = [1, "hello", 3.14, True]
    print(f"List: {numbers}, Type: {type(numbers)}")
    print(f"Mixed list: {mixed_list}, Type: {type(mixed_list)}")

    # List operations
    numbers.append(6)
    numbers.insert(0, 0)
    numbers.remove(3)
    print(f"Modified list: {numbers}")

    # Tuples (immutable)
    coordinates = (10, 20)
    single_item = (42,)  # Note the comma
    print(f"\nTuple: {coordinates}, Type: {type(coordinates)}")
    print(f"Single item tuple: {single_item}, Type: {type(single_item)}")

    # Range
    range_obj = range(5)
    print(f"\nRange: {list(range_obj)}, Type: {type(range_obj)}")


def demonstrate_mapping_data_structures():
    print("\n=== Mapping Data Structures ===")

    # Dictionaries (key-value pairs)
    person = {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }
    print(f"Dictionary: {person}, Type: {type(person)}")

    # Dictionary operations
    person["email"] = "alice@example.com"
    print(f"Added email: {person}")

    # Dictionary methods
    print(f"Keys: {list(person.keys())}")
    print(f"Values: {list(person.values())}")
    print(f"Items: {list(person.items())}")


def demonstrate_set_data_structures():
    print("\n=== Set Data Structures ===")

    # Sets (unique, unordered)
    numbers = {1, 2, 3, 3, 4, 4, 5}  # Duplicates are removed
    print(f"Set: {numbers}, Type: {type(numbers)}")

    # Set operations
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    print(f"\nSet1: {set1}")
    print(f"Set2: {set2}")
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference: {set1 - set2}")
    print(f"Symmetric difference: {set1 ^ set2}")


def demonstrate_complex_data_structures():
    print("\n=== Complex Data Structures ===")

    # Nested lists (2D list)
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"2D Matrix: {matrix}")
    print(f"Access element [1][2]: {matrix[1][2]}")

    # List of dictionaries
    students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78}
    ]
    print(f"\nList of dictionaries: {students}")

    # Dictionary with lists
    classroom = {
        "teacher": "Mr. Smith",
        "students": ["Alice", "Bob", "Charlie"],
        "grades": [85, 92, 78]
    }
    print(f"\nDictionary with lists: {classroom}")


def demonstrate_data_structure_methods():
    print("\n=== Common Data Structure Methods ===")

    # List methods
    numbers = [1, 2, 3, 4, 5]
    print(f"Original list: {numbers}")
    numbers.append(6)
    print(f"After append: {numbers}")
    numbers.extend([7, 8])
    print(f"After extend: {numbers}")
    numbers.pop()
    print(f"After pop: {numbers}")
    numbers.reverse()
    print(f"After reverse: {numbers}")

    # String methods
    text = "Hello, World!"
    print(f"\nOriginal string: {text}")
    print(f"Upper: {text.upper()}")
    print(f"Lower: {text.lower()}")
    print(f"Split: {text.split(',')}")
    print(f"Replace: {text.replace('World', 'Python')}")


def demonstrate_data_structure_comprehensions():
    print("\n=== Data Structure Comprehensions ===")

    # List comprehension
    squares = [x**2 for x in range(5)]
    print(f"List comprehension (squares): {squares}")

    # Dictionary comprehension
    square_dict = {x: x**2 for x in range(5)}
    print(f"Dictionary comprehension: {square_dict}")

    # Set comprehension
    even_squares = {x**2 for x in range(10) if x % 2 == 0}
    print(f"Set comprehension: {even_squares}")


def main():
    print("Python Data Structures Examples")
    print("=" * 30)

    demonstrate_primary_data_structures()
    demonstrate_sequence_data_structures()
    demonstrate_mapping_data_structures()
    demonstrate_set_data_structures()
    demonstrate_complex_data_structures()
    demonstrate_data_structure_methods()
    demonstrate_data_structure_comprehensions()


if __name__ == "__main__":
    main()
