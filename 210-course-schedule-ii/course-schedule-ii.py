class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph and indegree array
        for course, prereq in prerequisites:
           graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph and indegree array
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Queue for courses with no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        result = []

        while queue:
            curr = queue.popleft()
            result.append(curr)

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If we could take all courses
        return result if len(result) == numCourses else []