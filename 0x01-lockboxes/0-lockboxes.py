#!/usr/bin/python3
"""
0-lockboxes.py
This module contains the canUnlockAll function.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list):
           - A list of lists, where each list contains keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)  # Number of boxes
    unlocked = {0}  # Set of unlocked boxes, starting with box 0
    stack = boxes[0]  # Start with keys from the first box

    # Process the stack to unlock boxes
    while stack:
        key = stack.pop()  # Take a key from the stack

        # If the key unlocks a new box
        if key < n and key not in unlocked:
            unlocked.add(key)  # Mark the box as unlocked
            stack.extend(boxes[key])  # Add keys from the newly unlocked box

    # If all boxes are unlocked, return True; else return False
    return len(unlocked) == n
