#!/usr/bin/env python
from submodules import input
from submodules import shape

if __name__ == '__main__':
  input = input.parseInput() # returns (shape, size, format)
  print input

  if (input[0] == 'spiral'):
    shape = shape.Spiral(input[1])
    shape.name()
  else:
    print "Invalid Shape: " + input[0]
    # shape = shape.Shape(input[1])
    # shape.name()