#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.core.audio import SoundLoader
from kivy.uix.image import Image

class ResourcesLoader(object):

    def load_textures(self):
        self.background_texture = Image(source="data/background.png").texture
        self.background_texture.wrap = 'repeat'
        self.background_texture.uvsize = (5, 5)

        self.snake_head_texture = Image(source="data/snake-head.png").texture
        self.snake_body_texture = Image(source="data/snake-body.png").texture

        self.apple_texture = Image(source="data/apple.png").texture

    def load_sounds(self):
        self.background_sound = SoundLoader.load('data/game-sound.wav')
        self.background_sound.loop = True

        self.score_sound = SoundLoader.load('data/game-score.wav')
        self.end_sound = SoundLoader.load('data/game-end.wav')
