def get_teamname():
    return "This is Team Zin er in. We are: \nMadeleine"

def get_name():
    """
    Returns my name as a string.
    
    Returns:
        str: The name "Madeleine"
    """
    return "Madeleine"


def act1_madeleine():
    """
    Returns Act I of the story - The Meeting Meltdown, from Madeleine.
    
    Returns:
        str: The story about the Bloom magazine board meeting.
    """
    return """The quarterly Bloom magazine board meeting began with high hopes, stale croissants, 
and one suspiciously sweaty thermos of herbal tea. Margaret, Chair of Snacks and Vibes, 
proudly held up a rainbow assortment of glitter pens like sacred relics and declared that 
"true creativity only flows when surrounded by sparkle." She had, however, neglected to mention 
that these pens had consumed half the magazine's annual budget. Harold tallied costs, Greg’s 
name buzzed through the room, the intern arranged chairs, and the janitor swept around the rainbow 
fallout while Margaret beamed.
"""


def act2_madeleine():
    """
    Returns Act II of the story - The Meeting Meltdown, from Madeleine.
    
    Returns:
        str: The story about the Bloom magazine board meeting.
    """
    return """Greg pointed a trembling finger at the table of board members, 
his eyes wild with the fervor of someone who had been rehearsing this moment 
in his bathroom mirror for weeks. "Bloom is the downfall of civilization!" 
he shouted, voice cracking somewhere between indignation and dramatic flair. 
"Your fonts are too whimsical, your margins are anarchy, and your metaphors… 
unforgivable!" The room fell silent except for the faint hum of the overhead 
lights and someone's very audible gasp. Margaret bristled, Harold adjusted 
the agenda, Greg doubled down, the intern typed furiously, and the janitor 
tapped the flickering light."""


def act3_madeleine():
    """
    Returns Act III of the story - The Meeting Meltdown, from Madeleine.
    
    Returns:
        str: The story about the Bloom magazine board meeting.
    """
    return """Just when the staff thought the drama was over, 
the office printer whirred ominously and spat out fifty copies 
of an unsigned manifesto titled "Bloom Forever: A Manifesto for 
a Magazine That Refuses to Fold." No one admitted to writing it, 
but Harold swore the toner smelled like Greg's cologne. Margaret, 
unwilling to be outdone by a rogue printer, decorated her copy with 
glitter stars, then announced it would be serialized in the next issue 
as "performance literature. Margaret decorated the margins, Harold 
checked page counts, Greg sniffed the toner suspiciously, the intern 
archived the stack, and the janitor asked who would recycle the other 
forty-nine."
"""


if __name__ == "__main__":
    # Test the functions
    name = get_name()
    print(f"My name is: {name}")
    
    story1 = act1_madeleine()
    print(f"\nAct 1:\n{story1}")
    
    story2 = act2_madeleine()
    print(f"\nAct 2:\n{story2}")
    
    story3 = act3_madeleine()
    print(f"\nAct 3:\n{story3}")
