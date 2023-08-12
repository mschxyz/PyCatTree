from PyCatTree import Tree as CTree

# Reading a tree from a file
ct = CTree('demo.ctr')

# Adding nodes
whatever = ct.addChildNode('Whatever')
whatever.addChildNode('Foo')
whatever.addChildNode('Bar')

print(ct)

# Creating a new empty tree
new_ct = CTree()

# Adding nodes
foo = new_ct.addChildNode('Foo') 
bar = new_ct.addChildNode('Bar')

foo.addChildNode('Beep') 
foo.addChildNode('Boop')

bar.addChildNode('Meep') 
bar.addChildNode('Moop')

print(new_ct) 
