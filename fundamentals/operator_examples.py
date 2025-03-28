def demonstrate_arithmetic_operators():
    print("\n=== Arithmetic Operators ===")
    a, b = 10, 3

    print(f"a = {a}, b = {b}")
    print(f"Addition (+): {a} + {b} = {a + b}")
    print(f"Subtraction (-): {a} - {b} = {a - b}")
    print(f"Multiplication (*): {a} * {b} = {a * b}")
    print(f"Division (/): {a} / {b} = {a / b}")
    print(f"Floor Division (//): {a} // {b} = {a // b}")
    print(f"Modulus (%): {a} % {b} = {a % b}")
    print(f"Exponentiation (**): {a} ** {b} = {a ** b}")
    print(f"Unary minus (-): -{a} = {-a}")
    print(f"Unary plus (+): +{a} = {+a}")


def demonstrate_comparison_operators():
    print("\n=== Comparison Operators ===")
    a, b = 5, 10

    print(f"a = {a}, b = {b}")
    print(f"Equal (==): {a} == {b} is {a == b}")
    print(f"Not Equal (!=): {a} != {b} is {a != b}")
    print(f"Greater Than (>): {a} > {b} is {a > b}")
    print(f"Less Than (<): {a} < {b} is {a < b}")
    print(f"Greater Than or Equal (>=): {a} >= {b} is {a >= b}")
    print(f"Less Than or Equal (<=): {a} <= {b} is {a <= b}")


def demonstrate_logical_operators():
    print("\n=== Logical Operators ===")
    x, y, z = True, False, True

    print(f"x = {x}, y = {y}, z = {z}")
    print(f"AND (and): x and y = {x and y}")
    print(f"OR (or): x or y = {x or y}")
    print(f"NOT (not): not x = {not x}")
    print(f"Complex logical: (x and y) or (not z) = {(x and y) or (not z)}")


def demonstrate_assignment_operators():
    print("\n=== Assignment Operators ===")
    x = 10
    print(f"Initial x = {x}")

    x += 5  # x = x + 5
    print(f"After += 5: x = {x}")

    x -= 3  # x = x - 3
    print(f"After -= 3: x = {x}")

    x *= 2  # x = x * 2
    print(f"After *= 2: x = {x}")

    x /= 4  # x = x / 4
    print(f"After /= 4: x = {x}")

    x //= 2  # x = x // 2
    print(f"After //= 2: x = {x}")

    x %= 3  # x = x % 3
    print(f"After %= 3: x = {x}")

    x **= 2  # x = x ** 2
    print(f"After **= 2: x = {x}")


def demonstrate_bitwise_operators():
    print("\n=== Bitwise Operators ===")
    a, b = 60, 13  # 60 = 0011 1100, 13 = 0000 1101

    print(f"a = {a} (binary: {bin(a)})")
    print(f"b = {b} (binary: {bin(b)})")
    print(f"AND (&): {a} & {b} = {a & b} (binary: {bin(a & b)})")
    print(f"OR (|): {a} | {b} = {a | b} (binary: {bin(a | b)})")
    print(f"XOR (^): {a} ^ {b} = {a ^ b} (binary: {bin(a ^ b)})")
    print(f"NOT (~): ~{a} = {~a} (binary: {bin(~a)})")
    print(f"Left Shift (<<): {a} << 2 = {a << 2} (binary: {bin(a << 2)})")
    print(f"Right Shift (>>): {a} >> 2 = {a >> 2} (binary: {bin(a >> 2)})")


def demonstrate_identity_operators():
    print("\n=== Identity Operators ===")
    x = [1, 2, 3]
    y = [1, 2, 3]
    z = x

    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = {z}")
    print(f"x is y: {x is y}")  # False because they are different objects
    print(f"x is z: {x is z}")  # True because z references the same object
    # True because they are different objects
    print(f"x is not y: {x is not y}")


def demonstrate_membership_operators():
    print("\n=== Membership Operators ===")
    fruits = ["apple", "banana", "cherry"]
    print(f"fruits = {fruits}")

    print(f"'apple' in fruits: {'apple' in fruits}")
    print(f"'orange' in fruits: {'orange' in fruits}")
    print(f"'apple' not in fruits: {'apple' not in fruits}")
    print(f"'orange' not in fruits: {'orange' not in fruits}")


def main():
    print("Python Operators Examples")
    print("=" * 30)

    demonstrate_arithmetic_operators()
    demonstrate_comparison_operators()
    demonstrate_logical_operators()
    demonstrate_assignment_operators()
    demonstrate_bitwise_operators()
    demonstrate_identity_operators()
    demonstrate_membership_operators()


if __name__ == "__main__":
    main()
