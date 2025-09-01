import sys

sys.path.append('/Users/lottejaspers/Documents/GitHub/computational-thinking-week-group-Brabus')

from lotte_jaspers import who_am_i as lotte_who
from Asjfaaq import who_am_i as asjfaaq_who

def introduce_team():
    print("This is Team Brabus. We are:")
    print(lotte_who())
    print(asjfaaq_who())

if __name__ == "__main__":
    introduce_team()
