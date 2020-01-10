# python3
import sys

from collections import deque

NA = -1


class Node:
    def __init__(self):
        self.next = [NA] * 4
        self.patternEnd = False


def build_trie(patterns):
    tree = dict()
    node_id = 0
    max_node_id = 0
    tree[node_id] = dict()

    for index, pattern in enumerate(patterns):
        node_id = 0
        current_node = tree[node_id]
        for i in range(len(pattern)):
            current_symbol = pattern[i]
            if current_symbol in current_node:
                node_id = current_node[current_symbol]
                current_node = tree[node_id]
            else:
                tree[max_node_id + 1] = dict()
                current_node[current_symbol] = max_node_id + 1
                current_node = tree[max_node_id + 1]
                max_node_id += 1
    return tree


def prefix_trie_matching(text, trie):
    text_local = deque(text)
    symbol = text_local.popleft()
    node_id = 0
    while True:
        # print(node_id, symbol)
        if trie[node_id] == dict():
            return True
        elif symbol in trie[node_id]:
            node_id = trie[node_id][symbol]
            if text_local:
                symbol = text_local.popleft()
            elif trie[node_id] != dict():
                return False
        else:
            return False


def trie_matching(text, trie):
    result = []
    index = 0
    while text:
        if prefix_trie_matching(text, trie):
            result.append(index)
        index += 1
        text = text[1:]

    return result


def solve(text, n, patterns):
    result = []

    trie = build_trie(patterns)
    print(trie)

    result = trie_matching(text, trie)

    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
