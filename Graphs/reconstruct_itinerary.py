"""
LeetCode: 332

Given a list of airline tickets represented by pairs of departure and arrival
airports [from, to], reconstruct the itinerary in order. All of the tickets
belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Example:

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
"""

class Solution(object):
    def dfs(self, graph, start, path):
        while graph[start]:
            to = graph[start].pop()
            self.dfs(graph, to, path)

        path.append(start)

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ans = []
        graph = {}

        # Construct the graph

        for t in tickets:
            if t[0] not in graph:
                graph[t[0]] = []

            if t[1] not in graph:
                graph[t[1]] = []

            graph[t[0]].append(t[1])

        if len(graph['JFK']) < 1:
            return []

        self.dfs(graph, 'JFK', ans)

        return ans[::-1]

if __name__ == '__main__':
    s = Solution()

    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

    print(s.findItinerary(tickets))

    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

    print(s.findItinerary(tickets))
