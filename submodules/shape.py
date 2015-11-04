#!/usr/bin/env python
import pdb
from submodules import canvas

class Shape():
  def draw(self):
    return 0
  def name(self):
    print ("Shape")
  def __init__(self, size):
    self.size = size

class Spiral(Shape):
  def draw(self):
    starting = self.size-1
    self.draw_helper(starting, 0, starting, 0)
    return self.canvas
  
  # Recursively draws lines that are one shorter, and go in a different direction in the following pattern: left, down, right, up
  def draw_helper(self, x, y, remaining, direction):

    # direction 0 is left, 1 is down, 2 is right, 3 is up
    direction = direction % 4
    if (direction == 0):
      x1 = x - remaining
      y1 = y
    elif (direction == 1):
      x1 = x
      y1 = y + remaining
    elif (direction == 2):
      x1 = x + remaining
      y1 = y
    elif (direction == 3):
      x1 = x
      y1 = y - remaining

    self.canvas.drawLine(x,y,x1,y1)

    if remaining > 0:
      self.draw_helper(x1, y1, remaining-1, direction+1)
    else:
      return 0
  def name(self):
    print ("Spiral, of size: " + self.size)
  
  # takes input (shape, size, format)
  def __init__(self, input):
    self.shape = input[0]
    self.size = int(input[1])
    self.format = input[2]

    self.canvas = canvas.Canvas(self.size, self.size, self.format)

class Square(Shape):
  def draw(self):
    return self.canvas
  def name(self):
    print ("Square, of size: " + self.size)
  # takes input (shape, size, format)
  def __init__(self, input):
    self.shape = input[0]
    self.size = int(input[1])
    self.format = input[2]

    self.canvas = canvas.Canvas(self.size, self.size, self.format)
