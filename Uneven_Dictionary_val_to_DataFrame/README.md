## How to Convert a Dictionary with Different lengths of values into a Pandas DataFrame


So, when trying to convert a dictionary with values as lists of unequal lenghts , e.g:
```sh
dict_data = {
    'bio_sample_': ['a','b','c'], 
    'concentration' : [1,2]
            }
```
If you run :
```sh
df=pd.DataFrame(dict_data)
```
You will get an error because the length of the list in the value is not equal for all keys.
To transform this dictionary to a pandas dataframe, you can run the function in **main.py**