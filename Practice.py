import os

dire = "/home/gaurabs/Downloads/cccccc"

for file in os.listdir(dire):
    a = str(file)
    b=file[file.index("lab"):file.index(".c")].upper()
    os.rename(dire+"/"+file, dire+"/"+b+".c")