class Node:
	"""Represents a node in the cat tree
	
	Args:
		name (str, optional): This node's name *(Default: None - reserved for the root node)*
		parent (:obj:`Node`, optional): This node's parent node *(Default: None - reserved for the root node)*
	
	Attributes:
		name (str): The node's name
		parent (:obj:`Node`): The parent node
		children (set of :obj:`Node`): This node's children
	
	"""
	
	def __init__(self, name = None, parent = None):
		self.name = name
		self.parent = parent
		self.children = set()
		
	def addChildNode(self, node):
		if type(node) is str:
			node = Node(node)
		if not node.parent:
			node.parent = self
		self.children.add(node)
		return node
		
	def removeChildNode(self, node):
		self.children.remove(node)

	def getDepth(self):
		parent = self.parent
		depth = 0
		while parent:
			parent = parent.parent
			depth += 1
		return depth

	def __str__(self):
		return self.name
	
	def __repr__(self):
		return (
			'CatTreeNode:'
			+ ' "'+self.name+'"'
			+ ' (Depth: '+str(self.getDepth())
			+ ' | Parent: '+str(self.parent.name)
			+ ' | Children: '+str(self.children)+')'
		)
		
	def __lt__(self, other):
		return self.name < other.name
		
	def __gt__(self, other):
		return self.name > other.name
		
	def __del__(self):
		"""Delete this node
		
		Attach this node's children to the parent and delete this node from the parent's children.
		
		Note:
			Doesn't seem to work yet...
		
		"""
		for child in self.children:
			child.parent = self.parent
			if self.parent:
				self.parent.addChildNode(child)
		if self.parent:
			self.parent.removeChildNode(self)
