#!/usr/bin/python3
"""Define a text file-reading function."""

def read_file(filename=""):
   """ Function that reads from a file

   Args:
      filename: filename
   Raises
      Exception: when the file can be opened

   """

   with open(filename, encoding="utf-8") as f:
      print(f.read(), end="")
