import os
import time
from memory_profiler import profile

# Open the file in read mode ('r')
file_path = os.path.join(os.getcwd(),'prefix-list.txt')
list_of_data=[]  # Replace 'your_file.txt' with the actual file path
with open(file_path, 'r') as file:
    # Read and print each line in the file
    for line in file:
        x=line.split()
        x[0]="0x"+x[0]
        x[0]=int(x[0],16)
        x[1]=int(x[1])
        x[2]=int(x[2],10)
        list_of_data.append(tuple(x))
       


class Node:
    def __init__(self):
        self.children = {}
        self.next_hop = None


class MultiBitTrie:
    def __init__(self, stride):
        self.root = Node()
        self.stride = stride

    def insert(self, prefix, length, next_hop):
        node = self.root
        for i in range(0, length, self.stride):
            key = (prefix >> max(0, min(length - i - self.stride, length))) & ((1 << self.stride) - 1)
            if key not in node.children:
                node.children[key] = Node()
            node = node.children[key]
        node.next_hop = next_hop
    def lookup(self, address):
        node = self.root
        result = None
        for i in range(0, 32, self.stride):
            key = (address >> max(0, min(32 - i - self.stride, 32))) & ((1 << self.stride) - 1)
            if key in node.children:
                node = node.children[key]
                if node.next_hop is not None:
                    result = node.next_hop
            else:
                break
        return result
    def print_tree(self, node, level=0, prefix=""):
        if node.next_hop is not None:
            print(f"{prefix} -> Next Hop: {node.next_hop}")
        for key, child in node.children.items():
            print(f"{prefix} - {key}")
            self.print_tree(child, level + 1, prefix + "  ")

@profile
def main():
    trie_strides = [1,2,4,8]

    for stride in trie_strides:
        start_time=time.time()
        print(f"\n--- Trie with Stride {stride} ---")
        trie = MultiBitTrie(stride)

        # Provided commands for inserting prefixes
        commands = list_of_data

        # Inserting prefixes based on the provided commands
        for prefix, length, next_hop in commands:
            trie.insert(prefix, length, next_hop)

        # Printing the trie
        trie.print_tree(trie.root)
        print(f'stride {stride} finished at {time.time()-start_time} seconds.')

if __name__ == "__main__":
    main()