from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Rectangle
from kivy.core.image import Image

import random

class Cv(Widget):
  def __init__(self):
    super(Cv, self).__init__()
  
    Clock.schedule_interval(self.drift, 1/30)
    
    self.dx=2
    self.dy=2

    with self.canvas:
      self.rect=Rectangle(texture=Image("dvd_logo.png", mipmap=True).texture,
                          size=(128,128), pos=(10,10))
  
  def drift(self, dt):
    self.rect.pos=(self.rect.pos[0]+self.dx,
                   self.rect.pos[1]+self.dy)

    if self.rect.pos[0]+self.rect.size[0]>self.size[0]:
      self.dx=-2
    if self.rect.pos[1]+self.rect.size[1]>self.size[1]:
      self.dy=-2
    if self.rect.pos[0]<0:
      self.dx=2
    if self.rect.pos[1]<0:
      self.dy=2

  def on_touch_down(self, t):
    self.dx=random.choice([-3,3])
    self.dy=random.choice([-3,3])

class WrApp(App):
  def build(self):
    return Cv()

WrApp().run()
