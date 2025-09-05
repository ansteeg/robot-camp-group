from challenge_day1 import leopoldo_gerrit, Mies_Haenen

def print_team_members():
    team_name = "uiiai"  # You can change this to your actual team name
    print(f"This is Team {team_name}. We are:")
    print(f"- {leopoldo_gerrit.get_name()}")
    print(f"- {Mies_Haenen.get_name()}")
    print(f"- {nadz.get_name()}")

if __name__ == "__main__":
    print_team_members()
