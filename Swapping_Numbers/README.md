# Python Trick: Swapping Two Numbers

## Description

Swapping the values of two variables is a common task in programming, but it can be cumbersome to do it without a temporary variable. However, in Python, there is a simple trick that allows you to swap the values of two variables in a single line of code, without needing a temporary variable.

## Trick

The trick consists of using tuple unpacking to assign the values of two variables to each other. Here's an example:

```python3
a = 5
b = 10

a, b = b, a
```


After executing this code, the values of `a` and `b` will be swapped, so `a` will be equal to `10`, and `b` will be equal to `5`.

## Explanation

When you write `a, b = b, a`, Python creates a tuple `(b, a)` with the values of `b` and `a` in that order. Then, Python unpacks the tuple and assigns the first value, `b`, to the first variable, `a`, and the second value, `a`, to the second variable, `b`. This effectively swaps the values of the two variables.

## Conclusion

Swapping the values of two variables in Python is easy and elegant with this simple trick. You don't need to use a temporary variable, and you can do it in a single line of code. Use this trick to make your code more readable and efficient!

