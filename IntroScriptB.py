""" Example in Python

For the MarDATA Block course
"""


def build_pairs(group_one: list, group_two: list = [3, 4]) -> list:  # mutable argument
    """ Combines to list

    :param group_one:
    :param group_two:
    :return: list with all combinations from group_one and group_two
    """

    assert isinstance(group_one, list)
    assert isinstance(group_two, list)

    result_list = [(element_a, element_b) for element_a in group_one for element_b in group_two]  # inline for loop

    group_two[0] = 5

    return result_list


if __name__ == "__main__":

    print('Second test')
    print(build_pairs(group_one=['a', 'b']))
    print(build_pairs(group_one=['a', 'b']))
