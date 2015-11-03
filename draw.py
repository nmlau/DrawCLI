#!/usr/bin/env python
from submodules import input
from submodules import shape
from submodules import canvas
from submodules import output

if __name__ == '__main__':
  input = input.parseInput() # returns (shape, size, format)
  print input

  if (input[0] == 'spiral'):
    shape = shape.Spiral(input)
  # elif (input[0] == 'square'):
  #   shape = shape.Square(input)

  canvas = shape.draw()
  canvas.output() # output(canvas)