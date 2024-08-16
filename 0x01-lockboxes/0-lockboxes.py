
ckboxes.py
This module contains the function canUnlockAll that determines if all boxes 
in a list of boxes can be opened starting from the first box.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    
    :param boxes: List of lists where each sublist represents keys inside a box.
                  A key with the same number as a box opens that box.
    :return: True if all boxes can be unlocked, otherwise False.
    """
    # A set to keep track of all opened boxes
    opened_boxes = set()
    
    # Initialize the stack with the first box (box 0 is always open)
    stack = [0]

    while stack:
        # Pop the last box from the stack
        current_box = stack.pop()

        # If this box has not been opened yet
        if current_box not in opened_boxes:
            # Mark the current box as opened
            opened_boxes.add(current_box)

            # Add keys found in the current box to the stack
            for key in boxes[current_box]:
                # Ensure the key corresponds to a valid box that hasn't been opened
                if key < len(boxes) and key not in opened_boxes:
                    stack.append(key)

    # If the number of opened boxes equals the total number of boxes, return True
    return len(opened_boxes) == len(boxes)
