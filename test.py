#!/usr/bin/env python
import pdb

import draw
from submodules import input
from submodules import shape
from submodules import canvas
from submodules import output

import unittest

class TestDraw(unittest.TestCase):

  def test_flow(self):
    sampleInput = ('spiral', '10', 'ascii')
    isValidInput = input.validateInput(sampleInput)
    self.assertEqual(isValidInput, True)

    spiral = shape.Spiral(sampleInput)
    self.assertEqual(spiral.shape, 'spiral')
    self.assertEqual(spiral.size, 10)
    self.assertEqual(spiral.format, 'ascii')

    sampleCanvas = spiral.draw()
    self.assertEqual(sampleCanvas.height, 10)
    self.assertEqual(sampleCanvas.width, 10)
    self.assertEqual(sampleCanvas.format, 'ascii')

    string = '+--------+\n|         \n| +----+  \n| |    |  \n| | ++ |  \n| |  | |  \n| +--+ |  \n|      |  \n+------+  \n          \n'
    self.assertEqual(sampleCanvas.output(), string)

  def test_input(self):
    sampleInput = ('spiral', '10', 'ascii')
    self.assertEqual(input.validateInput(sampleInput), True)

    sampleInput = ('spiral', '-5', 'ascii')
    self.assertRaises(ValueError, input.validateInput, sampleInput)

    sampleInput = ('spiral', '0', 'ascii')
    self.assertRaises(ValueError, input.validateInput, sampleInput)

    sampleInput = ('squiggly', '10', 'ascii')
    self.assertRaises(ValueError, input.validateInput, sampleInput)

    sampleInput = ('spiral', '10', 'crayon')
    self.assertRaises(ValueError, input.validateInput, sampleInput)

  def test_shape(self):
    sampleInput = ('spiral', '49', 'ascii')
    spiral = shape.Spiral(sampleInput)
    self.assertEqual(spiral.shape, 'spiral')
    self.assertEqual(spiral.size, 49)
    self.assertEqual(spiral.format, 'ascii')

  def test_canvas(self):
    sampleInput = ('spiral', '1', 'ascii')
    spiral = shape.Spiral(sampleInput)
    sampleCanvas = spiral.draw()
    string = "+\n"
    self.assertEqual(sampleCanvas.output(), string)

    sampleInput = ('spiral', '15', 'ascii')
    spiral = shape.Spiral(sampleInput)
    sampleCanvas = spiral.draw()
    string = "+-------------+\n|              \n| +---------+  \n| |         |  \n| | +-----+ |  \n| | |     | |  \n| | | +-+ | |  \n| | | + | | |  \n| | |   | | |  \n| | +---+ | |  \n| |       | |  \n| +-------+ |  \n|           |  \n+-----------+  \n               \n"
    self.assertEqual(sampleCanvas.output(), string)

    sampleInput = ('spiral', '40', 'ascii')
    spiral = shape.Spiral(sampleInput)
    sampleCanvas = spiral.draw()
    string = "+--------------------------------------+\n|                                       \n| +----------------------------------+  \n| |                                  |  \n| | +------------------------------+ |  \n| | |                              | |  \n| | | +--------------------------+ | |  \n| | | |                          | | |  \n| | | | +----------------------+ | | |  \n| | | | |                      | | | |  \n| | | | | +------------------+ | | | |  \n| | | | | |                  | | | | |  \n| | | | | | +--------------+ | | | | |  \n| | | | | | |              | | | | | |  \n| | | | | | | +----------+ | | | | | |  \n| | | | | | | |          | | | | | | |  \n| | | | | | | | +------+ | | | | | | |  \n| | | | | | | | |      | | | | | | | |  \n| | | | | | | | | +--+ | | | | | | | |  \n| | | | | | | | | |  | | | | | | | | |  \n| | | | | | | | | ++ | | | | | | | | |  \n| | | | | | | | |    | | | | | | | | |  \n| | | | | | | | +----+ | | | | | | | |  \n| | | | | | | |        | | | | | | | |  \n| | | | | | | +--------+ | | | | | | |  \n| | | | | | |            | | | | | | |  \n| | | | | | +------------+ | | | | | |  \n| | | | | |                | | | | | |  \n| | | | | +----------------+ | | | | |  \n| | | | |                    | | | | |  \n| | | | +--------------------+ | | | |  \n| | | |                        | | | |  \n| | | +------------------------+ | | |  \n| | |                            | | |  \n| | +----------------------------+ | |  \n| |                                | |  \n| +--------------------------------+ |  \n|                                    |  \n+------------------------------------+  \n                                        \n"
    self.assertEqual(sampleCanvas.output(), string)

  def test_canvas_drawLine(self):
    sampleCanvas = canvas.Canvas(5,5,'ascii')
    sampleCanvas.drawLine(0,0,4,4)
    string = '+||||\n|||||\n|||||\n|||||\n||||+\n'
    self.assertEqual(sampleCanvas.output(), string)

    sampleCanvas = canvas.Canvas(10,5,'ascii')
    sampleCanvas.drawLine(0,0,9,0)
    string = "+--------+\n          \n          \n          \n          \n"
    self.assertEqual(sampleCanvas.output(), string)

    sampleCanvas = canvas.Canvas(5,5,'ascii')
    sampleCanvas.drawLine(0,0,4,4)
    string = '+||||\n|||||\n|||||\n|||||\n||||+\n'
    self.assertEqual(sampleCanvas.output(), string)

  # Output doesn't really do anything at the moment, could test stdin/stdout though
  def test_output(self):
    self.assertEqual(True, True)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestDraw)
  unittest.TextTestRunner(verbosity=2).run(suite)
