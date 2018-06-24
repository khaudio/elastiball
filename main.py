#!/usr/bin/env python

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Elastiball(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ElastiballApp(App):
    pass


if __name__ == '__main__':
    ElastiballApp().run()
