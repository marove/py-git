from git import Repo
from googletrans import Translator


def enter_branch_type():
    return input("Enter branch type (feature/fix/hotfix): ")


def enter_pbi_number():
    pbi = input("Enter PBI number: ")
    pbi_without_spaces = pbi.strip()
    return pbi_without_spaces


def enter_task_number():
    task_number_entered = input("Enter task number (leave empty if there is not task): ")
    task_number_entered_without_spaces = task_number_entered.strip()
    if task_number_entered_without_spaces:
        task_number_entered_without_spaces = "/" + task_number_entered_without_spaces
    return task_number_entered_without_spaces


def enter_branch_name():
    branch_name_entered = input("Enter branch name: ")
    branch_name_entered_without_spaces_and_lowercase = branch_name_entered.strip().lower()
    return branch_name_entered_without_spaces_and_lowercase


def translate_branch_name(branch):
    translator = Translator()
    translated_branch_name = translator.translate(branch, dest='en').text
    formatted_translated_branch_name = translated_branch_name.capitalize().replace(" ", "_")
    return formatted_translated_branch_name


def compound_final_branch_name(branch_type, pbi_number, task_number, translated_branch_name):
    return branch_type + "/" + pbi_number + task_number + "-" + translated_branch_name


def create_git_branch_from_develop():
    repo = Repo("./")
    repo.git.checkout("develop")
    repo.git.checkout("-b", final_branch_name)


def create_branch(branch_name):
    confirmation_response = input("The branch name will be " + branch_name + ". Is it ok? (y/n): ").lower()
    if confirmation_response == 'y':
        create_git_branch_from_develop()
        print("Branch created: " + branch_name)
    else:
        print("Cancelled")


branch_type_input = enter_branch_type()
pbi_number_input = enter_pbi_number()
task_number_input = enter_task_number()
branch_name_input = enter_branch_name()
translated_branch_input = translate_branch_name(branch_name_input)

final_branch_name = compound_final_branch_name(branch_type_input, pbi_number_input, task_number_input,
                                               translated_branch_input)
create_branch(final_branch_name)
