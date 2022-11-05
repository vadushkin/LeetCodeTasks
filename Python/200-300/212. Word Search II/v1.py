class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        root = {}
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node[None] = True

        board = {i + j * 1j: c
                 for i, row in enumerate(board)
                 for j, c in enumerate(row)}

        found = []

        def search(node, loc, word):
            if node.pop(None, None):
                found.append(word)

                path = [root]
                for char in word:
                    path.append(path[-1].get(char))

                if not path[-1]:
                    for char, parent in zip(word[::-1], path[::-1][1:]):
                        if len(parent) > 1:
                            break
                        del parent[char]

            char = board.get(loc)
            for k in range(4):
                if char in node:
                    board[loc] = None
                    search(node[char], loc + 1j ** k, word + char)
                    board[loc] = char

        for loc in board:
            search(root, loc, '')

        return found


def main():
    s = Solution()
    print(s.findWords([["o", "a", "a", "n"],
                       ["e", "t", "a", "e"],
                       ["i", "h", "k", "r"],
                       ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"]))


if __name__ == "__main__":
    main()

"""Tests:
# 1. Time Limit Exceeded 38 / 64 testcases passed
# 2. Time Limit Exceeded 38 / 64 testcases passed

1. Runtime 9110 ms Beats 7.9%
   Memory 16.5 MB Beats 37.50%
   
2. Runtime 9150 ms Beats 6.84% 
   Memory 16.4 MB Beats 48.46%
"""
