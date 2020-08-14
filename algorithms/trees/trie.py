from typing import Dict, List

class TrieNode:
    '''
    The root trie will have ch = None and terminal = False
    '''
    def __init__(self, ch):
        self.ch = ch
        self.word = None
        self.children : Dict[str, TrieNode] = {}

def add_word(trie_node: TrieNode, word: str):
    '''
    Adds word to trie rooted on trie_node
    '''
    current_node = trie_node
    for ch in word:
        if not ch in current_node.children:
            ch_trie_node = TrieNode(ch)
            current_node.children[ch] = ch_trie_node
            current_node = ch_trie_node
        else:
            ch_trie_node = current_node.children[ch]
            current_node = ch_trie_node
    current_node.word = word

def find_node(trie_node: TrieNode, prefix: str) -> TrieNode:
    '''
    Searches for prefix on trie rooted at trie_node and returns the
    last TrieNode of the search. If it cannot find the entire prefix,
    returns None
    '''
    current_node = trie_node
    for ch in prefix:
        if not ch in current_node.children:
            return None
        current_node = current_node.children[ch]
    return current_node

def search_word(trie_node: TrieNode, word: str) -> bool:
    '''
    Returns true if word was found in trie, otherwise returns false
    '''
    final_node = find_node(trie_node, word)
    return True if final_node is not None and final_node.word is not None else False

def prefix_search(trie_node: TrieNode, prefix: str) -> List[str]:
    '''
    Returns all words in trie that have the given prefix
    '''
    to_return = []
    final_node = find_node(trie_node, prefix)
    
    if final_node is None:
        return to_return
    
    # Do BFS on nodes, appending words as I find them as terminals
    queue = [final_node]
    while len(queue) > 0:
        node = queue.pop(0)
        if node.word is not None:
            to_return.append(node.word)
        for child_node in node.children.values():
            queue.append(child_node)
    
    return to_return