#!/usr/bin/python
# -*- coding: utf-8 -*-

from copy import copy
from element import Element

class Snake(object):

    def __init__(self, head_position, element_size, snake_body_size = 3):
        super(Snake, self).__init__()
        self.__elements = [Element(head_position, element_size)]
        self.__path = [self.__elements[0]]
        self.__number_of_elements = 1 + snake_body_size

    @property
    def head(self):
        return self.__elements[0]

    @property
    def body(self):
        return self.__elements[1:]

    def extend(self):
        self.__number_of_elements = self.__number_of_elements + 1

    def move(self, difference):
        new = copy(self.head)
        new.position = new.position + difference

        self.__path.insert(0, new)
        self.__elements = [new]
        last_added = new

        for step in self.__path:
            if len(self.__elements) < self.__number_of_elements and not last_added.overlap(step):
                last_added = step
                self.__elements.append(step)

