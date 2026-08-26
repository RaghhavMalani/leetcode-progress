"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""

        data = []

        def dfs(node):
            data.append(str(node.val))
            data.append(str(len(node.children)))

            for child in node.children:
                dfs(child)

        dfs(root)

        return " ".join(data)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        values = data.split()
        index = 0

        def dfs():
            nonlocal index

            val = int(values[index])
            index += 1

            childCount = int(values[index])
            index += 1

            node = Node(val, [])

            for _ in range(childCount):
                node.children.append(dfs())

            return node

        return dfs() 

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))