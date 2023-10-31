## This folder shows how to connect to a remote Google sheet securely using Pandas

First, you copy the URL to the Google sheet and make sure its public (i.e it's share setting is set to 'anyone with this link can open').

from the URL e.g :
```sh
https://docs.google.com/spreadsheets/d/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/edit#gid=############
```

The section between /d/ and /edit is the Google sheet Id, then also take note of the sheet name, make sure there's no spacing in the name, you can use an underscore in place of a white space.

Then follow the script in **main.py**