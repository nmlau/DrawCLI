#!/usr/bin/env python
import pdb

from submodules import canvas

class Output():
  def __init__(self, canvas):
    self.canvas = canvas
  def put(self):
    stdout = self.canvas.output();
    print stdout
