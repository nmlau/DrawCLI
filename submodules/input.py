#!/usr/bin/env python
import optparse
import argparse

def parseInput():
  optionParser = optparse.OptionParser()
  optionParser.add_option('--shape', '-s', default="spiral")
  optionParser.add_option('--size', '-t', default="0")
  optionParser.add_option('--format', '-f', default="ascii")
  options, arguments = optionParser.parse_args()
  print '%s %s %s' % (options.shape, options.size, options.format)
  return (options.shape, options.size, options.format)