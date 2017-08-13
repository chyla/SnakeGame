#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.metrics import dp
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Rectangle
import random

from snake import Snake
from element import Element


class SnakeGame(Widget):

    score = NumericProperty(0)
    game_over = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(SnakeGame, self).__init__(*args, **kwargs)
        self.bind(size=self.__draw_background)
        self.__drawing_instructions = InstructionGroup()
        
    def start_game(self):
        self.score = 0
        self.__snake = None
        self.__fruit = None
        self.__game_finished = False

        self.canvas.before.add(self.__drawing_instructions)
        self.__create_game_objects()

        self.__event = Clock.schedule_interval(self.__redraw_scene, 1.00 / 60.00)

    def stop_game(self):
        self.resources.end_sound.play()
        self.__game_finished = True
        self.__event.cancel()
        self.__show_game_over()

        def go_to_menu_screen(*args):
            self.manager.current = 'MenuScreen'
            self.canvas.before.remove(self.__drawing_instructions)
            self.__drawing_instructions.clear()
            self.__hide_game_over()
        Clock.schedule_once(go_to_menu_screen, 3)

    def __show_game_over(self):
        self.game_over.opacity = 1

    def __hide_game_over(self):
        self.game_over.opacity = 0

    def __redraw_scene(self, time_delta):
        self.__drawing_instructions.clear()
        self.__draw_snake()
        self.__draw_fruit()
        
    def __draw_background(self, *args):
        with self.canvas.before:
            Rectangle(texture=self.resources.background_texture, pos=self.pos, size=self.size)

    def __draw_snake(self):
        for element in self.__snake.body:
            item = Rectangle(texture=self.resources.snake_body_texture, pos=element.position, size=element.size)
            self.__drawing_instructions.add(item)

        item = Rectangle(texture=self.resources.snake_head_texture, pos=self.__snake.head.position, size=self.__snake.head.size)
        self.__drawing_instructions.add(item)

    def __draw_fruit(self):
        item = Rectangle(texture=self.resources.apple_texture, pos=self.__fruit.position, size=self.__fruit.size)
        self.__drawing_instructions.add(item)

    def __create_game_objects(self):
        objects_size = (dp(45), dp(45))
        def random_position_in_visible_space():
            return (random.randrange(objects_size[0], self.size[0] - objects_size[0]),
                    random.randrange(objects_size[1], self.size[1] - objects_size[1]))

        if self.__snake is None:
            self.__snake = Snake(random_position_in_visible_space(), objects_size)

        if self.__fruit is None:
            self.__fruit = Element(random_position_in_visible_space(), objects_size)

    def on_touch_down(self, event):
        if self.__snake.head.contains_position(event.pos):
            event.grab(self)
            return True

        return super(SnakeGame, self).on_touch_down(event)

    def on_touch_move(self, event):
        if not self.__game_finished and event.grab_current is self:
            self.__snake.move(event.dpos)
            self.__serve_collisions()
            return True

        return super(SnakeGame, self).on_touch_move(event)

    def on_touch_up(self, event):
        if event.grab_current is self:
            event.ungrab(self)
            return True

        return super(SnakeGame, self).on_touch_up(event)

    def __serve_collisions(self):
        if self.__snake.head.overlap(self.__fruit):
            self.resources.score_sound.play()
            self.score = self.score + 1
            self.__snake.extend()
            self.__fruit = None

            self.__create_game_objects()

        if any((self.__snake.head.overlap(body) for body in self.__snake.body)):
            self.stop_game()
