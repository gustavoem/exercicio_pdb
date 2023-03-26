def get_list_average(v):
    # calcula a média de uma lista v
    numerator = sum(v)
    denominator = len(v)
    return numerator / denominator

def test_it_finds_the_average_of_a_list_with_one_element():
    assert get_list_average([1]) == 1

def test_it_returns_none_for_an_empty_list():
    assert get_list_average([]) == None

