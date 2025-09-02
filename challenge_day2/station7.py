def solution_station_7(expr: str, values: dict[str, float]) -> float:
    """
    Evaluate expressions like 'e+b', 'a+c', 'd*c*b' using only + and *.
    values: mapping like {'a': 3.0, 'b': -0.5, 'c': 4.0, ...}
    """
    s = expr.replace(" ", "")

    def term_value(term: str) -> float:
        # product of factors split by '*'
        prod = 1.0
        for f in term.split('*'):
            if f.isalpha():
                if f not in values:
                    raise KeyError(f"Missing value for '{f}'")
                v = float(values[f])
            else:
                v = float(f)
            prod *= v
        return prod

    # sum of products split by '+'
    return sum(term_value(term) for term in s.split('+'))
