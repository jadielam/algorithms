from algorithms.trees.trie import TrieNode, add_word, search_word, prefix_search


def test_trie_basic_search_and_prefix():
    root = TrieNode(None)
    add_word(root, 'apple')
    add_word(root, 'app')
    assert search_word(root, 'app') is True
    assert search_word(root, 'ap') is False
    prefixes = prefix_search(root, 'app')
    assert set(prefixes) == {'app', 'apple'}
