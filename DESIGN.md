# DESIGN

## Modules

* [Master Control](#mastercontrol)
* [Input](#input)
* [Shape](#shape)
* [Canvas](#canvas)
* [Output](#output)

## Module Details

DataStructures: 
input: format, shape, size

<a name="mastercontrol"></a>
#### Master Control
* Everything runs in here, takes args from CLI framework
* Not sure exactly how commandlinetool frameworks work so this works as the layer in between framework and everything else

<a name="input"></a>
#### Input (REST api) 
* Master Control calls input with commandline args
* Reads from commandline (or rest request)
* Parses
* Returns input(format, shape, size)

<a name="shape"></a>
#### Shape (Spiral, Rectangle, Square, etc)
* Takes input(format, shape, size)
* Creates appropriate **shape** with **size**
* Creates canvas in proper **format** and **size**
* Uses shapes draw method which uses Canvas's drawLine method

<a name="canvas"></a>
#### Canvas (Ascii, SVG)
* Width, height for size
* Exposes drawLine(x,y) that writes a '+' at x, then '-' until it reaches y where it prints another '+'. Draw
* Exposes a print method

<a name="output"></a>
#### Output (Commandline, SVG file)
* Takes canvas object
* Prints it to commandline

## Notes
* Input, Shape, Canvas, Output can be made into abstract classes that are inherited from. ie, Shape is extended by Spiral, Rectangele, Square, etc

* Considersation: if we're using Master Control to hide what's inside from commandline, then perhaps output should return something rather than print to commandline?

* CommandLineTool Frameworks for Python, [link](http://nvie.com/posts/writing-a-cli-in-python-in-under-60-seconds/): pipsi

* Python REST (Web Service) Frameworks, [Stackoverflow link](http://stackoverflow.com/questions/713847/recommendations-of-python-rest-web-services-framework): Flask, [Cherrypy](http://blaag.haard.se/Simple-REST-ful---ish--exposure-of-Python-APIs/)
