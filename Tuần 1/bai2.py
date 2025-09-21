import pprint

# --- Đọc đồ thị từ file ---
def read_graph(filename):
    G = {}
    with open(filename, "rt", encoding="utf-8") as f:
        n = int(f.readline().strip())  # số đỉnh
        for line in f:
            parts = line.strip().split()
            if parts:
                G[parts[0]] = set(parts[1:])
    return G


# --- BFS ---
def BFS(G, start, goal):
    if G.get(start) is None or G.get(goal) is None:
        return None

    path = {start: None}
    s_open = [start]   # queue
    s_closed = []

    while s_open:
        u = s_open.pop(0)
        s_closed.append(u)

        if u == goal:
            break

        for v in G[u]:
            if v not in s_open and v not in s_closed:
                s_open.append(v)
                path[v] = u

    return path


# --- DFS ---
def DFS(G, start, goal):
    if G.get(start) is None or G.get(goal) is None:
        return None

    path = {start: None}
    s_open = [start]   # stack
    s_closed = []

    while s_open:
        u = s_open.pop()
        s_closed.append(u)

        if u == goal:
            break

        for v in G[u]:
            if v not in s_open and v not in s_closed:
                s_open.append(v)
                path[v] = u

    return path


# --- Hàm dựng đường đi từ path ---
def find_path(path, start, goal):
    if path is None or goal not in path:
        return []

    result = []
    cur = goal
    while cur is not None:
        result.insert(0, cur)
        cur = path[cur]

    if not result or result[0] != start:
        return []

    return result


if __name__ == "__main__":
    G = read_graph("graph.txt")

    print("Đồ thị (danh sách kề):")
    pprint.pprint(G)

    # Tìm đường từ A đến B
    bfs_path = BFS(G, "A", "B")
    dfs_path = DFS(G, "A", "B")

    print("\nBFS path map:")
    pprint.pprint(bfs_path)
    print("Đường đi BFS A→B:", find_path(bfs_path, "A", "B"))

    print("\nDFS path map:")
    pprint.pprint(dfs_path)
    print("Đường đi DFS A→B:", find_path(dfs_path, "A", "B"))
