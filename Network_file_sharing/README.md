# Python HTTP Server

Python provides a simple way to create an HTTP server that serves files in the current directory and its subdirectories. The `python3 -m http.server` command allows you to start a simple HTTP server in your current working directory using Python version 3.

## Starting the Server

To start the HTTP server, navigate to the directory that contains the files you want to serve and run the following command in your terminal:

```
python3 -m http.server
```

If you are using a version of Python earlier than version 3, you can start the server using the following command:

```
python -m SimpleHTTPServer
```


By default, the server will listen on port 8000. You can then access the files in your web browser by visiting `http://localhost:8000`.

## Specifying a Custom Port

If you want to use a different port number, you can specify it by adding the port number as an argument to the command:

```
python3 -m http.server 8080
```

This will start the server on port 8080, and you can access the files by visiting `http://localhost:8080` in your web browser.

## Serving a Specific Directory

By default, the server will serve files from the current working directory. However, you can specify a different directory by adding it as an argument to the command:

```
python3 -m http.server /path/to/directory
```


This will start the server and serve files from the specified directory.

## Conclusion

In conclusion, the `python3 -m http.server` command is a simple and easy way to create an HTTP server that serves files in the current directory and its subdirectories using Python version 3. If you are using an earlier version of Python, you can start the server using the `python -m SimpleHTTPServer` command. With just a few commands, you can start serving files on your local machine and access them in your web browser.

