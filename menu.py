#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle
from kivy.animation import Animation

class Menu(Widget):

    snake = ObjectProperty(None)
    apple = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(Menu, self).__init__(*args, **kwargs)
        self.bind(size=self.on_size)

    def on_size(self, *args):
        self.draw_background()
        self.make_snake_animation()
        self.make_apple_animation()

    def draw_background(self):
        with self.canvas.before:
            Rectangle(texture=self.resources.background_texture, pos=self.pos, size=self.size)

    def make_snake_animation(self):
        Animation.cancel_all(self.snake)

        self.snake.pos = (self.size[0] * 1.0 / 4.0 - self.snake.width / 2, self.size[1] * 3.0 / 4.0 - self.snake.height / 2)

        anim = (Animation(x=self.snake.pos[0] + 20, y=self.snake.pos[1] - 20, duration=10, transition="in_bounce")
                + Animation(x=self.snake.pos[0] - 20, y=self.snake.pos[1] + 20, duration=10, transition="in_out_elastic"))
        anim.repeat = True
        anim.start(self.snake)

    def make_apple_animation(self):
        Animation.cancel_all(self.apple)
        anim = (Animation(size=(self.apple.size[0] - 20, self.apple.size[1] - 20),  duration=3)
                + Animation(size=(self.apple.size[0] + 10, self.apple.size[1] + 10), duration=3))
        anim.repeat = True
        anim.start(self.apple)
