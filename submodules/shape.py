#!/usr/bin/env python
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
    self.draw_helper(self.size-1,0)
    return self.canvas
  
  def draw_helper(self,remaining, direction):
    self.canvas.drawLine(remaining,0,0,0)

    if remaining > 0:
      draw_helper(remaining-1, direction+1)
    else:
      return 0  
  
  def name(self):
    print ("Spiral, of size: " + self.size)
  
  def __init__(self, input):
    # takes input (shape, size, format)
    self.shape = input[0]
    self.size = int(input[1])
    self.format = input[2]

    self.canvas = canvas.Canvas(self.size, self.size, self.format)

class Square(Shape):
  def draw(self):
    return self.canvas
  def name(self):
    print ("Square, of size: " + self.size)
  def __init__(self, input):
    # takes input (shape, size, format)
    self.shape = input[0]
    self.size = input[1]
    self.format = input[2]

    self.canvas = canvas.Canvas(self.size, self.size, self.format)
