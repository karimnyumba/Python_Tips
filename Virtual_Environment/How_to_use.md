# How to Use the `main.py` Script to Create a Virtual Environment

1. Open a terminal window and navigate to the directory where the `main.py` script is located.

2. Run the following command to create a new virtual environment:
```
python3 main.py
```

This will create a new virtual environment named `myenv` in the same directory as the `main.py` script.

3. After the virtual environment is created, you can activate it by running the following command:

```
source myenv/bin/activate
```


This will activate the virtual environment, and any packages you install or scripts you run will use the Python version and packages installed in the virtual environment.

4. When you're done working in the virtual environment, you can deactivate it by running the following command:

```
deactivate
```


This will deactivate the virtual environment and return you to your system's default Python environment.

Creating and using virtual environments is a good practice to ensure that your project dependencies are isolated and your project runs consistently across different systems. The `main.py` script provides a convenient way to create a virtual environment in Python using the built-in `venv` module.

