# Python Debug Demo

Common Python script errors found in real 
projects — each with root cause analysis 
and the correct fix applied.

---

## Bugs Fixed

### Bug 1 — SyntaxError: Missing Colon
**Error:** SyntaxError: invalid syntax  
**Cause:** Python requires a colon at the end  
of def, if, for, while, and class statements  
**Fix:** Added colon after function definition

### Bug 2 — IndentationError
**Error:** IndentationError: unexpected indent  
**Cause:** Python uses indentation to define  
code blocks — mixing spaces causes errors  
**Fix:** Consistent 4-space indentation  
inside function body

### Bug 3 — TypeError: String + Integer
**Error:** TypeError: can only concatenate  
str (not "int") to str  
**Cause:** Python won't implicitly convert  
integers to strings like some languages  
**Fix:** str() conversion or f-string syntax

### Bug 4 — Empty List Division
**Symptom:** ZeroDivisionError on empty input  
**Cause:** No guard against empty list,  
dividing by zero length  
**Fix:** Added length check before division

### Bug 5 — IndexError: List Out of Range
**Error:** IndexError: list index out of range  
**Cause:** Accessing index 3 on a 3-item list  
(valid indexes are 0, 1, 2)  
**Fix:** Length check + try/except handling

### Bug 6 — NameError: Undefined Variable
**Error:** NameError: name 'total_items'  
is not defined  
**Cause:** Variable defined as item_count  
but called as total_items  
**Fix:** Consistent variable naming throughout

### Bug 7 — Input Type Comparison Fails
**Symptom:** Condition never true even  
with correct input  
**Cause:** input() returns string,  
comparing "10" == 10 is always False  
**Fix:** int() conversion before comparison

### Bug 8 — File Not Closed After Reading
**Symptom:** Memory leak, potential  
file corruption  
**Cause:** open() without close() or  
context manager  
**Fix:** with statement handles  
automatic closing

---

## Skills Demonstrated
- Python syntax debugging
- Type handling and conversion
- Exception handling with try/except
- File handling best practices
- Defensive programming patterns

---

## Contact
Available for Python debugging on  
Fiverr and Upwork.
