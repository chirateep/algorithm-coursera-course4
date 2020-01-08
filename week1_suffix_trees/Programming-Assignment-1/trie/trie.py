# Uses python3
import sys


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
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


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
