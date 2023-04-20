# Handling Paths in Python using os library

To handle path separators correctly, you can use the os.path module in Python. This module provides functions for working with file paths in a cross-platform way. For example:

This code uses the os.path.join() function to join the individual components of the file path using the appropriate path separator for the current operating system.

For example:
file_path = `os.path.join('c:', 'Users', 'Mac', 'Desktop', 'doc.txt')`
