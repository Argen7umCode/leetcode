class Graph:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for index, value in enumerate(self.root):
                if self.root[index] == rootY:
                    self.root[index] = rootX
    
gr = Graph(10)
gr.union(1, 2)
gr.union(2, 5)
gr.union(6, 7)
gr.union(5, 6)
gr.union(3, 8)
gr.union(8, 9)

print(gr.root)