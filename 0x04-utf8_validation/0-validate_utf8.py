#!/usr/bin/python3
"""
Function that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Check if data represents valid UTF-8 encoding.
    Args:
        data (list): List of integers where each integer represents 1 byte.
    Returns:
        bool: True if valid UTF-8, False otherwise.
    """
    # Number of bytes remaining to be validated as continuation bytes
    num_bytes = 0

    # Masks for checking different byte types
    mask_1_byte = 0b10000000  # Mask to check if byte starts with 0 (ASCII)
    mask_2_bytes = 0b11100000  # Mask for leading byte of 2-byte character
    mask_3_bytes = 0b11110000  # Mask for leading byte of 3-byte character
    mask_4_bytes = 0b11111000  # Mask for leading byte of 4-byte character
    mask_continuation = 0b11000000  # Mask for cont byte (must be 10xxxxxx)

    for byte in data:
        byte = byte & 0xFF  # Ensure we're working with only 8 bits (1 byte)

        # If we're expecting continuation bytes
        if num_bytes == 0:
            # Check for 1-byte character (ASCII range)
            if (byte & mask_1_byte) == 0:
                continue
            # Check for 2-byte character
            elif (byte & mask_2_bytes) == 0b11000000:
                num_bytes = 1
            # Check for 3-byte character
            elif (byte & mask_3_bytes) == 0b11100000:
                num_bytes = 2
            # Check for 4-byte character
            elif (byte & mask_4_bytes) == 0b11110000:
                num_bytes = 3
            else:
                # Invalid leading byte
                return False
        else:
            # Check that byte is a valid continuation byte (10xxxxxx)
            if (byte & mask_continuation) != 0b10000000:
                return False
            num_bytes -= 1

    # If we have leftover continuation bytes that haven't been matched
    return num_bytes == 0
