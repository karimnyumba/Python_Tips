# Handling Paths in Python

When working with files in Python, it's important to handle file paths correctly to avoid conflicts between Python and system settings. There are several ways to do so, this repo is gonna mention some feel free to add more.

## Ways

* using raw strings with the "r" prefix.
* using os library

It's worth noting that different operating systems use different path structures. For example, Windows uses backslashes as path separators, while Unix-based systems (such as macOS and Linux) use forward slashes. This means that when working with a script that communicates with different operating systems, it's important to handle path separators correctly.
