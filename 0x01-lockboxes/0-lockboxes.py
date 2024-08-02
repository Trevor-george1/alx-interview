#!/usr/bin/env python3
"""method that determines if all boxes can be opened"""


def canUnlockAll(boxes):
    """returns True if all boxes cn be opened"""
    visited = {0}

    queue = [boxes[0]]

    while queue:
        box = queue.pop(0)

        for key in box:
            if key not in visited and key < len(boxes):
                visited.add(key)

                queue.append(boxes[key])

    return len(visited) == len(boxes)
