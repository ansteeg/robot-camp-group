import os

def our_group():
    print("This is Team 'Any Name Suggestions?'. We are:")
    for file in os.listdir():
        if file.endswith('.py') and file != 'git_exercise.py':
            module_name = os.path.splitext(file)[0]
            module = __import__(module_name)
            person = getattr(module, module_name)()
            print(person)

our_group()
