#!/usr/bin/python3
def validUTF8(data):
    # Count the number of bytes left to validate as continuation bytes
    num_bytes = 0

    # Masks to check most significant bits
    mask_1_byte = 0b10000000  # 1-byte mask (ASCII characters)
    mask_n_bytes = 0b11100000  # Mask for n-byte sequences
    mask_2_bytes = 0b11000000  # 2-byte mask
    mask_3_bytes = 0b11110000  # 3-byte mask
    mask_4_bytes = 0b11111000  # 4-byte mask
    mask_continuation = 0b11000000  # Continuation byte mask
    mask_continuation_check = 0b10000000  # Check for continuation bytes

    for byte in data:
        byte = byte & 0xFF  # Only care about the last 8 bits

        # If num_bytes is 0, we're expecting a new character
        if num_bytes == 0:
            if (byte & mask_1_byte) == 0:  # 1-byte character (ASCII)
                continue
            elif (byte & mask_2_bytes) == 0b11000000:  # 2-byte character
                num_bytes = 1
            elif (byte & mask_3_bytes) == 0b11100000:  # 3-byte character
                num_bytes = 2
            elif (byte & mask_4_bytes) == 0b11110000:  # 4-byte character
                num_bytes = 3
            else:
                return False  # Invalid leading byte
        else:
            # Check if it's a valid continuation byte
            if (byte & mask_continuation) != mask_continuation_check:
                return False
            num_bytes -= 1

    # If num_bytes is not zero, we have incomplete characters left
    return num_bytes == 0
