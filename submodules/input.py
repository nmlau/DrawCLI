#!/usr/bin/env python
import pdb

import optparse
import argparse

def parseInput():
  input = parseArgs() # returns (shape, size, format)
  isValidInput = validateInput(input)
  return input

# def parseOpts():
#   optionParser = optparse.OptionParser()
#   optionParser.add_option('--shape', '-s', default="spiral")
#   optionParser.add_option('--size', '-t', default="0")
#   optionParser.add_option('--format', '-f', default="ascii")
#   options, arguments = optionParser.parse_args()

#   # pdb.set_trace()
#   #changes to lower so we can ignore caps (is this the best place to do this?)
#   # print '%s %s %s' % (options.shape, options.size, options.format)
#   return (options.shape.lower(), options.size.lower(), options.format.lower())

def parseArgs():
  argParser = argparse.ArgumentParser()
  argParser.add_argument("shape", help="choose what shape you want drawn")
  argParser.add_argument("size", help="choose the size of the shape")
  argParser.add_argument("-f", "--format", help="choose the format", default="ascii")

  arguments = argParser.parse_args()

  # Changes to lower so we can ignore caps (is this the best place to do this?)
  # print '%s %s %s' % (arguments.shape.lower(), arguments.size.lower(), arguments.format.lower())
  return (arguments.shape.lower(), arguments.size.lower(), arguments.format.lower())
  
def validateInput(input):
  # takes tuple (shape, size, format)
  shape = input[0]
  size = input[1]
  format = input[2]

  inputIsValid = True
  # Validate size
  if (int(size) < 1):
    print "Invalid Size: " + size
    inputIsValid = False
  
  # Validate shape
  if (shape != 'spiral'): # || shape != Rectangle || shape != etc
    print "Invalid Shape: " + shape
    inputIsValid = False

  # Validate format
  if (format != 'ascii'): # || format != nvg || format != etc
    print "Invalid Format: " + format
    inputIsValid = False

  # Check Flag
  if (inputIsValid == False):
    raise ValueError("Invalid Input: " + str(input))

  return inputIsValid
