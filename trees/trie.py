from typing import Dict

class TrieNode:
    '''
    The root trie will have ch = None and terminal = False
    '''
    def __init__(self, ch, terminal = False):
        self.ch = ch
        self.terminal = terminal
        self.children : Dict[str, TrieNode] = {}

def add_word(trie_node: TrieNode, word: str):
    current_node = trie_node
    for ch in word:
        if not ch in current_node.children:
            ch_trie_node = TrieNode(ch)
            current_node.children[ch] = ch_trie_node
            current_node = ch_trie_node
        else:
            ch_trie_node = current_node.children[ch]
            current_node = ch_trie_node
    current_node.terminal = True

def search_word(trie_node: TrieNode, word: str) -> bool:
    current_node = trie_node
    for ch in word:
        if not ch in current_node.children:
            return False
        current_node = current_node.children[ch]
    if current_node.terminal:
        return True
    return False
    