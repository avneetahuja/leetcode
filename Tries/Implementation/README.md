# Trie Implementation 🌳

## Problem Statement

Implement a Trie (Prefix Tree) with the following functionalities:

1. **Insert Word:**
   - Inserts a word into the Trie.

2. **Search Word:**
   - Returns `true` if the word is present in the Trie, and `false` otherwise.

3. **Search Prefix:**
   - Returns `true` if there is any word in the Trie that starts with the given prefix, and `false` otherwise.

## Approach 🛠️

The Trie is implemented using a class `Node`, where each node contains an array of links to child nodes, a boolean flag indicating the end of a word, and the necessary methods for trie operations.

1. **Node Class:**
   - `containsKey(char ch)`: Checks if the node contains a link for the character `ch`.
   - `put(char ch, Node* node)`: Adds a link for the character `ch` to the current node.
   - `get(char ch)`: Retrieves the node linked with the character `ch`.
   - `setEnd()`: Marks the current node as the end of a word.
   - `isEnd()`: Checks if the current node represents the end of a word.

2. **Trie Class:**
   - `insert(string word)`: Inserts a word into the Trie by iterating through its characters and creating nodes as needed.
   - `search(string word)`: Searches for a complete word in the Trie by traversing the Trie based on the characters of the word.
   - `startsWith(string prefix)`: Checks if there is any word in the Trie that starts with the given prefix.

## Complexity Analysis ⚙️

- The time complexity for inserting, searching, and checking prefixes is O(L), where L is the length of the word or prefix.
- The space complexity is determined by the number of nodes in the Trie, making it O(N), where N is the total number of characters in all inserted words.
