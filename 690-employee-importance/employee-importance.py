"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {emp.id: emp for emp in employees}

        def dfs(id):
            if id not in emp_map:
                return 0
            
            employee = emp_map[id]
            total = employee.importance

            for subord in employee.subordinates:
                total += dfs(subord)
            return total

        return dfs(id)
        