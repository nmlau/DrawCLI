#!/usr/bin/env python
import pdb
from submodules import canvas

class Shape():
  def draw(self):
    return
  def __init__(self, size):
    self.size = size

class Spiral(Shape):
  def draw(self):
    self.draw_helper(self.size-1, 0, self.size-1, 0)
    return self.canvas
  
  # Recursively draws lines that are one shorter, and go in a different direction in the following pattern: left, down, right, up
  def draw_helper(self, x, y, length, direction):

    # direction 0 is left, 1 is down, 2 is right, 3 is up
    direction = direction % 4
    x1 = x
    y1 = y
    if (direction == 0):
      x1 = x - length
    elif (direction == 1):
      y1 = y + length
    elif (direction == 2):
      x1 = x + length
    elif (direction == 3):
      y1 = y - length

    self.canvas.drawLine(x,y,x1,y1)

    if length > 0:
      self.draw_helper(x1, y1, length-1, direction+1)
    else:
      return
  
  # takes input (shape, size, format)
  def __init__(self, input):
    self.shape = input[0]
    self.size = input[1]
    self.format = input[2]
    
    self.canvas = canvas.Canvas(self.size, self.size, self.format)

class Square(Shape):
  def draw(self):
    length = self.size-1
    self.canvas.drawLine(0,0,length,0)
    self.canvas.drawLine(length,0,length,length)
    self.canvas.drawLine(length,length,0,length)
    self.canvas.drawLine(0,length,0,0)
    return self.canvas
  # takes input (shape, size, format)
  def __init__(self, input):
    self.shape = input[0]
    self.size = input[1]
    self.format = input[2]

    self.canvas = canvas.Canvas(self.size, self.size, self.format)
