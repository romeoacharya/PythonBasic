# PythonBasic
# Python Utilities

A collection of basic Python algorithms, number conversions, set operations, and small console demos.

## Features

- Calculate the average of one or more numbers
- Search sorted lists using binary search
- Check whether a string is a palindrome
- Calculate factorial and Fibonacci values
- Find the greatest common divisor and least common multiple
- Check prime numbers and calculate prime factors
- Convert between decimal, binary, and hexadecimal formats
- Roll two six-sided dice
- Generate all subsets of a string
- Perform union, intersection, difference, and symmetric difference operations on sets
- Compare list, dictionary, and tuple element access timing
- Play Rock-Paper-Scissors in the console

Set operations use:

```python
seta = {23, 45, 34}
setb = {23, 45, 34, 56, 78}
```

## Running the Program

Run `main.py` with Python:

```powershell
python main.py
```

Some functions are demonstration helpers and may need to be called manually. For example:

```python
from main import factorial, is_prime

print(factorial(5))
print(is_prime(29))
```

## Running the Tests

The test suite is written with Python's built-in `unittest` module and is located in `test_main.py`.

Run all tests:

```powershell
python -m unittest test_main.py
```

Or run the test file directly:

```powershell
python test_main.py
```

The tests cover averages, searching, palindromes, factorials, Fibonacci numbers, GCD and LCM, prime calculations, number conversions, dice rolls, string subsets, and set operations. Random dice values are mocked to provide predictable test results.

## Project Files

- `main.py` — contains the utility functions and demonstrations
- `test_main.py` — contains the automated unit tests
