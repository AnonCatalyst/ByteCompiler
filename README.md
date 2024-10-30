# ByteCompiler

**ByteCompiler** is a simple tool designed to convert various file formats into bytecode. It provides a user-friendly interface that makes it easy to process supported files while handling errors gracefully.

## Features
- ✔ Simple tool for converting file formats to bytecode
- ✔ Supports `.py`, `.scr`, `.txt`, `.html`, `.js`, `.json`, `.csv`, and `.xml` files
- ✔ User-friendly interface for easy use
- ✔ Handles errors with clear messages
- ✔ Provides file type descriptions

## Install & Run

1. `git clone https://github.com/AnonCatalyst/ByteCompiler`
2. `cd ByteCompiler`
3. `pip install -r requirements.txt --break-system-packages`
 - (alternative) > pip install colorama --break-system-packages
4. `python3 bytecompiler.py`

## Display Example 

   ByteCompiler   
   ------------   
```
Features: 
✔ Simple tool for converting file formats to bytecode
✔ Supports .py, .scr, .txt, .html, .js, .json, .csv, and .xml files

Enter file names separated by commas: 
(supported formats: .py, .scr, .txt, .html, .js, .json, .csv, .xml): test.py   

Processing test.py (Python Script)...

Summary of Results:
Compiled test.py to bytecode: test.pyc
```
