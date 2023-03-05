from collections import deque, defaultdict


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        hash_map = defaultdict(list)

        for index, num in enumerate(arr):
            hash_map[num].append(index)

        queue = deque([(0, 0)])
        visited, visited_groups = set(), set()

        while queue:
            steps, index = queue.popleft()

            if index == len(arr) - 1:
                return steps

            for neighbour in [index - 1, index + 1]:
                if 0 <= neighbour < len(arr) and neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((steps + 1, neighbour))

            if arr[index] not in visited_groups:
                for neighbour in hash_map[arr[index]]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((steps + 1, neighbour))

                visited_groups.add(arr[index])


def main():
    s = Solution()
    print(s.minJumps([11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 815 ms Beats 53.66% 
   Memory 32.9 MB Beats 17.7%
   
2. Runtime 815 ms Beats 53.66% 
   Memory 32.8 MB Beats 17.7%
"""
