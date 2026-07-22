import os

files = os.listdir(path="documents")
for filename in files:
    if filename.endswith(".txt"):
        path = os.path.join("documents", filename)
        with open(path, "r") as file:
            file_content = file.read()
        print(f"----- {filename} -----")
        print(file_content)