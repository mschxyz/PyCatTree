# PyCatTree

Python (de-)serializer for [Cat Tree](https://github.com/mschxyz/Cat-Tree) files.

This is just a toy, but maybe someone finds it useful.

## Installation

>not (yet) on PyPI

## Usage

The cat tree file used in the following examples `demo.ctr`:

```
# A demo cat tree
Food
	Hot
		Soup
		Steak
	Cold
		Sandwich
		Ice Cream
		
Drinks
	Hot
		Coffee
		Tea # could be cold, though
	Cold
		Beer
		Soda
```

### Example 1: Reading a cat tree from a file

```python
from PyCatTree import Tree as CTree

ct = CTree('demo.ctr')

print(ct)
```

output

```
Food
	Hot
		Soup
		Steak
	Cold
		Sandwich
		Ice Cream
Drinks
	Hot
		Coffee
		Tea
	Cold
		Beer
		Soda
```

### Example 2: Reading a cat tree from a file and adding more nodes

```python
from PyCatTree import Tree as CTree

ct = CTree('demo.ctr')

whatever = ct.addChildNode('Whatever')
whatever.addChildNode('Foo')
whatever.addChildNode('Bar')

print(ct)
```

output

```
Food
	Hot
		Soup
		Steak
	Cold
		Sandwich
		Ice Cream
Drinks
	Hot
		Coffee
		Tea
	Cold
		Beer
		Soda
Whatever
	Bar
	Foo
```

### Example 3: Creating an empty tree and adding nodes

```python
from PyCatTree import Tree as CTree

new_ct = CTree()

foo = new_ct.addChildNode('Foo') 
bar = new_ct.addChildNode('Bar')

foo.addChildNode('Beep') 
foo.addChildNode('Boop')

bar.addChildNode('Meep') 
bar.addChildNode('Moop')

print(new_ct) 
```

output

```
Bar
	Meep
	Moop
Foo
	Beep
	Boop
```
