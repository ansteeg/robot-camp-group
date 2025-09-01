# git_exercise.py

import bennis_file
import Lolo_file
import marfa_file
import marie_file
import paz_file
import younes_file

def print_team_roster():
    print("This is Team Pinky Robots. We are:")

    # Call each teammate's function
    print("-", bennis_file.name())
    print("-", Lolo_file.get_my_name())
    print("-", marfa_file.name())
    print("-", marie_file.name())
    print("-", paz_file.name())
    print("-", younes_file.name())

if __name__ == "__main__":
    print_team_roster()
