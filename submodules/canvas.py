#!/usr/bin/env python
import pdb

class Canvas():
  # Draws '+' at (x,y) and (x1,y1)
  # Draws '-' or '|' between (x,y) and (x1,y1)
  # Or shades in everything between (x,y) and (x1,y1) if (x-x1 != 0 and y-y1 != 0)
  def drawLine(self, x, y, x1, y1):
    if (x > x1):
      temp = x
      x = x1
      x1 = temp

    if (y > y1):
      temp = y
      y = y1
      y1 = temp

    if (x == x1): # vertical line
      for j in range(y+1,y1):
        self.grid[x][j] = '|'
    elif (y == y1): # horizontal line
      for i in range(x+1,x1):
        self.grid[i][y] = '-'
    else:
      raise ValueError('Invalid Coordinates')

    self.grid[x][y] = '+'
    self.grid[x1][y1] = '+'

  # Prints output to commandline
  def output(self):
    string = ''
    for x in range(self.width):
      for y in range(self.height):
        string += str(self.grid[y][x])
      string += '\n'
    return string

  def __init__(self, height, width, format):
    self.height = height
    self.width = width
    self.format = format
    self.grid = []
    for i in range(self.height):
      self.grid.append([' '] * self.width)
