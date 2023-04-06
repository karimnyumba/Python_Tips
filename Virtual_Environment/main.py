# Creating a virtual environment in Python using venv

import os
import venv

# Set the name and location of the virtual environment
venv_name = "myenv"
venv_dir = os.path.join(os.getcwd(), venv_name)

# Create the virtual environment
venv.create(venv_dir, system_site_packages=False)

# Print the path to the virtual environment
print(f"Virtual environment created at {venv_dir}")

