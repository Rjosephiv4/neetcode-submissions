class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = {}

        for element in tasks:
            frequency[element] = frequency.get(element,0) + 1

        lists = []
        for item,count in frequency.items():
            lists.append([-1*count,item])
        heapq.heapify(lists)
        queue = collections.deque()
        i = 0
        while queue or lists:
            if queue and queue[0][1] <= i:
                heapq.heappush(lists, queue.popleft()[0])
            if lists:
                element = heapq.heappop(lists)
                element[0] +=1
                if element[0] < 0:
                    queue.append((element, i + n + 1))
            i += 1
        return i

