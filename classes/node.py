class NumNode:
    """Node class for the graph gen."""

    def __init__(self, value: int) -> None:
        """Init the class.

        Args:
            value (int): number id of the node.
        """
        self.value: int = value
        self._from = set()

    def add_from(self, value: int):
        """Add value to the set.

        Args:
            value (int): value to be saved for the node.
        """
        self._from.add(value)

    def is_in_from(self, node: "NumNode") -> bool:
        return (node.value in self._from)

    def __eq__(self, value: "NumNode") -> bool:

        return (self.value == value.value)

    def dict(self) -> dict:
        return {"value": self.value,
                "from": list(self._from)}

    def __str__(self) -> str:
        return f'{self.value}'

    def __repr__(self) -> str:
        return f"{self.value}"
