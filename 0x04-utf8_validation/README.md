# UTF-8 Validation Project

## Description

This project is part of the **ALX Interview Preparation** and involves writing a Python function that determines if a given data set represents a valid UTF-8 encoding. UTF-8 is a variable-length character encoding that can encode characters using one to four bytes. The goal is to validate whether the provided data follows the rules of UTF-8 encoding.

___

## Learning Objectives

In this project, I will apply the following concepts:
- **Bitwise Operations**: Manipulating bits using AND, OR, and bit shifts in Python.
- **UTF-8 Encoding Rules**: Understanding the structure of valid UTF-8 encoded sequences (1 to 4 bytes).
- **Boolean Logic**: Making logical decisions to validate byte patterns.
- **Data Representation**: Interpreting integers as byte data, focusing on the 8 least significant bits.
- **List Manipulation**: Iterating through a list of integers representing bytes.

___

## Requirements

- **Python Version**: the code will be run and tested on Python 3.4.3.
- **Operating System**: Ubuntu 20.04 LTS.
- **Code Style**: Follow PEP 8 style (version 1.7.x).
- All files are executable.

___

## Project Files

### `0-validate_utf8.py`
This file contains the main function to validate the UTF-8 encoded data.

### Prototype:
```python
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (list): A list of integers where each integer represents 1 byte.
        
    Returns:
        bool: True if data is a valid UTF-8 encoding, otherwise False.
    """
```

___

## Usage

The function `validUTF8(data)` should be used to validate the UTF-8 encoding. It takes a list of integers as input where each integer represents a byte. It will return `True` if the data is a valid UTF-8 encoding and `False` otherwise.

### Example Usage

```python
#!/usr/bin/python3
from 0-validate_utf8 import validUTF8

# Example 1: Valid UTF-8 data (ASCII)
data = [65]  # ASCII for 'A'
print(validUTF8(data))  # Output: True

# Example 2: Valid UTF-8 sentence
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

# Example 3: Invalid UTF-8 data
data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```

___

## Bitwise Explanation

- A **1-byte character** (ASCII) starts with a `0xxxxxxx` pattern.
- **Multi-byte characters**:
  - **2-byte** characters start with `110xxxxx` followed by `10xxxxxx`.
  - **3-byte** characters start with `1110xxxx` followed by two `10xxxxxx`.
  - **4-byte** characters start with `11110xxx` followed by three `10xxxxxx`.
  
The function checks each byte to ensure it follows the correct UTF-8 encoding patterns using bitwise operations.

___

## Testing

You can run the provided `0-main.py` file to test your implementation:

```bash
$ ./0-main.py
True
True
False
```
___

## Author

Project by **Gideon Phiri**  
GitHub: [Gideon-Phiri](https://github.com/Gideon-Phiri)

___
