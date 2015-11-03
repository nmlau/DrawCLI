#!/usr/bin/env python
import pdb

class Canvas():

  # Draws '+' at (x,y) and (x1,y1)
  # Draws '-' or '|' between (x,y) and (x1,y1)
  # Or shades in everything between (x,y) and (x1,y1) if (x-x1 != 0 and y-y1 != 0)
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

    # Need to track direction so that canvas knows whether to draw '-' or '|'
    direction = 'vertical'
    if (yStart - yEnd == 0):
      direction = 'horizontal'

    for i in range(xStart,xEnd+1):
      for j in range(yStart,yEnd+1):
        if (i == x and j == y):
          self.grid[i][j] = '+'
        elif (i == x1 and j == y1):
          self.grid[i][j] = '+'
        else:
          if (direction == 'horizontal'):
            self.grid[i][j] = '-'
          elif (direction == 'vertical'):
            self.grid[i][j] = '|'
    return 0

  def output(self):
    for x in range(self.width):
      string = ''
      for y in range(self.height):
        if (str(self.grid[y][x]) == '0'):
          string += ' '
        else:
          string += str(self.grid[y][x])
        # print(self.grid[y][x]), 
      print(string)
    return 0

  def __init__(self, height, width, format):
    self.height = int(height)
    self.width = int(width)
    self.format = format
    self.grid = []
    for i in range(self.height):
      temp = [0] * self.width
      self.grid.append(temp)
