class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        dictionary = {}
        for number in range(numRows):
            # Сколько будет строк
            dictionary[number] = []

        index_list = 0
        counting = 1
        for c in s:
            # Добавляем по индексу в список в словаре
            listN = dictionary[index_list]
            listN.append(c)

            # Увеличиваем счёт на 1 или уменьшаем если index_list >= numRows
            index_list += counting
            # Будем считать вниз и пока не дойдем до нуля и опять пойдем до numRows
            if index_list >= numRows:
                index_list -= 2
                counting *= -1
            if index_list < 0:
                index_list += 2
                counting *= -1

        result = ''
        for list_numbers in range(numRows):
            result += ''.join(dictionary[list_numbers])

        return result


s = Solution()
print(s.convert("amongus", 4))

"""Tests:
1.  Runtime: 73 ms, faster than 79.55% of Python3 online submissions for Zigzag Conversion.
Memory Usage: 14.2 MB, less than 14.73% of Python3 online submissions for Zigzag Conversion.
 
2. Runtime: 107 ms, faster than 42.40% of Python3 online submissions for Zigzag Conversion.
Memory Usage: 14.2 MB, less than 29.20% of Python3 online submissions for Zigzag Conversion.
"""
