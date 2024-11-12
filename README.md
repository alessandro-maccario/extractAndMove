# Create a simple ExtractAndMove and ExtractAndConvert script

## Problem Breakdown

The purpose of this script is twofold:

1. Firstly:
   1. Manually unzip a folder
   2. Extract the content of each of the folders available from the zip extraction
   3. For each file, assign the folder's name to it (where the folder's name represents the name of a student)
   4. Move those files in a "main" folder, to be easily accessible.
2. Secondly:
   1. Convert a PDF into a .md file by using PyMuPDF.
   2. This conversion will be used as input for any GPTs that will be able to convert the .md to a Latex file easier and faster than dumping the entire PDF content into one of this LLMs.

The entire application has been created by using CustomTkinter, a library built on top of Tkinter to make the UI more modern.

### References:

1. https://docs.python.org/3/library/tk.html
2. https://www.tcl.tk/man/tcl8.5/TkCmd/event.htm
