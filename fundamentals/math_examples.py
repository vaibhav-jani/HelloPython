import math
import random
from decimal import Decimal


def demonstrate_basic_math():
    print("\n=== Basic Math Operations ===")
    a, b = 10, 3

    print(f"a = {a}, b = {b}")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Floor Division: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}")
    print(f"Absolute Value: |{a}| = {abs(a)}")


def demonstrate_math_module():
    print("\n=== Math Module Functions ===")
    x = 3.14
    y = 2

    print(f"x = {x}, y = {y}")
    print(f"Square Root: √{y} = {math.sqrt(y)}")
    print(f"Power: {x} ^ {y} = {math.pow(x, y)}")
    print(f"Ceiling: ⌈{x}⌉ = {math.ceil(x)}")
    print(f"Floor: ⌊{x}⌋ = {math.floor(x)}")
    print(f"Round: {x} = {round(x)}")
    print(f"Pi: π = {math.pi}")
    print(f"E: e = {math.e}")
    print(f"Logarithm (base e): ln({x}) = {math.log(x)}")
    print(f"Logarithm (base 10): log₁₀({x}) = {math.log10(x)}")
    print(f"Sine: sin({x}) = {math.sin(x)}")
    print(f"Cosine: cos({x}) = {math.cos(x)}")
    print(f"Tangent: tan({x}) = {math.tan(x)}")


def demonstrate_random_functions():
    print("\n=== Random Functions ===")

    print("Random float between 0 and 1:", random.random())
    print("Random integer between 1 and 10:", random.randint(1, 10))
    print("Random float between 1 and 10:", random.uniform(1, 10))

    # Random choice from a sequence
    fruits = ["apple", "banana", "cherry", "date"]
    print("Random fruit:", random.choice(fruits))

    # Random sample from a sequence
    print("Random sample of 2 fruits:", random.sample(fruits, 2))

    # Shuffle a sequence
    random.shuffle(fruits)
    print("Shuffled fruits:", fruits)


def demonstrate_decimal_operations():
    print("\n=== Decimal Operations ===")

    # Using Decimal for precise decimal arithmetic
    d1 = Decimal('0.1')
    d2 = Decimal('0.2')

    print(f"d1 = {d1}, d2 = {d2}")
    print(f"Addition: {d1} + {d2} = {d1 + d2}")
    print(f"Multiplication: {d1} * {d2} = {d1 * d2}")

    # Compare with float arithmetic
    f1 = 0.1
    f2 = 0.2
    print(f"\nFloat arithmetic:")
    print(f"f1 = {f1}, f2 = {f2}")
    print(f"Addition: {f1} + {f2} = {f1 + f2}")
    print(f"Multiplication: {f1} * {f2} = {f1 * f2}")


def demonstrate_number_methods():
    print("\n=== Number Methods ===")
    num = 42

    print(f"Number: {num}")
    print(f"Binary: {bin(num)}")
    print(f"Hexadecimal: {hex(num)}")
    print(f"Octal: {oct(num)}")

    # Complex numbers
    c1 = 3 + 4j
    c2 = 1 + 2j
    print(f"\nComplex numbers:")
    print(f"c1 = {c1}, c2 = {c2}")
    print(f"Addition: {c1} + {c2} = {c1 + c2}")
    print(f"Multiplication: {c1} * {c2} = {c1 * c2}")
    print(f"Absolute value: |{c1}| = {abs(c1)}")


def demonstrate_advanced_math():
    print("\n=== Advanced Math Operations ===")
    x = 16
    y = 3

    print(f"x = {x}, y = {y}")
    print(f"Factorial of {y}: {y}! = {math.factorial(y)}")
    print(f"GCD of {x} and {y}: gcd({x}, {y}) = {math.gcd(x, y)}")
    print(f"Hypotenuse: hypot({x}, {y}) = {math.hypot(x, y)}")

    # Trigonometric functions with degrees
    angle = 45
    print(f"\nTrigonometric functions for {angle} degrees:")
    print(f"Sine: sin({angle}°) = {math.sin(math.radians(angle))}")
    print(f"Cosine: cos({angle}°) = {math.cos(math.radians(angle))}")
    print(f"Tangent: tan({angle}°) = {math.tan(math.radians(angle))}")


def main():
    print("Python Math Functions Examples")
    print("=" * 30)

    demonstrate_basic_math()
    demonstrate_math_module()
    demonstrate_random_functions()
    demonstrate_decimal_operations()
    demonstrate_number_methods()
    demonstrate_advanced_math()


if __name__ == "__main__":
    main()
