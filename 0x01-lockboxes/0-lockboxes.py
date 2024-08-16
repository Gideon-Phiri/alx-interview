#!/usr/bin/python3

def canUnlockAll(boxes):
    opened_boxes = set()
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()  # Get the last box in the stack
        if current_box not in opened_boxes:
            opened_boxes.add(current_box)  # Mark this box as opened
            for key in boxes[current_box]:
                if key < len(boxes) and key not in opened_boxes:
                    stack.append(key)  # Add all keys to the stack

    # Check if we've opened all the boxes
    return len(opened_boxes) == len(boxes)
