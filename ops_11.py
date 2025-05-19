```python
import sys

def aadadadad():
    if len(sys.argv) != 2:
        print("Usage: python aadadadad.py <input_string>", file=sys.stderr)
        sys.exit(1)

    input_string = sys.argv[1]
    try:
        int(input_string)  #Check if input is an integer
        print("Input is an integer")

    except ValueError:
        if input_string.isalpha():
            print("Input is an alphabet string")
        elif input_string.isalnum():
            print("Input is an alphanumeric string")
        else:
            print("Input is a string with special characters")


if __name__ == "__main__":
    aadadadad()

```