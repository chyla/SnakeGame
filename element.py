#!/usr/bin/python
# -*- coding: utf-8 -*-

from position import Position

class Element(object):

    def __init__(self, position, size):
        super(Element, self).__init__()
        self.position = Position(position)
        self.size = size

    def contains_position(self, position):
        end_position = self.position + self.size

        # interval comparison
        return self.position < Position(position) < end_position

    def overlap(self, element):
        diff = self.position - element.position
        return abs(diff.x) < self.size[0] and abs(diff.y) < self.size[1]
