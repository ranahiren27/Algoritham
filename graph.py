class graph():

	def __init__(self,numbers_of_node):
		cheak = True
		counter = 0
		self.nodes = numbers_of_node
		while cheak:
			if counter == 0:
				self.drection_notation = int(input("Press 1 for directed graph and 0 for undirected:"))
			else:
				self.drection_notation = int(input("Plaesh Press valid key!!"))

			if (self.drection_notation == 0)or(self.drection_notation == 1):
				cheak = False

		self.graph = [[0 for j in range(numbers_of_node)] for j in range(numbers_of_node+1)]

		if self.drection_notation == 0 :
			for i in range(self.nodes):
				for j in range(self.nodes):
					if i == j:
						self.graph[i][j] = 1

	def display(self):
		a = [j+1 for j in range(self.nodes)]
		print(0,a)
		for i in range(self.nodes):
			print(i+1,self.graph[i])

	def Addedeg(self,i,j):
		self.graph[i-1][j-1] = 1
		
		if self.drection_notation == 1:
			self.graph[j-1][i-1] = 1

	def __getitem__(self, key):
		return self.graph[key]

	def get_all_vertex(self):
		edge = list()
		a = [j+1 for j in range(self.nodes)]
		for i in range(self.nodes-1):
			edge.append(self.graph[i])
		return edge


g = graph(5)
g.Addedeg(1,2)
g.Addedeg(2,3)
g.Addedeg(3,4)
g.Addedeg(5,4)
g.Addedeg(1,4)
g.Addedeg(2,5)

g.display()
