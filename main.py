from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Rectangle
from kivy.core.image import Image

import random

# Kivy needs a class for your app
class WrApp(App):
  def build(self):
    return Cv()

# And we go ahead and put a custom widget in there
class Cv(Widget):
  def __init__(self):
    super(Cv, self).__init__()
  
    # This lets us move the logo around at 30 fps
    Clock.schedule_interval(self.drift, 1/30)
    
    # This sets up the drift speed
    self.dx=2
    self.dy=2

    # This tells Kivy what to draw, and it'll update it for us when the object changes
    with self.canvas:
      self.rect=Rectangle(texture=Image("dvd_logo.png", mipmap=True).texture,
                          size=(128,128), pos=(10,10))
  
  # This is some super simple bouncing =]
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

  # A little interaction for tapping the screen
  def on_touch_down(self, t):
    self.dx=random.choice([-3,3])
    self.dy=random.choice([-3,3])

# Lastly, now that everything's defined, run it!
WrApp().run()
