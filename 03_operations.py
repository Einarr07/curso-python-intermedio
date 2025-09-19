set_a = {
    'colombia',
    'mexico',
    'bolivia'
}

set_b ={
    'peru',
    'bolivia'
}


if __name__ == '__main__':

    # Union
    # Also we can use the operator -> |
    set_c = set_a.union(set_b)
    print(f'Union -> {set_c}')

    # Intersection
    # Also we can use the operator -> &
    set_d = set_a.intersection(set_b)
    print(f'Intersection -> {set_d}')

    # Difference in set
    # Also we can use the operator -> -
    set_e = set_a.difference(set_b)
    print(f'Difference -> {set_e}')

    # Symmetric difference
    # Also we can use the operator -> ^
    set_f = set_a.symmetric_difference(set_b)
    print(f'Symmetric difference -> {set_f}')

