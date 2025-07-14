class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        # Add original indices to the tasks and sort them by enqueueTime
        sorted_tasks = sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)])
        
        result = []
        heap = []
        time = 0  # Current CPU time
        i = 0  # Pointer for sorted_tasks

        while i < n or heap:
            # If no task is available, move time to the next enqueueTime
            if not heap and time < sorted_tasks[i][0]:
                time = sorted_tasks[i][0]
            
            # Push all available tasks into the heap
            while i < n and sorted_tasks[i][0] <= time:
                enqueueTime, processingTime, idx = sorted_tasks[i]
                heapq.heappush(heap, (processingTime, idx))
                i += 1
            
            if heap:
                processingTime, idx = heapq.heappop(heap)
                time += processingTime
                result.append(idx)
        
        return result
        