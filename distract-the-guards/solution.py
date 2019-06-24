class Graph:
    def __init__(self, banana_list):
        self.list_len = len(banana_list)
        self.graph = list([0] * self.list_len for i in xrange(self.list_len))
        for i in xrange(self.list_len):
            for j in xrange(self.list_len):
                if i < j:
                    self.graph[i][j] = self.dead_lock(banana_list[i], banana_list[j])
                    self.graph[j][i] = self.graph[i][j]

    def gcd(self, x, y):
        while (y):
            x, y = y, x % y
        return x

    def dead_lock(self, x, y):
        if x == y:
            return 0

        l = self.gcd(x, y)

        if (x + y) % 2 == 1:
            return 1

        x, y = x / l, y / l
        x, y = max(x, y), min(x, y)
        return self.dead_lock(x - y, 2 * y)

    # A DFS based recursive function that returns true if a
    # matching for vertex u is possible
    def bpm(self, u, match_r, visited):
        for v in range(self.list_len):
            if self.graph[u][v] and visited[v] == False:
                visited[v] = True  # Mark v as visited

                if match_r[v] == -1 or self.bpm(match_r[v], match_r, visited):
                    match_r[v] = u
                    return True
        return False

    # Returns maximum number of matching
    def max_pairs(self):
        match_r = [-1] * self.list_len
        count = 0
        for i in range(self.list_len):
            visited = [False] * self.list_len
            if self.bpm(i, match_r, visited):
                count += 1
        return self.list_len - 2 * (count / 2)

def solution(banana_list):
    return Graph(banana_list).max_pairs()

def main():
    print solution([1, 1])
    print solution([1, 7, 3, 21, 13, 19])
    print solution([1])
    print solution([1, 7, 1, 1])

if __name__ == '__main__':
    main()