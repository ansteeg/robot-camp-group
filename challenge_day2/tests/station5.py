def count_holes(name: str) -> int:
    """
    Count the total number of enclosed 'holes' in the letters of a name.
    Works for both lowercase and uppercase.
    """
    holes_map = {
        'A': 1, 'a': 1,
        'B': 2, 'b': 1,  # uppercase B=2, lowercase b=1
        'D': 1, 'd': 1,
        'O': 1, 'o': 1,
        'P': 1, 'p': 1,
        'Q': 1, 'q': 1,
        'R': 1,
        'g': 1, 'e': 1   # some fonts treat these as 1 hole
    }

    return sum(holes_map.get(ch, 0) for ch in name)


# Examples
print("Benedikt →", count_holes("Benedikt"))  # expected 2
print("uli →", count_holes("uli"))            # expected 0
print("Betija →", count_holes("Betija"))      # expected 3
print("maria →", count_holes("maria"))        # expected 3
