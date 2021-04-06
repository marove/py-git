# Py-Git
A simple python tool to generate a new branch from develop in a project.

A user enters a type branch folder (release/fix/hotfix), a task code and a name and this program creates the branch formatted in a git branch style in english language.

## Instructions
1. Install the next python modules:
  `pip install googletrans==3.1.0a0`
  `pip install GitPython`

2. Copy the branch_generator.py file in the root project directory working with git.

3. Execute the python script in terminal: `python branch_generator.py`

4. Fill the CLI inputs.

5. Check the created branch in project: `git branch`
