#!/usr/bin/env python
import pdb

class Canvas():

  #Draws '+' at (x,y) and (x1,y1)
  #Shades in everything between x and x1, and y and y1
  def drawLine(self, x, y, x1, y1):
    # pdb.set_trace()
    if (x < x1):
      xStart = x
      xEnd = x1
    else:
      xStart = x1
      xEnd = x

    if (y < y1):
      yStart = y
      yEnd = y1
    else:
      yStart = y1
      yEnd = y

    for i in range(xStart,xEnd+1):
      for j in range(yStart,yEnd+1):
        if (i == x and j == y):
          self.grid[i][j] = '+'
        elif (i == x1 and j == y1):
          self.grid[i][j] = '+'
        else:
          self.grid[i][j] = '-'
    return 0

  def output(self):
    for x in range(self.width):
      for y in range(self.height):
        print(self.grid[y][x]),
      print
    return 0

  def __init__(self, height, width, format):
    self.height = int(height)
    self.width = int(width)
    self.format = format
    self.grid = []
    for i in range(self.height):
      temp = [0] * self.width
      self.grid.append(temp)
