""" Python Example for the MarDATA Block course

Content:
- typehints
- asserts
- inline for loop
- method calls
"""


def build_pairs(group_one: list, group_two: list) -> list:
    """ Combines to list

    :param group_one:
    :param group_two:
    :return: list with all combinations from group_one and group_two
    """

    assert isinstance(group_one, list)
    assert isinstance(group_two, list)

    return [(element_a, element_b) for element_a in group_one for element_b in group_two]  # inline for loop


if __name__ == "__main__":

    print('First test')

    # this will fail
    # print(build_pairs(['a', 'b']))
    # print(build_pairs(['a', 'b'], 'test'))

    # this will work
    # print(build_pairs(['a', 'b'], [1, 2]))

    print(build_pairs(group_one=['a', 'b'], group_two=[1, 2]))

    # Bonus Tip
    print('zip: ', list(zip(['a', 'b', 'c'], [1, 2, 3])))
    print('unzip: ', list(zip(*[('a', 1), ('b', 2), ('c', 3)])))
