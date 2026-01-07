from algorithms.string.string_matching import naive_string_matching


def test_naive_string_matching_basic():
    t = "abcabc"
    p = "abc"
    assert naive_string_matching(t, p) == [0, 3]
    assert naive_string_matching("aaaa", "aa") == [0, 1, 2]
