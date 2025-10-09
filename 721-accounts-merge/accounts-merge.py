class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
       
        from collections import defaultdict

        graph = defaultdict(set)
        email_to_name = {}

        # Build graph connections between emails
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                email_to_name[email] = name
                graph[emails[0]].add(email)
                graph[email].add(emails[0])

        visited = set()
        res = []

        def dfs(email):
            stack = [email]
            component = []
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    component.append(node)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            stack.append(neighbor)
            return component

        # Find all connected components (merged accounts)
        for email in graph:
            if email not in visited:
                merged_emails = dfs(email)
                res.append([email_to_name[email]] + sorted(merged_emails))

        return res
