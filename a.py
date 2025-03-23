import os

def list_directory(root_dir):
    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, "").count(os.sep)
        indent = " " * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = " " * 4 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")

root_directory = "/home/ankit/Development/Heasarc/nicer/Cas_A/output"
list_directory(root_directory)
