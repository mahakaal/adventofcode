import re


class Node:
    def __init__(self):
        self.name = ''
        self.parent = None
        self.children = []
        self.value = 0
        self.type = ''

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        if 'file' == child.get_type():
            self.value += child.get_value()

        parent = self.get_parent()
        if parent:
            parent.set_value(parent.get_value() + child.get_value())

        self.children.append(child)

    def set_name(self, name):
        self.name = name

    def set_value(self, value):
        self.value = value

    def set_type(self, node_type):
        self.type = node_type

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_type(self):
        return self.type

    def get_dir_children(self):
        return [child for child in self.children if child.get_type() == 'dir']

    def get_child_by_name(self, child_name):
        for child in self.children:
            if child.get_name() == child_name:
                return child

        return None


def create_node(c_name, c_parent, c_type, c_value):
    child = Node()
    child.set_name(c_name)
    child.set_parent(c_parent)
    child.set_type(c_type)
    child.set_value(c_value)

    return child


filename = 'test-data.txt'

with open(filename, 'r') as file:
    instructions = [line for line in file.read().strip().split('\n')]

cur_dir, root = None, None

for line in instructions:
    if match_object := re.match(r'^\$ cd (.*)$', line):
        dir_name = match_object.group(1)

        if dir_name == '..':
            cur_dir = cur_dir.get_parent()
            continue

        if cur_dir:
            child_dir = cur_dir.get_child_by_name(dir_name)
            if child_dir:
                cur_dir = child_dir
                continue

        n_parent = cur_dir if dir_name != '/' else None
        node = create_node(dir_name, n_parent, 'dir', 0)

        if dir_name == '/':
            if root:
                cur_dir = root
            else:
                root = node
                cur_dir = node
            continue

        cur_dir = node
        del node

        continue

    if re.match(r'^\$ ls$', line):
        continue

    dim, n_name = line.split(' ')
    n_type = 'dir' if dim == 'dir' else 'file'
    n_value = 0 if dim == 'dir' else int(dim)

    cur_dir.add_child(create_node(n_name, cur_dir, n_type, n_value))

dir_100k = [child for child in root.get_children() if 'dir' == child.get_type() and 100_000 >= child.get_value()]

total = 0
for child_dir in dir_100k:
    total += child_dir.get_value() + sum(grand_child_dir.get_value() for grand_child_dir in child_dir.get_dir_children())

print(total)
