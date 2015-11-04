Takes input: Shape, Size, Format

Format: python draw.py <shape> <size> -option 

Example: python draw.py spiral 10 -f ascii

Prints:
+--------+
|         
| +----+  
| |    |  
| | ++ |  
| |  | |  
| +--+ |  
|      |  
+------+  


==================== Notes ====================

Option Parser is fine for now, but to get closer to what they're asking for I should bring in ArgParse
https://docs.python.org/2/library/argparse.html

Can do imports better, might not want to use input since it's a keyword

OptParse and Making CLI tool in Python, http://goo.gl/d65at4
-I just took the optparse section in ran with it, read this later for more help with CLI tool if I need it

No switch/case in python, will use elifs for now

Input validation could be given more specific errors

Using Pdb for debugger

Would be using git branches if I were collaborating with others

This is my first time using python beyond a quick one off interview question

ArgParse has replaced the deprecated Python 2.x OptParse

Biggest bug I ran into: naming parseArg() return value test instead of input..."typeerror 'builtin_function_or_method' object has no attribute '__getitem__'"

==================== Todo ====================

add tests
comment

Done:
change to parseArgs
input validation should ignore caps
.gitignore *.pyc files
clean up output
need to print | when going vertically

==================== Learned ====================

str.lower() is faster than the alternative (strcmp?) for ignoring case

False not false
int() and str() to cast

print('.'), # this will still print a space, but not a newline
But I like this one more to get rid of space
>>> for i in xrange(20):
...     s += 'a'
... 
>>> print s
aaaaaaaaaaaaaaaaaaaa



SO link, http://goo.gl/qlnvsi
If by "array" you actually mean a Python list, you can use
a = [0] * 10
or
a = [None] * 10

==================== Problem ====================

Create a command line tool to draw spirals. Just print the output to console. They’re just ASCII characters (dash -, pipe |, and plus +).

The program should be object oriented. Currently it only draws spirals, but the tool will eventually draw more things like rectangle, triangle, etc and it will not only draw it as ASCII, it will draw as SVG and other formats too. The drawing functionalities will also be exposed via web application and REST API. Your class design should take into account those future requirements so that it’s easy to add those functionalities. Write down your design rationale on the file DESIGN.md on the root of the project directory using Markdown format.

The image below shows the output of spiral 6, spiral 11, and spiral 17 from left to right.spiral 6 can be ruby spiral.rb 6 or whatever is convenient for your programming language. Use git to version control the code as you work on it. Just zip the project directory (git repo included) and send us the zip. Follow all the best practices that you know of. No tests are needed, but bonus points if you have them.

==================== Followup ====================

Here's the feedback --

I'm not sure why REST API is needed. I'd like to know the reasoning behind that.

He can continue with the code. There's no need to use CLI framework because it's very simple, but it's up to him. The code should have tests. RSpec is preferable, but anything goes"

==================== Answers ====================

> I'm not sure why REST API is needed. I'd like to know the reasoning behind that.

> ...SVG and other formats too. The drawing functionalities will also be exposed via web application and REST API. Your class design should...