def round_up(x):
    if x % 1 == 0:
        return int(x)
    else:
        return int(x//1 + 1)

def chunker(iterable, size):
    # Implement function here
    for group in range(round_up(len(iterable)/size)):
        yield iterable[group*size:group*size+size]


for chunk in chunker(range(25), 4):
    print(list(chunk))