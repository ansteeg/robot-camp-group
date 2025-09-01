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
that these pens had consumed half the magazine's annual budget.

Harold, Treasurer of Paperclips, adjusted his three pairs of glasses and 
slammed the table so hard that two croissants became airborne. "This," he 
thundered, "is not budgeting. This is financial terrorism!" A hush fell 
over the room, except for the sound of the intern quietly choking on a raisin scone. 
Margaret shot back with a glare so sharp it could cut cardboard, preparing to deliver 
a manifesto about how stationery is the bedrock of civilization.

Before she could launch into her ten-minute PowerPoint on "The Socioeconomic Importance of Glitter," 
the door creaked open. In stormed Greg, the infamous Bloom hater, known in town for once trying to 
sue a sunflower for copyright infringement. His scarf was dramatically long, his expression permanently 
scowling, and his hands clutched a binder labeled "Bloom = Doom."

"Ladies, gentlemen, and glitter enthusiasts," Greg sneered, "I have come to expose this fraudulent operation." 
He slammed his binder on the table, sending more crumbs flying. "Bloom magazine is nothing but overpriced doodles 
wrapped in pretentious adjectives. And I, as a concerned citizen, demand the immediate disbanding of this… paper cult."

Margaret gasped so loudly that three pigeons outside the window startled and flew off. Harold, secretly 
pleased that someone else was angry at Margaret, leaned back with a smirk and muttered, "Finally, someone 
who speaks sense." The intern, unsure whether to take minutes or dial emergency services, quietly wrote "apocalypse???" 
in the meeting notes.

Tension filled the air like a badly timed incense stick. Margaret clutched her glitter pens to her chest as though 
shielding them from Greg's dark aura. "You don't understand," she whispered fiercely. "Without Bloom, the world will 
descend into beige despair." Greg rolled his eyes so hard he nearly sprained them. Harold licked a croissant crumb 
off his tie and muttered, "Beige might be cheaper."
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
lights and someone's very audible gasp."""


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
as "performance literature."
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
