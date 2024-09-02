#!/usr/bin/python3
"""Lockboxes are now opened"""


def open_box(box, _list, opened):
    """Open the boxes"""
    if len(box) == 0:
        return (opened)
    for key in box:
        if key not in opened and key < len(_list):
            break
    else:
        return (opened)
    ops = opened
    for key in box:
        if key > len(_list) - 1:
            continue
        if key not in ops:
            ops.add(key)
            small_open = open_box(_list[key], _list, ops)
            for item in small_open:
                ops.add(item)
    return (ops)


def canUnlockAll(boxes):
    """Check if all boxes can be unlocked"""
    if len(boxes) == 0:
        return (True)
    my_list = boxes
    opened_boxes = list(open_box(my_list[0], my_list, {0}))
    if len(opened_boxes) == len(my_list):
        return (True)
    else:
        return (False)
