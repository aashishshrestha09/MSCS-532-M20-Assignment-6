from dataclasses import dataclass, field
from typing import Any


@dataclass
class TreeNode:
    """
    A simple rooted tree node.

    Attributes:
        data (Any): The value stored in the node.
        children (list['TreeNode']): list of child TreeNode objects.
    """

    data: Any
    children: list["TreeNode"] = field(default_factory=list)

    def add_child(self, child_node: "TreeNode") -> None:
        """
        Add a child node to this node.

        Args:
            child_node (TreeNode): The node to be added as a child.
        """
        self.children.append(child_node)

    def remove_child(self, child_node: "TreeNode") -> None:
        """
        Remove a specific child node from this node.

        Args:
            child_node (TreeNode): The node to be removed.
        """
        self.children = [child for child in self.children if child != child_node]

    def traverse(self) -> list[Any]:
        """
        Traverse the tree in pre-order (root → children).

        Returns:
            list[Any]: A flat list of node values in traversal order.
        """
        result = [self.data]
        for child in self.children:
            result.extend(child.traverse())
        return result

    def __repr__(self) -> str:
        return f"TreeNode({self.data})"
