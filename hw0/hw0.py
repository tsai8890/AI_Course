class Solution:
    def __init__(self):
        pass

    def solve(self):
        ## input part
        N, M = [int(i) for i in input().split()]

        graph = [[] for i in range(N+1)]
        for i in range(M):
            u, v = [int(i) for i in input().split()]
            graph[u].append(v)
            graph[v].append(u)

        for u in range(1, N+1):
            graph[u].sort()

        ## find the path
        visited = [0 for i in range(N+1)]
        visited[1] = 1
        cur, ans = 1, []
        
        while True:
            ans.append(cur)
            next = -1
            for v in graph[cur]:
                if not visited[v]:
                    next = v
                    visited[v] = 1
                    break

            if next == -1:
                break
            else:
                cur = next

        ## output the result
        for i in ans[:-1]:
            print('%d' %i, end=' ')
        print(ans[-1])

if __name__ == '__main__':
    ans = Solution()
    ans.solve()