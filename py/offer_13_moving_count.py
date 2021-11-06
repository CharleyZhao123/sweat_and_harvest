def digitsum(n):
    ans = 0
    while n:
        ans += n%10
        n = n // 10
    return ans
class Solution:
    # DFS
    def movingCount1(self, m: int, n: int, k: int) -> int:
        maxn = [0]
        flag = [([0] * n) for i in range(m)]

        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or flag[i][j] == 1:
                return 0
            sum_i_j = digitsum(i) + digitsum(j)
            flag[i][j] = 1
            
            if sum_i_j <= k:
                maxn[0] += 1
            else:
                # 如果不满足条件，就不能继续走了
                return 0
            # 可以优化为只向右和向下搜索
            # dfs(i-1, j)
            dfs(i+1, j)
            # dfs(i, j-1)
            dfs(i, j+1)
            return 0

        dfs(0, 0)
        return maxn[0]

    # BFS
    def movingCount(self, m: int, n: int, k: int) -> int:
        from queue import Queue
        q = Queue()
        q.put((0, 0))
        s = set()
        while not q.empty():
            x, y = q.get()
            if x < m and y < n and (x, y) not in s and digitsum(x) + digitsum(y) <= k:
                s.add((x, y))
                q.put((x, y+1))
                q.put((x+1, y))
        return len(s)

    # 递推
    def movingCount2(self, m: int, n: int, k: int) -> int:
        vis = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in vis) and digitsum(i) + digitsum(j) <= k:
                    vis.add((i, j))
        return len(vis)



if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(16, 8, 4))