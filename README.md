# calpy

Calculator in Python using tkinter for GUI.

Emulates an old-school handheld calculator, or the standard Microsoft calculator app.

## Files

* `calc.py` is our GUI
* `calc_func.py` contains our calculation functions
* `test_calc_func.py` contains unit tests for `calc_func.py`

## Calculation Functions

`calculate(expr_list)` accepts a list of strings containing numbers and operators. Return the result of calculating the expression.

### `expr_list` examples

Consider the following key presses (from left to right):

#### Display

```
7  +  3  /  2  x  3  =
^  ^  ^  ^  ^  ^  ^  ^
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  Entry "15", Label "5 x 3 ="
|  |  |  |  |  |  Entry "3", Label "5 x"
|  |  |  |  |  Entry "5", Label "5 x"
|  |  |  |  Entry "2", Label "10 /"
|  |  |  Entry "10", Label "10 /"
|  |  Entry "3", Label "7 +"
|  Entry "7", Label "7 +"
Entry "7", Label ""
```

#### Calculation Steps

```
   7
+  3
----
  10
/  2
----
   5
x  3
====
  15
```
