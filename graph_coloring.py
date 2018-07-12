class GraphNode:
  def __inti__(self, label):
      self.label = label
      self.neighbors = set()
      self.color = None

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]
color = ['red', 'yellow', 'blue', 'green',
        'aqua', 'pink', 'magenta','purple',
        'black', 'white', 'brown']

def colorGraph(graph):
    graph[0].color = color[0]
    # i = 1
    # for i in range(size(graph)):
    if graph[i] in graph[i-1].neighbors:
        graph[1].color = color[1]
    else:
        graph[1].color = color[1]
