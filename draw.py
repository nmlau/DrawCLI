#!/usr/bin/env python
from submodules import input
from submodules import shape
from submodules import canvas
from submodules import output

if __name__ == '__main__':
  input = input.parseInput() # returns input tuple: (shape, size, format)
  print input

  #no case statements in python, using if/elif/else
  if (input[0] == 'spiral'):
    shape = shape.Spiral(input)
  # elif (input[0] == 'square'):
  #   shape = shape.Square(input)

  canvas = shape.draw()
  canvas.output() # output(canvas)