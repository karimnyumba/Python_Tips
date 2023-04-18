# Dictionary Merge

Here is a fantastic Python tip that will help you merge two or more dictionaries in pyhton in a very easy and efficient way. We use **notation for**kwargs-like objects (values with names like dictionaries) to merge them conveninently.

## For example as shown in the code

{**d1,**d2}
The result will be: {'A': 10, 'B': 20, 'C': 30, 'X': 100, 'Y': 200, 'Z': 300}

You do that and Python will take care of the rest.
