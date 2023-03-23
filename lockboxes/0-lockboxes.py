#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
"""


def canUnlockAll(boxes):
    """
    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """
    keys = [0]
    for key in keys:
        box = boxes[key]
        for key_in_box in box:
            if key_in_box not in keys and key_in_box < len(boxes):
                keys.append(key_in_box)
    if len(keys) == len(boxes):
        return True
    return False
