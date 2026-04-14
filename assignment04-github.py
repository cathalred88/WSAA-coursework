## Assignment 4 - name replacer python file 
# Author Cathal Redmond Date 14 April 2026

#imports 
target_file = "story.txt"

# set the name to be replaced and the new name
name_to_replace = "Andrew"
new_name = "Cathal"

# read the content of the target file
with open(target_file, 'r', encoding='utf-8') as file:
    content = file.read()
    updated_content = content.replace(name_to_replace, new_name)

# write the updated content back to the target file
with open(target_file, 'w', encoding='utf-8') as file:
    file.write(updated_content)
print(f"Replaced '{name_to_replace}' with '{new_name}' in {target_file}.")
