#!/usr/bin/env python
import pdb
from submodules import input
from submodules import canvas
from submodules import shape
from submodules import output

if __name__ == '__main__':
  input = input.parseInput() # returns input tuple: (shape, size, format)

  # no case statements in python, could use a factory here
  if (input[0] == 'spiral'):
    shape = shape.Spiral(input)
  elif (input[0] == 'square'):
    shape = shape.Square(input)

  canvas = shape.draw()
  
  output = output.Output(canvas)
  output.put()

# if __name__ == '__main__':
#   (input_shape,input_size,input_format) = input.parseInput() # returns input tuple: (shape, size, format)

#   #no case statements in python, using if/elif/else
#   if (input_shape == 'spiral'):
#     shape = shape.Spiral(input_shape,input_size,input_format)
#   elif (input_shape == 'square'):
#     shape = shape.Square(input_shape,input_size,input_format)

#   canvas = shape.draw()
  
#   output = output.Output(canvas)
#   output.put()