import bennis_file
import Lolo_file
import marfa_file
import marie_file
import paz_file
import younes_file

def print_team_story():
    # Team header
    print("This is Team " + TEAM_NAME + ". We are:")
    print("-", bennis_file.name())
    print("-", Lolo_file.name())
    print("-", marfa_file.name())
    print("-", marie_file.name())
    print("-", paz_file.name())
    print("-", younes_file.name())

    # The story (acts 1–3), rotating authors so nobody follows themselves
    print(bennis_file.act1())
    print(Lolo_file.act1())
    print(marfa_file.act1())
    print(marie_file.act1())
    print(paz_file.act1())
    print(younes_file.act1())

    print(Lolo_file.act2())
    print(bennis_file.act2())
    print(marie_file.act2())
    print(younes_file.act2())
    print(paz_file.act2())
    print(marfa_file.act2())

    print(marie_file.act3())
    print(bennis_file.act3())
    print(younes_file.act3())
    print(Lolo_file.act3())
    print(marfa_file.act3())
    print(paz_file.act3())

if __name__ == "__main__":
    TEAM_NAME = "Pinky Robots"
    print_team_story()
