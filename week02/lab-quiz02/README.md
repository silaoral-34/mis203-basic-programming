# Week 02 Lab Quiz - Two-Item Purchase Quote

## Test Runs
* *Standard Test Case:* Tested with Item 1 (quantity = 2, unit price = 50), Item 2 (quantity = 1, unit price = 80), delivery fee = 20, and tax = 10%. The program calculated a subtotal of 180.00 TRY, tax of 18.00 TRY, and the expected final total of 218.00 TRY.
* *Boundary / Error Case (Stretch Task):* Tested entering letters (abc) instead of a number for the quantity input. The program stopped with the following error message:
  ValueError: invalid literal for int() with base 10: 'abc'
  * *How a later version could handle it:* A future version could use a try-except ValueError block inside a while loop (or check .isdigit()) to catch invalid inputs and prompt the user to enter a valid integer without crashing the program.

## What I Changed After Testing
* After running the initial test, I updated the output formatting using :.2f in the f-strings so that all monetary values (unit prices, line totals, subtotal, tax, delivery fee, and final total) consistently display with two decimal places.

## Why input() Must Be Converted Before Arithmetic
* In Python, the input() function always returns user input as a text string (str). If we do not convert it using int() or float() before arithmetic operations, the + operator will concatenate strings instead of adding numbers, and multiplication/division operations will fail with a TypeError.
