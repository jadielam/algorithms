from algorithms.string.string_matching import naive_string_matching, rabin_karp_string_matching


def test_naive_string_matching_basic():
    t = "abcabc"
    p = "abc"
    assert naive_string_matching(t, p) == [0, 3]
    assert naive_string_matching("aaaa", "aa") == [0, 1, 2]


def test_rabin_karp_matches_naive_and_edge_cases():
    cases = [
        ("abcabc", "abc", [0, 3]),
        ("aaaa", "aa", [0, 1, 2]),
        ("abcdef", "gh", []),
        ("a", "a", [0]),
        ("", "", [0]),
        ("a", "aa", []),
    ]

    import pytest
    for t, p, expected in cases:
        if len(p) > len(t):
            with pytest.raises(IndexError):
                rabin_karp_string_matching(t, p)
        else:
            assert rabin_karp_string_matching(t, p) == expected
            assert rabin_karp_string_matching(t, p) == naive_string_matching(t, p)


def test_rabin_karp_randomized_matches_naive():
    import random
    random.seed(0)
    for _ in range(200):
        n = random.randint(0, 40)
        m = random.randint(0, n)  # ensure m <= n so implementation doesn't raise
        t = ''.join(random.choice('abcd') for _ in range(n))
        p = ''.join(random.choice('abcd') for _ in range(m))
        assert rabin_karp_string_matching(t, p) == naive_string_matching(t, p)


def test_rabin_karp_unicode_and_overlaps():
    # Unicode characters
    t = '😀😃😄😁😆😀😃'
    p = '😀😃'
    assert rabin_karp_string_matching(t, p) == [0, 5]

    # Overlapping matches
    t2 = 'aaaaa'
    p2 = 'aa'
    assert rabin_karp_string_matching(t2, p2) == [0, 1, 2, 3]

