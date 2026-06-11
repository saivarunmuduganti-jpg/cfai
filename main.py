import time
import random


class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return BSTNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value

        return node

    def search(self, key):
        current = self.root

        while current is not None:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return None

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self._min_value_node(node.right)
            node.key = successor.key
            node.value = successor.value
            node.right = self._delete(node.right, successor.key)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


def measure_time(operation):
    start = time.perf_counter()
    operation()
    end = time.perf_counter()
    return end - start


def main():
    n = 10000

    keys = list(range(n))
    random.shuffle(keys)

    search_keys = random.sample(keys, 1000)
    delete_keys = random.sample(keys, 1000)

    print("Hash Table vs Binary Search Tree")
    print("--------------------------------")
    print(f"Number of records: {n}")
    print()

    # Python Dictionary - Hash Table
    hash_table = {}

    hash_insert_time = measure_time(
        lambda: [hash_table.__setitem__(key, f"Value {key}") for key in keys]
    )

    hash_search_time = measure_time(
        lambda: [hash_table.get(key) for key in search_keys]
    )

    hash_delete_time = measure_time(
        lambda: [hash_table.pop(key, None) for key in delete_keys]
    )

    # Custom Binary Search Tree
    bst = BinarySearchTree()

    bst_insert_time = measure_time(
        lambda: [bst.insert(key, f"Value {key}") for key in keys]
    )

    bst_search_time = measure_time(
        lambda: [bst.search(key) for key in search_keys]
    )

    bst_delete_time = measure_time(
        lambda: [bst.delete(key) for key in delete_keys]
    )

    print("Performance Comparison")
    print("--------------------------------")
    print(f"{'Operation':<15}{'Python Dictionary':<25}{'Custom BST':<25}")
    print(f"{'Insert':<15}{hash_insert_time:<25.8f}{bst_insert_time:<25.8f}")
    print(f"{'Search':<15}{hash_search_time:<25.8f}{bst_search_time:<25.8f}")
    print(f"{'Delete':<15}{hash_delete_time:<25.8f}{bst_delete_time:<25.8f}")

    print()
    print("Time Complexity")
    print("--------------------------------")
    print("Hash Table / Python Dictionary:")
    print("Insert: O(1)")
    print("Search: O(1)")
    print("Delete: O(1)")

    print()
    print("Binary Search Tree:")
    print("Insert: O(log n)")
    print("Search: O(log n)")
    print("Delete: O(log n)")

    print()
    print("Conclusion")
    print("--------------------------------")
    print("Python Dictionary is faster because it uses hashing.")
    print("Binary Search Tree is useful because it stores data in sorted order.")
    print("For direct lookup, Hash Table is generally better.")
    print("For ordered data operations, BST is useful.")


if __name__ == "__main__":
    main()