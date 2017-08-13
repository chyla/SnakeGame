#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
import random

from menu import Menu
from resources_loader import ResourcesLoader
from snake_game import SnakeGame


class MenuScreen(Screen):

    menu = ObjectProperty(None)

    def __init__(self, resources, *args, **kwargs):
        super(MenuScreen, self).__init__(*args, **kwargs)
        self.resources = resources

    def on_pre_enter(self, *args):
        self.menu.manager = self.manager
        self.menu.resources = self.resources


class SnakeGameScreen(Screen):

    snake_game = ObjectProperty(None)

    def __init__(self, resources, *args, **kwargs):
        super(SnakeGameScreen, self).__init__(*args, **kwargs)
        self.resources = resources

    def on_pre_enter(self, *args):
        self.snake_game.manager = self.manager
        self.snake_game.resources = self.resources

    def on_enter(self, *args):
        self.snake_game.start_game()


class SnakeApp(App):
    def build(self):
        random.seed()

        self.resources = ResourcesLoader()
        self.resources.load_textures()
        self.resources.load_sounds()

        menu_screen = MenuScreen(self.resources, name='MenuScreen')
        snake_game_screen = SnakeGameScreen(self.resources, name='SnakeGameScreen')

        sm = ScreenManager(transition=SwapTransition())
        sm.add_widget(menu_screen)
        sm.add_widget(snake_game_screen)

        return sm

    def on_start(self):
        self.resources.background_sound.play()

    def on_stop(self):
        self.resources.background_sound.stop()


if __name__ == '__main__':
    SnakeApp().run()
