from algorithms.string.edit_distance import editDistance


def test_edit_distance_examples():
    assert editDistance(None, "kitten", "sitting") == 3
    assert editDistance(None, "", "") == 0
    assert editDistance(None, "a", "") == 1
