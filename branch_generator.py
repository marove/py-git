from git import Repo
from googletrans import Translator

directory = input("Enter directory (leave empty and press enter if not desired): ")
if directory:
    directory = directory + "/"

pbi_number = input("Enter pbi number: ").strip()
branch_name = input("Enter branch name: ").strip().lower()

translator = Translator()
translated_branch = translator.translate(branch_name, dest='en').text.capitalize().replace(" ", "_")

final_branch_name = directory + pbi_number + "-" + translated_branch

repo = Repo("./")
repo.git.checkout("develop")
repo.git.checkout("-b", final_branch_name)

print("Branch created: " + final_branch_name)
