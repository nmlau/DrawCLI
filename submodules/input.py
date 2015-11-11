#!/usr/bin/env python
import argparse

def parseInput():
  input = parseArgs() # returns (shape, size, format)
  validateInput(input)
  return input

def parseArgs():
  argParser = argparse.ArgumentParser()
  argParser.add_argument("shape", help="choose what shape you want drawn")
  argParser.add_argument("size", help="choose the size of the shape", type=int)
  argParser.add_argument("-f", "--format", help="choose the format", default="ascii")
  arguments = argParser.parse_args()

  # Changes to lower so we can ignore caps (is this the best place to do this?)
  return (arguments.shape.lower(), arguments.size, arguments.format.lower())
  
def validateInput(input):
  # takes tuple (shape, size, format)
  shape = input[0]
  size = input[1]
  format = input[2]

  # Validate shape
  if (shape != 'spiral' and shape != 'square'): # || shape != Rectangle || shape != etc
    raise ValueError("Invalid Shape: " + shape)
  
  # Validate size
  if (size < 1):
    raise ValueError("Invalid Size: " + str(size))

  # Validate format
  if (format != 'ascii'): # || format != nvg || format != etc
    raise ValueError("Invalid Format: " + format)
