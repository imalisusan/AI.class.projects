from collections import defaultdict
from filecmp import cmp
from queue import Queue

import queue as Q


class GBfsTraverser:
  def __init__(self):

    self.visited={}
    self.steps={}
    self.parent={}
    self.output=[]
    self.queue = Queue()
    self.q = Q.PriorityQueue()
    self.path=[]
  def GBFS(self,graph,heuristic,start_node, goal_node):
    ten = []
    for node in graph.nodes.keys():
      self.visited[node]=False
      self.parent[node]=None
      self.steps[node]=-1



    s=start_node
    self.visited[s]=True
    self.steps[s]=0
    self.queue.put(s)
    ten.append(s)
    while not self.queue.empty():


      # Dequeue a vertex from
      u = self.queue.get()
      self.output.append(u)
      for v in list(graph[u]):



        if not self.visited[v]:
          self.q.put((heuristic[v], v))


      t=self.q.get()[1]


      ten.append(t)
      self.queue.put(t)
      if t==goal_node:
        break;
      self.visited[t] = True
      self.parent[t] = u
      self.steps[t] = self.steps[u] + 1
    p=goal_node
    for n in ten:
      self.path.append(n)
      p=self.parent[n]
      print(n)
   
