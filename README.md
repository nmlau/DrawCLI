Takes input: Shape, Size, Format

Example: python draw -s spiral -t 11 -f ascii
Prints:


==================== Notes ====================

Option Parser is fine for now, but to get closer to what they're asking for I should bring in ArgParse
https://docs.python.org/2/library/argparse.html

Can do imports better, might not want to use input since it's a keyword

OptParse and Making CLI tool in Python, http://goo.gl/d65at4
-I just took the optparse section in ran with it, read this later for more help with CLI tool if I need it

No switch/case in python, will use elifs for now

Input validation could be given more specific errors

Using Pdb for debugger

==================== Todo ====================

input validation should ignore cpas
.gitignore *.pyc files

==================== Learned ====================

False not false
int() and str() to cast
print('.'), # this will still print a space, but not a newline

SO link, http://goo.gl/qlnvsi
If by "array" you actually mean a Python list, you can use
a = [0] * 10
or
a = [None] * 10