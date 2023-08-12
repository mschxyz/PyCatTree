# PyCatTree - Changelog

## 0.1.X

### 0.1.0
_(initial publication)_

#### Tree
* initialization with cat tree file or as empty tree (root node only)
* `load(path)` to load and parse a cat tree file
* `traverse(node)` generator function for tree traversal with `node` as traversal root
* `subTreeToString(node)` render a sub tree as string with `node` as the sub tree's root

#### Node
* initialization with optional name and parent node (usually reserved for the root node)
* `addChildNode(node)` to add a child node either by supplying a new node name or an existing Node object
* `removeChildNode(node)`
* `getDepth()` to get the node's depth in the cat tree (only the root node has depth zero)

#### Errors
* `CatTreeNameError` is a parsing error raised on a missing category name
* `CatTreeIndentationError` is a parsing error raised in improper indentation
