def get_name():
    """
    Returns my name as a string.
    
    Returns:
        str: The name "Madeleine"
    """
    return "Madeleine"


def get_story():
    """
    Returns a story about a Bloom magazine board meeting.
    
    Returns:
        str: The story "Act I – The Meeting Meltdown"
    """
    return """Act I – The Meeting Meltdown
The quarterly Bloom magazine board meeting began 
with high hopes and stale croissants. Margaret, 
Chair of Snacks and Vibes, was passionately defending 
her decision to spend half the budget on glitter pens 
when Harold, Treasurer of Paperclips, slammed the table 
and declared, "This is financial terrorism!" Before Margaret 
could launch into a speech about the power of stationery in 
shaping artistic destiny, the door creaked open and in stormed 
Greg — self-proclaimed "Bloom hater" and man who once tried to 
sue a sunflower for copyright infringement."""


if __name__ == "__main__":
    # Test the functions
    name = get_name()
    print(f"My name is: {name}")
    
    story = get_story()
    print(f"\nMy story:\n{story}")
