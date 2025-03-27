def demonstrate_escape_sequences():
    print("\n=== Escape Sequences ===")
    print("New line: Hello\nWorld")
    print("Tab: Hello\tWorld")
    print("Backslash: This is a backslash \\")
    print("Single quote: It\'s a nice day")
    print("Double quote: \"Hello\"")
    print("ABCDEFGHIJKLMNOP Carriage return: Hello\rWorld")
    print("Backspace: Hello\bWorld")
    print("Form feed: Hello\fWorld")
    print("Vertical tab: Hello\vWorld")
    print("Octal value: \110\145\154\154\157")  # "Hello" in octal
    print("Hex value: \x48\x65\x6c\x6c\x6f")    # "Hello" in hex


def demonstrate_string_functions():
    print("\n=== String Functions ===")
    text = "Hello, World! Welcome to Python"

    # Case conversion
    print(f"Original: {text}")
    print(f"Upper: {text.upper()}")
    print(f"Lower: {text.lower()}")
    print(f"Title: {text.title()}")
    print(f"Capitalize: {text.capitalize()}")

    # Length and counting
    print(f"\nLength: {len(text)}")
    print(f"Count 'l': {text.count('l')}")
    print(f"Count 'World': {text.count('World')}")

    # Finding and replacing
    print(f"\nFind 'World': {text.find('World')}")
    print(f"Replace 'World' with 'Python': {text.replace('World', 'Python')}")

    # Stripping whitespace
    print(f"\nStrip: '{text.strip()}'")
    print(f"Lstrip: '{text.lstrip()}'")
    print(f"Rstrip: '{text.rstrip()}'")

    # Splitting and joining
    print(f"\nSplit: {text.split()}")
    print(f"Split by comma: {text.split(',')}")
    print(f"Join: {'-'.join(text.split())}")


def demonstrate_string_formatting():
    print("\n=== String Formatting ===")
    name = "Alice"
    age = 25
    height = 1.75

    # % operator
    print("Using % operator:")
    print("Name: %s, Age: %d, Height: %.2f" % (name, age, height))

    # str.format()
    print("\nUsing str.format():")
    print("Name: {}, Age: {}, Height: {:.2f}".format(name, age, height))
    print("Name: {0}, Age: {1}, Height: {2:.2f}".format(name, age, height))
    print("Name: {n}, Age: {a}, Height: {h:.2f}".format(
        n=name, a=age, h=height))

    # f-strings (Python 3.6+)
    print("\nUsing f-strings:")
    print(f"Name: {name}, Age: {age}, Height: {height:.2f}")
    print(f"Age in 5 years: {age + 5}")
    print(f"Name length: {len(name)}")


def demonstrate_substrings():
    print("\n=== Substrings ===")
    text = "Hello, World! Welcome to Python"

    # Basic slicing
    print(f"Original: {text}")
    print(f"First 5 characters: {text[:5]}")
    print(f"Last 5 characters: {text[-5:]}")
    print(f"Characters 7-12: {text[7:12]}")

    # Step in slicing
    print(f"\nEvery second character: {text[::2]}")
    print(f"Reverse string: {text[::-1]}")

    # Negative indexing
    print(f"\nLast word: {text.split()[-1]}")
    print(f"Second to last word: {text.split()[-2]}")

    # String slicing with step
    print(
        f"\nReverse each word: {' '.join(word[::-1] for word in text.split())}")


def main():
    print("Python String Operations Examples")
    print("=" * 30)

    demonstrate_escape_sequences()
    demonstrate_string_functions()
    demonstrate_string_formatting()
    demonstrate_substrings()


if __name__ == "__main__":
    main()
