# GardenSnake
## A parser generator demonstration program.

**This implements a modified version of a subset of Python:**

*   only 'def', 'return' and 'if' statements
*   'if' only has 'then' clause (no elif nor else)
*   single-quoted strings only, content in raw format
*   numbers are decimal.Decimal instances (not integers or floats)
*   no print statment; use the built-in 'print' function
*   only < > == + - / * implemented (and unary + -)
*   assignment and tuple assignment work
*   no generators of any sort
*   no ... well, no quite a lot

### Why?

I'm thinking about a new indentation-based configuration language for a project and wanted to figure out how to do it.  Once I got that working I needed a way to test it out.  My original AST was dumb so I decided to target Python's AST and compile it into Python code.  Plus, it's pretty cool that it only took a day or so from sitting down with Ply to having working code.

This uses David Beazley's Ply from http://www.dabeaz.com/ply/

This work is hereby released into the Public Domain. To view a copy of the public domain dedication, visit http://creativecommons.org/licenses/publicdomain/ or send a letter to Creative Commons, 543 Howard Street, 5th Floor, San Francisco, California, 94105, USA.

Portions of this work are derived from Python's Grammar definition and may be covered under the Python copyright and license

> Andrew Dalke / Dalke Scientific Software, LLC
> 30 August 2006 / Cape Town, South Africa

**Changelog:**

+   30 August - added link to CC license; removed the "swapcase" encoding
