#!/usr/bin/env python

class Shape():
  def draw(self):
    return 0
  def name(self):
    print ("Shape")
  def __init__(self, size):
    self.size = size

class Spiral(Shape):
  def draw(self):
    return 0
  def name(self):
    print ("Spiral, of size: " + self.size)
  def __init__(self, size):
    self.size = size

