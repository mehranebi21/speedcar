from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.properties import NumericProperty
import random

Window.size = (400, 700)

class Game(Widget):

    player_x = NumericProperty(170)
    enemy_x = NumericProperty(170)
    enemy_y = NumericProperty(700)

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.speed = 8

        Clock.schedule_interval(
            self.update,
            1.0 / 60.0
        )

    def update(self, dt):

        self.canvas.clear()

        with self.canvas:

            Color(0.1, 0.1, 0.1)

            Rectangle(
                pos=(0,0),
                size=(400,700)
            )

            Color(0.3,0.3,0.3)

            Rectangle(
                pos=(70,0),
                size=(260,700)
            )

            Color(0,0.8,1)

            Rectangle(
                pos=(self.player_x,50),
                size=(60,100)
            )

            Color(1,0,0)

            Rectangle(
                pos=(self.enemy_x,self.enemy_y),
                size=(60,100)
            )

        self.enemy_y -= self.speed

        if self.enemy_y < -100:

            self.enemy_y = 700

            self.enemy_x = random.choice(
                [90,170,250]
            )

    def on_touch_move(self, touch):

        self.player_x = touch.x - 30

        if self.player_x < 90:
            self.player_x = 90

        if self.player_x > 250:
            self.player_x = 250


class MyApp(App):

    def build(self):
        return Game()


MyApp().run()
