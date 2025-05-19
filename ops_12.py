```python
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <argument>", file=sys.stderr)
        sys.exit(1)

    try:
        arg = int(sys.argv[1])
        print(arg * 2)
    except ValueError:
        print("Invalid input. Please provide an integer.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```