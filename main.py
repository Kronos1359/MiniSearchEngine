import os

files = os.listdir(path="documents")
for file in files:
    if file.endswith(".txt"):
        print(file)