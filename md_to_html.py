import markdown
import os
import tkinter as tk
from tkinter import filedialog

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
        
        # Read the Markdown file and convert it to HTML
        with open(input_path, 'r') as input_file:
            markdown_text = input_file.read()
            html = markdown.markdown(markdown_text)
        
        # Write the HTML to the output file
        with open(output_path, 'w') as output_file:
            output_file.write(html)
    else:
        print(f'Not a Markdown file. Skipping {filename}.')
