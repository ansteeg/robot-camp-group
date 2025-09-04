def get_teamname():
    return "This is Team Zin er in. We are: \nMadeleine"

def get_name():
    """
    Returns my name as a string.
    
    Returns:
        str: The name "Madeleine"
    """
    return "Madeleine"


def act1_11():
    """
    Returns Act I of the story - The Meeting Meltdown, from Madeleine.
    
    Returns:
        str: The story about the Bloom magazine board meeting.
    """
    return """The quarterly Bloom magazine board meeting began with high hopes, stale croissants, 
and one suspiciously sweaty thermos of herbal tea. Margaret, Chair of Snacks and Vibes, 
proudly held up a rainbow assortment of glitter pens like sacred relics and declared that 
"true creativity only flows when surrounded by sparkle." She had, however, neglected to mention 
that these pens had consumed half the magazine's annual budget. Margaret beamed as glitter 
drifted across the room like confetti at a parade.
"""


def act2_11():
    """
    Returns Act II of the story - The Meeting Meltdown, from Madeleine.
    
    Returns:
        str: The story about the Bloom magazine board meeting.
    """
    return """Margaret rose to her feet, pointing dramatically at the table as though 
delivering a speech to history itself. "Bloom is the soul of civilization!" she declared, 
her voice echoing between the fluorescent lights. "Without whimsy in our fonts, without 
imagination in our margins, the world would crumble into beige monotony." 
Her words hung heavy in the silent room, broken only by the hum of the overhead lights. 
Margaret crossed her arms with fierce determination, glitter pen still clutched like a sword.
"""


def act3_11():
    """
    Returns Act III of the story - The Meeting Meltdown, from Madeleine.
    
    Returns:
        str: The story about the Bloom magazine board meeting.
    """
    return """Just when the drama seemed to fade, the office printer whirred ominously 
and spat out fifty copies of an unsigned manifesto titled "Bloom Forever: A Manifesto for 
a Magazine That Refuses to Fold." Margaret seized the stack triumphantly, decorating the 
first page with glitter stars before announcing it would be serialized in the next issue 
as "performance literature." She smiled, satisfied, already envisioning Bloom’s future 
written in sparkle across every page.
"""


if __name__ == "__main__":
    # Test the functions
    name = get_name()
    print(f"My name is: {name}")
    
    story1 = act1_11()
    print(f"\nAct 1:\n{story1}")
    
    story2 = act2_11()
    print(f"\nAct 2:\n{story2}")
    
    story3 = act3_11()
    print(f"\nAct 3:\n{story3}")
