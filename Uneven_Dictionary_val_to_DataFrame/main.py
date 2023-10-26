import pandas as pd


def uneven_dict_converter(output):
    '''
    output is your uneven dictionary
    '''
    return pd.DataFrame({keys:[values] for keys,values in output.items()})