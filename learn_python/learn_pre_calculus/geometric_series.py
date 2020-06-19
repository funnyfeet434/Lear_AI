def get_geometric_series(start, factor, amount_terms):
    i = 0
    terms = []


    while i < amount_terms:
        terms.append(start*(factor**i))
        i += 1
        print("Term {}: {}".format(i, terms[-1]))

    return sum(terms)

print(get_geometric_series(42000, 1.04, 8))