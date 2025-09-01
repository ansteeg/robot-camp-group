from lotte_jaspers import who_am_i as lotte_who
from Asjfaaq import who_am_i as asjfaaq_who
from Juriaan_Rösingh import who_am_i as juriaan_who

def introduce_team():
    print("This is Team Brabus. We are:")
    print(lotte_who())
    print(asjfaaq_who())
    print(juriaan_who())

if __name__ == "__main__":
    introduce_team()
