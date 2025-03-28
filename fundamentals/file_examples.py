import os
from pathlib import Path
from typing import List, Union


def demonstrate_file_operations():
    print("\n=== File Operations in Python ===")

    # Example 1: Basic File Operations
    def basic_file_operations():
        print("\n1. Basic File Operations:")

        # Create a test file
        with open('test.txt', 'w') as f:
            f.write('Hello, World!\n')
            f.write('This is a test file.\n')

        # Read the file
        with open('test.txt', 'r') as f:
            content = f.read()
            print("File content:")
            print(content)

        # Append to file
        with open('test.txt', 'a') as f:
            f.write('Appending new line.\n')

        # Read line by line
        print("\nReading line by line:")
        with open('test.txt', 'r') as f:
            for line in f:
                print(line.strip())

        # Clean up
        os.remove('test.txt')

    # Example 2: File Path Operations
    def file_path_operations():
        print("\n2. File Path Operations:")

        # Using pathlib
        current_dir = Path.cwd()
        print(f"Current directory: {current_dir}")

        # Create a test directory
        test_dir = current_dir / 'test_dir'
        test_dir.mkdir(exist_ok=True)

        # Create multiple files in the test directory
        files = {
            'test1.txt': 'This is test file 1 content',
            'test2.txt': 'This is test file 2 content',
            'subdir': {
                'test3.txt': 'This is test file 3 content',
                'test4.txt': 'This is test file 4 content'
            }
        }

        # Create files and subdirectories
        for name, content in files.items():
            if isinstance(content, dict):
                # Create subdirectory
                subdir = test_dir / name
                subdir.mkdir(exist_ok=True)
                # Create files in subdirectory
                for subname, subcontent in content.items():
                    (subdir / subname).write_text(subcontent)
            else:
                # Create file
                (test_dir / name).write_text(content)

        # Function to print directory structure with indentation
        def print_directory_structure(path: Path, level: int = 0):
            indent = "  " * level
            print(f"{indent}📁 {path.name}/")

            # Print files first
            for item in sorted(path.iterdir()):
                if item.is_file():
                    print(f"{indent}  📄 {item.name}")
                    # Print file content with additional indentation
                    try:
                        content = item.read_text()
                        print(f"{indent}    Content: {content}")
                    except Exception as e:
                        print(f"{indent}    Error reading file: {e}")

            # Then print directories
            for item in sorted(path.iterdir()):
                if item.is_dir():
                    print_directory_structure(item, level + 1)

        # Print the directory structure
        print("\nDirectory structure with contents:")
        print_directory_structure(test_dir)

        # Clean up recursively
        def remove_directory(path: Path):
            if path.is_file():
                path.unlink()
            else:
                for item in path.iterdir():
                    remove_directory(item)
                path.rmdir()

        remove_directory(test_dir)

    # Example 3: File Modes and Context Managers
    def file_modes_and_context():
        print("\n3. File Modes and Context Managers:")

        # Create a test file
        with open('test.txt', 'w') as f:
            f.write('Line 1\nLine 2\nLine 3')

        # Different file modes
        print("\nReading with different modes:")

        # Read mode
        with open('test.txt', 'r') as f:
            print("Read mode:")
            print(f.read())

        # Binary read mode
        with open('test.txt', 'rb') as f:
            print("\nBinary read mode:")
            print(f.read())

        # Read with encoding
        with open('test.txt', 'r', encoding='utf-8') as f:
            print("\nRead with UTF-8 encoding:")
            print(f.read())

        # Clean up
        os.remove('test.txt')

    # Example 4: File Position and Seeking
    def file_position_and_seeking():
        print("\n4. File Position and Seeking:")

        # Create a test file
        with open('test.txt', 'w') as f:
            f.write('Line 1\nLine 2\nLine 3\nLine 4')

        with open('test.txt', 'r') as f:
            # Read first line
            print("First line:", f.readline().strip())

            # Get current position
            print(f"Current position: {f.tell()}")

            # Seek to beginning
            f.seek(0)
            print("After seeking to beginning:", f.readline().strip())

            # Seek to specific position
            f.seek(10)
            print("After seeking to position 10:", f.readline().strip())

        # Clean up
        os.remove('test.txt')

    # Example 5: File Error Handling
    def file_error_handling():
        print("\n5. File Error Handling:")

        # Try to open non-existent file
        try:
            with open('nonexistent.txt', 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print("File not found error handled")

        # Try to write to read-only file
        try:
            with open('readonly.txt', 'w') as f:
                f.write('test')
            os.chmod('readonly.txt', 0o444)  # Make file read-only
            with open('readonly.txt', 'w') as f:
                f.write('test')
        except PermissionError:
            print("Permission error handled")
        finally:
            # Clean up
            os.chmod('readonly.txt', 0o666)  # Restore write permissions
            os.remove('readonly.txt')

    # Run all examples
    basic_file_operations()
    file_path_operations()
    file_modes_and_context()
    file_position_and_seeking()
    file_error_handling()


def main():
    print("Python File Operations Examples")
    print("=" * 30)
    demonstrate_file_operations()


if __name__ == "__main__":
    main()
