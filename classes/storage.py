import os
import json

from classes.node import NumNode


class NodeStorage:
    def __init__(self, name: str) -> None:
        self.storage_path: str = os.path.join(os.getcwd(), name)
        os.makedirs(os.path.join(self.storage_path),
                    exist_ok=True)

    def add_node(self, node: "NumNode") -> None:
        with open(os.path.join(self.storage_path, f"{node.value}.json"), "w+") as file:
            json.dump(node.dict(), file)

    def check(self, node: "NumNode") -> bool:
        files = os.listdir(self.storage_path)

        if f"{node.value}.json" in files:
            return True

        return False

    def get(self, node: "NumNode") -> "NumNode":
        with open(os.path.join(self.storage_path, f"{node.value}.json"), "r+") as file:
            data = json.load(file)

        node = NumNode(data["value"])

        for parent in data["from"]:
            node.add_from(parent)

        return node

    def get_working_directory(self) -> list[NumNode]:
        files: list[str] = sorted(os.listdir(self.storage_path), key=lambda x: int(x[:-5]))
        working_directory: list[NumNode] = []
        for node_name in files:
            with open(os.path.join(self.storage_path, node_name), "r+") as file:
                data: dict = json.load(file)
                current_node: NumNode = NumNode(data["value"])

                for value in data["from"]:
                    current_node.add_from(value)

            for saved_node in working_directory:
                if current_node.is_in_from(saved_node):
                    working_directory.remove(saved_node)

            working_directory.append(current_node)

        return working_directory
