from .node import Node
from .errors import *
from re import search

class Tree:
	"""Represents a cat tree
	
	If a file path is passed to the constructor, :obj:`Tree` tries to load and parse that file (:py:func:`Tree.load()`).
	Otherwise an empty tree with only the root node is created.
	
	Args:
		cat_tree_file_path (:obj:`PathLike`, optional): Path to the cat tree file
		indentor (str, optional): Indentation character to signal node depth at the beginning of a line in  the cat tree file *(Default: \t)*
		
	Attributes:
		root (:obj:`Node`): The tree's root node
	
	"""
	
	def __init__(self, cat_tree_file_path = None, indentor='\t'):
		self.indentor = indentor
		# Root node - has no name or parent node
		self.root = Node()
		# "addChildNode" and "removeChildNode" for root node can be directly called on tree object 
		self.addChildNode = self.root.addChildNode
		self.removeChildNode = self.root.removeChildNode
		# Load file, if given
		if cat_tree_file_path:
			self.load(cat_tree_file_path)
			
	def load(self, cat_tree_file_path):
		"""Loads and parses a Cat Tree file
		
		Args:
			cat_tree_file_path (str): Path to the cat tree file
			
		Raises:
			...
		
		"""
		with open(cat_tree_file_path, 'r') as ctf:
			raw_lines = ctf.readlines()
		# Keeping track of the current node depth and parent node
		# Starting off with depth = 1 as the root node has depth zero
		current_depth = 1
		current_parent = self.root
		for line_number, raw_line in enumerate(raw_lines, start=1):
			# Remove line breaks
			line = raw_line.strip('\n')
			# Check for comments
			try:
				line, comment = line.split('#', maxsplit=1)
			except ValueError:
				...
			# Non-empty lines
			if line.strip():
				node_depth = self.__getNodeDepth(line, self.indentor)
				node_name = line.lstrip(self.indentor).strip()
				if node_name:
					# Go down *one* level
					if (node_depth - current_depth == 1):
						current_depth += 1
						current_parent = new_node # The node that was created last
					# Go up *several* levels
					elif (node_depth - current_depth < 0):
						current_parent = new_node.parent
						while not node_depth == current_depth:
							current_depth -= 1
							current_parent = current_parent.parent
					# Not the same level? (i.e. are we trying to move *down* several levels at once?)
					elif not node_depth == current_depth:
						raise CatTreeIndentationError(
							'Indentation Error on line '+str(line_number)
						)
						
					# Add new node as child node to current parent
					new_node = (
						current_parent
						.addChildNode(
							node_name
						)
					)
				else:
					raise CatTreeNameError(
						'Missing node name on line '+str(line_number)
					)

	def __getNodeDepth(self, line, indentor):
		"""Gets the node depth
		
		Calculates the node depth from a line, depending on the number of indentation-characters at the beginning of the line.
		
		Args:
			line (str): Line from the Cat Tree file
			indentor (str): Indentation character (usually `\t`)
			
		Returns:
			int: Depth of the node in this line within the cat tree
			
		Note:
			Then root node (not present in the Cat Tree file) has depth zero.
		
		"""
		return (
			search(
				r'('+indentor+'*)',
				line
			)
			.groups()[0]
			.count(indentor)
		) + 1

	def traverse(self, root=None):
		"""Traverses the whole tree and yields the nodes
		
		Args:
			root (:obj:`Node`, optional): The node from which to start traversing
			
		Yields:
			:obj:`Node`: The current node on traversal
			
		Note:
			A recursvie generator function with `yield` and `yield from`.
			I haven't fully wrapped my head around this concept yet...
		
		"""
		if not root:
			root = self.root
		for node in sorted(list(root.children)):
			yield node
			yield from self.traverse(node)
			
	def subTreeToString(self, root=None):
		if not root:
			root = self.root
		lines = []
		for node in self.traverse(root):
			if (node.name):
				lines.append(
					self.indentor*(node.getDepth()-1)
					+node.name
				)
		return '\n'.join(lines)			

	def __str__(self):
		return self.subTreeToString(self.root)
