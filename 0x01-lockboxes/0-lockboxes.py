#!/usr/bin/python3
"""
0-lockboxes.py
This module contains the canUnlockAll function which determines
if all boxes can be unlocked given a set of keys.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    Args:
        boxes (list of lists):
                            - A list of lists
                            - where each list contains keys to other boxes.
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    if not boxes:
        return False  # No boxes exist

    n = len(boxes)  # Number of boxes
    unlocked = [False] * n
    unlocked[0] = True  # The first box is unlocked by default
    stack = boxes[0]  # Initialize stack with keys from the first box

    # Process the stack
    while stack:
        key = stack.pop()
        # Ensure the key unlocks a valid, locked box
        if 0 <= key < n and not unlocked[key]:
            unlocked[key] = True  # Unlock the box
            stack.extend(boxes[key])
    # Check if all boxes are unlocked
    return all(unlocked)
