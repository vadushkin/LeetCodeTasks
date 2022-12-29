import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:

        next_task: list[tuple[int, int]] = []
        tasks_processing_order: list[int] = []

        sorted_tasks = [(enqueue, process, idx) for idx, (enqueue, process) in enumerate(tasks)]
        sorted_tasks.sort()

        curr_time = 0
        task_index = 0

        while task_index < len(tasks) or next_task:
            if not next_task and curr_time < sorted_tasks[task_index][0]:
                curr_time = sorted_tasks[task_index][0]

            while task_index < len(sorted_tasks) and curr_time >= sorted_tasks[task_index][0]:
                _, process_time, original_index = sorted_tasks[task_index]
                heapq.heappush(next_task, (process_time, original_index))
                task_index += 1

            process_time, index = heapq.heappop(next_task)

            curr_time += process_time
            tasks_processing_order.append(index)

        return tasks_processing_order


def main():
    s = Solution()
    print(s.getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 2075 ms Beats 83.44% 
   Memory 63.6 MB Beats 9.34%

2. Runtime 2083 ms Beats 82.30%
   Memory 63.5 MB Beats 13.28%
"""
