#!/usr/bin/python
# -*- coding: utf-8 -*-

class Position(object):

    def __init__(self, (x, y)):
        super(Position, self).__init__()
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __getitem__(self, key):
        return (self.__x, self.__y)[key]

    def __add__(self, other):
        return Position((self.__x + other[0], self.__y + other[1]))

    def __sub__(self, other):
        return self.__add__((-other[0], -other[1]))

    def __lt__(self, other):
        return self.__x < other[0] and self.__y < other[1]
