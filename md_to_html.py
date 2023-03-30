'''
The purpose of this file is to convert all markdown files to 
html files and save them in the same directory.

When run you will be prompted to choose a directory, after that
you will be warned if any files are being overwritten (which is
a normal part of the process, if you are updating an existing
html file).
'''

import markdown
import markdown
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Open a file dialog to select the input directory
root = tk.Tk()
root.withdraw()
input_dir = filedialog.askdirectory(title='Select the input directory')

# Checks if a directory has actually been selected, exits if not
if input_dir == '':
    print("No directory selected!!")
    exit()

# Loop through each file in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is a Markdown file
    if filename.endswith('.md'):
        # Define the input and output paths
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(input_dir, filename[:-3] + '.html')

        # Check if the output file already exists
        if os.path.exists(output_path):
            # Show a system message popup
            confirm = messagebox.askokcancel("File exists!", f"{output_path} already exists. Do you want to replace it?")
            if not confirm:
                continue

        # Read the Markdown file and convert it to HTML
        with open(input_path, 'r') as input_file:
            markdown_text = input_file.read()
            html = markdown.markdown(markdown_text)

        # Write the HTML to the output file
        with open(output_path, 'w') as output_file:
            output_file.write(html)
    else:
        print(f'Not a Markdown file. Skipping {filename}.')
