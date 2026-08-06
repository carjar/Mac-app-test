# -*- coding: utf-8 -*-
"""
Testing .app packaging
"""

# Using open() function
file_path = "test_file.txt"

# Open the file in write mode
with open(file_path, 'w') as file:
    # Write content to the file
    file.write("Test if .app is functioning.")
    
print(f"File '{file_path}' created successfully.")