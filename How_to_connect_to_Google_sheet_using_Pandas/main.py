import pandas as pd

## Load data from the Google sheet directly:
sheet_id = 'abcdefghijklmnopqrstuvxxyz' # replace with your actual sheet id

sheet_name = 'bwhiz_sample_sheet' #replace with your actual sheet name

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

#load into a pandas dataframe
df = pd.read_csv(url)