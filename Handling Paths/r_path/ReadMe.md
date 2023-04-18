# Handling Paths in Python using raw string

When working with files in Python, it's important to handle file paths correctly to avoid conflicts between Python and system settings. One way to do this is by using raw strings with the "r" prefix.

To use raw strings, simply include the "r" prefix before the opening quote of the string that contains the file path. For example:
file_path = `r'c:/Users/Mac/Desktop/doc.txt'`

This ensures that backslashes in the file path are treated as path separators rather than escape characters, which can cause conflicts and errors.

It's worth noting that different operating systems use different path structures. For example, Windows uses backslashes as path separators, while Unix-based systems (such as macOS and Linux) use forward slashes. This means that when working with a script that communicates with different operating systems, it's important to handle path separators correctly.
