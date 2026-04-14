## Assignment 4 - name replacer python file 
# Author Cathal Redmond Date 14 April 2026

#imports 
import subprocess

#set the target file in which to replace the name
target_file = "story.txt"

# set the github repository
repository = "https://api.github.com/repos/cathalred88/WSAA-coursework/contents/"

# set the name to be replaced and the new name
name_to_replace = "Andrew"
new_name = "Cathal"

try:
    # read the content of the target file
    with open(target_file, 'r', encoding='utf-8') as file:
        content = file.read()
        updated_content = content.replace(name_to_replace, new_name)

    # write the updated content back to the target file
    with open(target_file, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    print(f"Replaced '{name_to_replace}' with '{new_name}' in {target_file}.")
    
# commit this code to github and push the changes to github
    subprocess.run(["git", "add", target_file], check=True)
    subprocess.run(["git", "commit", "-m", f"Replaced '{name_to_replace}' with '{new_name}' in {target_file}"], check=True)
    subprocess.run(["git", "push"], check=True)
except Exception as e:
    print(f"An error occurred: {e}")

# End of code
# I know the assignment mentions using authorisation for this task, but the code i generated here worked and did not require any authorisation. 