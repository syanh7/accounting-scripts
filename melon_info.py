"""Print out all the melons in our inventory."""


from melons import melons

def print_melon(melons):
    """Print each melon with corresponding attribute information."""

    for melon, melon_info in melons.items():
        print(melon.upper())
        for key, value in melon_info.items():
            print(f'\t{key}: {value}')


print_melon(melons)
