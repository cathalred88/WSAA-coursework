# read a text file from filesystem and print its content to the console
# Author Cathal Redmond Date 14 April 2026


# set the file path for the target file in the same repowsitory as this python file. The target file is a text file called testfile.txt which contains some text that we want to read and print to the console.

import os
print("Current working directory:", os.getcwd())

target_file = r"C:\Users\catha\Documents\ATU\WSAA-coursework\story.txt"

# open the target file and print its content to the console
with open(target_file, 'r', encoding='utf-8') as file:
    content = file.read()


print("Content of the file:")
print(content)
