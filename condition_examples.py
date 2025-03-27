def demonstrate_basic_if_else():
    print("\n=== Basic If-Else ===")
    age = 18

    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")


def demonstrate_elif():
    print("\n=== If-Elif-Else ===")
    score = 85

    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")


def demonstrate_nested_conditions():
    print("\n=== Nested Conditions ===")
    age = 25
    has_license = True

    if age >= 18:
        if has_license:
            print("You can drive")
        else:
            print("You need to get a license first")
    else:
        print("You are too young to drive")


def demonstrate_logical_operators_in_conditions():
    print("\n=== Logical Operators in Conditions ===")
    age = 25
    income = 50000
    has_job = True

    # Using and
    if age >= 18 and income >= 30000:
        print("You meet the basic requirements")

    # Using or
    if has_job or income >= 50000:
        print("You have sufficient financial means")

    # Using not
    if not has_job:
        print("You need to find a job")

    # Complex conditions
    if (age >= 18 and income >= 30000) or (has_job and income >= 25000):
        print("You qualify for the program")


def demonstrate_conditional_expressions():
    print("\n=== Conditional Expressions (Ternary Operator) ===")
    age = 20
    score = 85

    # Basic ternary
    status = "adult" if age >= 18 else "minor"
    print(f"Status: {status}")

    # Nested ternary
    grade = "A" if score >= 90 else "B" if score >= 80 else "C"
    print(f"Grade: {grade}")


def demonstrate_isinstance_conditions():
    print("\n=== Type Checking Conditions ===")
    value = 42

    if isinstance(value, int):
        print("Value is an integer")
    elif isinstance(value, float):
        print("Value is a float")
    elif isinstance(value, str):
        print("Value is a string")
    else:
        print("Value is of another type")


def demonstrate_in_conditions():
    print("\n=== Membership Conditions ===")
    fruits = ["apple", "banana", "cherry"]
    fruit = "apple"

    if fruit in fruits:
        print(f"{fruit} is in the list")
    else:
        print(f"{fruit} is not in the list")

    # Using not in
    if "orange" not in fruits:
        print("Orange is not in the list")


def demonstrate_comparison_chaining():
    print("\n=== Comparison Chaining ===")
    age = 25

    # Multiple comparisons
    if 18 <= age <= 30:
        print("Age is between 18 and 30")

    # Using any()
    numbers = [1, 2, 3, 4, 5]
    if any(num > 3 for num in numbers):
        print("There are numbers greater than 3")

    # Using all()
    if all(num > 0 for num in numbers):
        print("All numbers are positive")


def main():
    print("Python Conditions Examples")
    print("=" * 30)

    demonstrate_basic_if_else()
    demonstrate_elif()
    demonstrate_nested_conditions()
    demonstrate_logical_operators_in_conditions()
    demonstrate_conditional_expressions()
    demonstrate_isinstance_conditions()
    demonstrate_in_conditions()
    demonstrate_comparison_chaining()


if __name__ == "__main__":
    main()
