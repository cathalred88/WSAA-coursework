## Assignment 4 - name replacer python file 
# Author Cathal Redmond Date 14 April 2026

#imports 
import requests


#set the target file in which to replace the name
target_file = "testfile.txt"
# set the name to be replaced and the new name
name_to_replace = "John Doe"
new_name = "Jane Smith"
# read the content of the target file
with open(target_file, 'r') as file:
    content = file.read()   
# replace the name in the content
updated_content = content.replace(name_to_replace, new_name)
# write the updated content back to the target file
with open(target_file, 'w') as file:
    file.write(updated_content)
print(f"Replaced '{name_to_replace}' with '{new_name}' in {target_file}.")

# commit the change and push this file to github repositry using git commands in the terminal:
# git add assignment04-github.py
# git commit -m "Updated name replacer script with new names"
# git push origin main
