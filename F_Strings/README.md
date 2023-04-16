# Formtting Strings with f-strings
This python tip demonstrates how to use f-strings to format strings in various ways.

## Code Example
Consider the following code snippet:

```
text ='EPIC'
print(f'{text}')
print(f'{text:#<20}')
print(f'{text:_>20}')
print(f'{text:.^20}')
```

## Output
The code of the code snippet above would be as follows:

```
EPIC
EPIC#################
_________________EPIC
.......EPIC.........
```

## Explanation
In the code snippet, the variable `text` is assigned the value "EPIC". The four print statements use f-strings to format `text` in various ways.

- The first print statement simply prints the value of `text` as is.
- The second print statement pads `text` with `#` characters on the right, until the total width of the resulting string is 20 characters.
- The third print statement pads `text` with `_` characters on the left, until the total width of the resulting string is 20 characters.
- The fourth print statement pads `text` with `.` characters on both sides, until the total width of the resulting string is 20 characters.        

## Conclusion
By using f-strings and formatting specifiers, you can easily format strings in Python to suit your needs. In this example, we showed how to pad a string with characters, but there are many other formatting options available with f-strings.              
