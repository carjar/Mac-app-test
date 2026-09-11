# -*- coding: utf-8 -*-
"""
Testing .app packaging
"""
import sys
import os

# If the file is in a .app or .exe bundle (sys.frozen = true), manually set the dir
if getattr(sys, 'frozen', False):
    app_dir = os.path.dirname(sys.executable)
else:
    app_dir = os.path.dirname(os.path.abspath(__file__))


# Setting open() function path
file_path = os.path.join(app_dir, "test_file.txt")

# Open the file in write mode
with open(file_path, 'w') as file:
    # Write content to the file
    file.write("Test if .app is functioning.")
    
print(f"File '{file_path}' created successfully.")