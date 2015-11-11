#!/usr/bin/env python
import pdb

class Canvas():
  # Draws '+' at (x,y) and (x1,y1)
  # Draws '-' or '|' between (x,y) and (x1,y1)
  def drawLine(self, x, y, x1, y1):

    self.validateInput(x, y, x1, y1)

    # reversing coordinates, range() can't go backwards    
    if (x > x1):
      temp = x
      x = x1
      x1 = temp

    if (y > y1):
      temp = y
      y = y1
      y1 = temp

    self.grid[x][y] = '+'
    self.grid[x1][y1] = '+'

    if (x == x1): # vertical line
      for j in range(y+1,y1):
        self.grid[x][j] = '|'
    elif (y == y1): # horizontal line
      for i in range(x+1,x1):
        self.grid[i][y] = '-'

  def validateInput(self, x, y, x1, y1):  
    flag = x != x1 and y != y1
    flag |= x < 0 or x > self.width
    flag |= x1 < 0 or x1 > self.width
    flag |= y < 0 or y > self.height
    flag |= y1 < 0 or y1 > self.height
    if flag:
      raise ValueError('Invalid Coordinates')

  # Prints output to commandline
  def output(self):
    string = ''
    for y in range(self.height):
      for x in range(self.width):
        string += str(self.grid[x][y])
      string += '\n'
    return string

  def __init__(self, width, height, format):
    self.width = width
    self.height = height
    self.format = format
    self.grid = []
    for i in range(self.width):
      self.grid.append([' '] * self.height)
