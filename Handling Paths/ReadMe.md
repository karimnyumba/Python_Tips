# Handling Paths in Python

This one is a life saver. standing for raw string, r in front of the string quotes ensure that file paths don’t get confused between Python and system settings.
 in some cases you might need to use double back slashes instead of forward slashes. This is because different systems use different path structures. When working with a script that communicates with Windows OS for example, you’ll need to use “\\“.

Just type `r'[file path]'`, replacing [file path] with the desired file path, Whenever you’re typing paths in your code, just by including that r in front of the quotes you can avoid lots of errors that might occur due to conflicts and confusions regarding path symbols like: /, //, \ . This problem occurs more often than you’d imagine and it can be very frustrating to troubleshoot. Just use r in front and path problems no more!
