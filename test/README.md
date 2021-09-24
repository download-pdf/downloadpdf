# **Test**

## **Usage**
### **unittest**
`python -m unittest downloadpdf_test`: Run all the test cases/Classes

`python -m unittest downloadpdf_test.TestURL`: Run specific test Class

`python -m unittest downloadpdf_test.TestDownloadPDF.test_shouldDownloadFromAthena`: Run specific test case

`python -m unittest test.downloadpdf_test.TestDownloadPDF.test_shouldDownloadFromWTF`

### **pytest**
`pytest` framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

`pytest -vv downloadpdf_test.py --maxfail=1 --html=testcov-html/downloadpdf_testdata.html  --no-cov-on-fail --cov=$(pwd) --cov-report=html` --html generates test cases status, --cov-report=html generates code coverage reports.

`pytest -vv test --maxfail=1 --no-cov-on-fail --cov=$(pwd)`

`pytest -vv test/downloadpdf_test.py --maxfail=1 --no-cov-on-fail --cov=$(pwd)`

### **flake8**
`flake8` glues together pycodestyle, pyflakes, mccabe, and third-party plugins to check the style and quality of some python code.

`flake8 . --count --max-complexity=3 --max-line-length=80 --statistics` Shows import issues in __init__.py files.

`flake8 . --count --select=E9,F63,F7,F82 --max-complexity=3 --max-line-length=80 --statistics` Hides issues such as import, 2 lines after import, etc..

`flake8 downloadpdf/*.py  --count --select=E9,F63,F7,F82 --max-complexity=3 --max-line-length=80 --statistics`

`flake8 main/*.py  --count --select=E9,F63,F7,F82 --max-complexity=3 --max-line-length=80 --statistic`

`flake8 util/*.py  --count --select=E9,F63,F7,F82 --max-complexity=3 --max-line-length=80 --statistics`

`flake8 test/*.py  --count --select=E9,F63,F7,F82 --max-complexity=3 --max-line-length=80 --statistics`

C McCabe Complexity like `C901 'downloadPDF' is too complex (3)` or `flake8 . --count --select C --max-complexity=0`

E Error like `E302 expected 2 blank lines, found 1`

W Warning like `W291 trailing whitespace` or `E501 line too long (110 > 80 characters)`

F `./util/__init__.py:3:1: F401 'util.log.initilaizeLog' imported but unused`

### **autopep8**
`autopep8` automatically formats Python code to conform to the PEP 8 style guide

`autopep8 --in-place --aggressive --aggressive */*.py` Removes lint errors

autopep8 fixes the following issues reported by pycodestyle and more:
- E101 - Reindent all lines.
- E11  - Fix indentation.
- E121 - Fix indentation to be a multiple of four.
- E122 - Add absent indentation for hanging indentation.
- E123 - Align closing bracket to match opening bracket.
- E124 - Align closing bracket to match visual indentation.
- E125 - Indent to distinguish line from next logical line.
- E126 - Fix over-indented hanging indentation.
- E127 - Fix visual indentation.
- E128 - Fix visual indentation.
- E129 - Fix visual indentation.
- E131 - Fix hanging indent for unaligned continuation line.
- E133 - Fix missing indentation for closing bracket.
- E20  - Remove extraneous whitespace.
- E211 - Remove extraneous whitespace.
- E22  - Fix extraneous whitespace around keywords.
- E224 - Remove extraneous whitespace around operator.
- E225 - Fix missing whitespace around operator.
- E226 - Fix missing whitespace around arithmetic operator.
- E227 - Fix missing whitespace around bitwise/shift operator.
- E228 - Fix missing whitespace around modulo operator.
- E231 - Add missing whitespace.
- E241 - Fix extraneous whitespace around keywords.
- E242 - Remove extraneous whitespace around operator.
- E251 - Remove whitespace around parameter '=' sign.
- E252 - Missing whitespace around parameter equals.
- E26  - Fix spacing after comment hash for inline comments.
- E265 - Fix spacing after comment hash for block comments.
- E266 - Fix too many leading '#' for block comments.
- E27  - Fix extraneous whitespace around keywords.
- E301 - Add missing blank line.
- E302 - Add missing 2 blank lines.
- E303 - Remove extra blank lines.
- E304 - Remove blank line following function decorator.
- E305 - Expected 2 blank lines after end of function or class.
- E306 - Expected 1 blank line before a nested definition.
- E401 - Put imports on separate lines.
- E402 - Fix module level import not at top of file
- E501 - Try to make lines fit within --max-line-length characters.
- E502 - Remove extraneous escape of newline.
- E701 - Put colon-separated compound statement on separate lines.
- E70  - Put semicolon-separated compound statement on separate lines.
- E711 - Fix comparison with None.
- E712 - Fix comparison with boolean.
- E713 - Use 'not in' for test for membership.
- E714 - Use 'is not' test for object identity.
- E721 - Use "isinstance()" instead of comparing types directly.
- E722 - Fix bare except.
- E731 - Use a def when use do not assign a lambda expression.
- W291 - Remove trailing whitespace.
- W292 - Add a single newline at the end of the file.
- W293 - Remove trailing whitespace on blank line.
- W391 - Remove trailing blank lines.
- W503 - Fix line break before binary operator.
- W504 - Fix line break after binary operator.
- W601 - Use "in" rather than "has_key()".
- W602 - Fix deprecated form of raising exception.
- W603 - Use "!=" instead of "<>"
- W604 - Use "repr()" instead of backticks.
- W605 - Fix invalid escape sequence 'x'.
- W690 - Fix various deprecated code (via lib2to3).

## **Resource**
- https://flake8.pycqa.org
- https://github.com/hhatto/autopep8
- https://pytest.org
- https://docs.python.org/3/library/unittest.html