from challenge_day1 import leopoldo_gerrit, Mies_Haenen, nadz, Keitaro_Indradjit, cris, eliana

def print_team_members():
    team_name = "uiiai"
    print(f"This is Team {team_name}. We are:")
    
    # Create a list of team members' names
    team_members = [
        leopoldo_gerrit.get_name(),
        Mies_Haenen.get_name(),
        nadz.get_name(),
        Keitaro_Indradjit.get_name(),
        cris.get_name(),
        eliana.get_name()
    ]
    
    # Print each team member's name
    for member in team_members:
        print(f"- {member}")

def print_story():
    print("\n--- The Story of UIIAI ---")
    team_modules = [leopoldo_gerrit, Mies_Haenen, nadz, Keitaro_Indradjit, cris, eliana]

    # Define the acts and their corresponding functions
    acts = {
        "Act 1": "get_paragraph_act1",
        "Act 2": "get_paragraph_act2",
        "Act 3": "get_paragraph_act3"
    }

    for act_title, func_name in acts.items():
        print(f"\n--- {act_title} ---")
        for module in team_modules:
            if hasattr(module, func_name):
                # Get the paragraph from the function and print it
                paragraph = getattr(module, func_name)()
                print(paragraph + "\n")

if __name__ == "__main__":
    print_team_members()
    print_story()
