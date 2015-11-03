#!/usr/bin/env python
import optparse
import argparse

def parseInput():
  input = parseOpts() # returns (shape, size, format)
  isValidInput = validateInput(input)
  return input

def parseOpts():
  optionParser = optparse.OptionParser()
  optionParser.add_option('--shape', '-s', default="spiral")
  optionParser.add_option('--size', '-t', default="0")
  optionParser.add_option('--format', '-f', default="ascii")
  options, arguments = optionParser.parse_args()
  print '%s %s %s' % (options.shape, options.size, options.format)
  return (options.shape, options.size, options.format)

def parseArgs():
  return 0
  
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
