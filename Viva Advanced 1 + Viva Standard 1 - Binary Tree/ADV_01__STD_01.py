import time


def recursive_find(number, cur):
    if number > cur.value and cur.right != None:
        return recursive_find(number, cur.right)
    elif number < cur.value and cur.left != None:
        return recursive_find(number, cur.left)
    if number == cur.value:
        return True
    return False


def find_r(number, cur):
    if type(number) != int:
        return False
    if number == cur.root.value:
        return True
    try:
        return recursive_find(number, cur.root)
    except:
        return False


def doTree():
    temp = BinaryTree(4)
    temp.insert(1)
    temp.insert(2)
    temp.insert(6)
    temp.insert(11)
    temp.insert(12)
    temp.insert(3)
    temp.insert(5)
    temp.insert(8)
    temp.insert(7)
    return temp


# In retrospect I should of made this function a method of the BinaryTree class as it would of been easier to do
# from an implementation and logic point of view.
def remove(target, tree):
    if not find_r(target, tree):
        print("Value not found in tree")
        return
    cur = tree.root
    # Path variable memorises the path that is taken to the target, and is used when we modify the tree
    path = ''
    # This while searches the target is
    while cur is not None:
        if target == cur.value:
            break;
        elif target > cur.value:
            cur = cur.right
            path += '.right'
        elif target < cur.value:
            cur = cur.left
            path += '.left'
    if cur.value != target:
        print("Number has not been found")
        return tree

    # Case 4: We are removing the root, as there are no children

    if cur.left is None and cur.right is None and path == '':
        cur.root = None
        print("You have just removed the root from the tree. Assign a new root to continue")
        tree.root = None
        return tree

    # Case1: If there is no child
    elif cur.left is None and cur.right is None:
        exec('tree.root' + path + '=None')
    # Case3: Both in left and right there is a child found. I chose to do Case3 before Case2 because its simpler
    # to think about the conditionals
    elif cur.left is not None and cur.right is not None:
        removePath = ''
        cur = cur.right
        while cur.left is not None:
            cur = cur.left
            removePath += '.left'
        exec('tree.root' + path + '.value = cur.value')
        exec('tree.root' + path + '.right' + removePath + '= cur.right')

    # Case 2: only one child is found

    elif cur.left is None:
        exec('tree.root' + path + ' = ' + 'tree.root' + path + '.right')
        exec('tree.root' + path + 'right = None')
    elif cur.right is None:
        exec('tree.root' + path + ' = ' + 'tree.root' + path + '.left')
        exec('tree.root' + path + 'left = None')

    return tree

    # My main issue with my code is that it heavily relies on the exec() function, and
    # I fear it's not that efficient.


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):

    def find_i(self, number):
        try:
            cur = tree.root
            while cur is not None:
                if cur.value == number:
                    return True
                elif number < cur.value:
                    cur = cur.left
                else:
                    cur = cur.right
            return False
        except TypeError:
            return False
            print("Please pass an integer")

    def __init__(self):
        self.root = None

    def __init__(self, root):
        self.root = Node(root)

    """DISPLAY FUNCTION FROM AULA"""

    def display(self, cur_node):
        if self.root == None:
            return
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)

    def _display(self, cur_node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    """INSERT FUNCTION FROM AULA"""

    def insert(self, value):
        if value is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value already present in tree")

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value already present in tree")


tree = BinaryTree(4)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(6)
tree.insert(11)
tree.insert(12)
tree.insert(3)
tree.insert(5)
tree.insert(8)
tree.insert(7)
#
print(tree.find_i(3))
print(tree.find_i(6))
print(tree.find_i("Hello"))
print(tree.find_i(15.443))
print(tree.find_i(99))
print(tree.find_i(tree.root.value))
print()
print(find_r(7, tree))
print(find_r(tree.root.value, tree))
print(find_r(143434, tree))
print(find_r("Hello", tree))
print()

tree.display(tree.root)
print("We remove 1 then add it. Then print to see the difference")
tree = (remove(1, tree))
tree.insert(1)
tree.display(tree.root)
print("We remove 11 to see the difference. Then print")
tree = (remove(11, tree))
tree.display(tree.root)
print("We remove 6 and 8 to see the difference. Then print and we check to see if 6 still exists")
tree = (remove(6, tree))
tree = (remove(8, tree))
tree.display(tree.root)
print(tree.find_i(6))
print(find_r(6, tree))
print("We remove twice in a row the root too see what happens. Print twice")
tree = (remove(4, tree))
tree.display(tree.root)
tree = (remove(5, tree))
tree.display(tree.root)
print("We remove all the elements from the tree")
tree = remove(7, tree)
tree = remove(12, tree)
tree.display(tree.root)
tree = remove(2, tree)
tree = remove(1, tree)
tree = remove(3, tree)
tree.display(tree.root)  # Doesnt print
print()

if input("Additionally, would you like to se a comparison between recursive and iterative searches?(y/n) ") == "y":
    nrOfLoops = int(input("Input your number of runs for each algorithm. It should be around the magnitudes of 10^5-6 "))
    start = time.time()
    tree = doTree()
    for i in range(nrOfLoops):
        tree.find_i(6)
    stop = time.time()
    time1 = stop - start

    start = time.time()
    for i in range(nrOfLoops):
        find_r(6, tree)
    stop = time.time()
    time2 = stop - start
    print(f"Iterative search time is about {round(time1,4)}, and recursive search time is about {round(time2,4)}.")
    print(f"This means that Iterative search is roughly {round((time1 / time2) * 100, 2)}% faster then recursive search")
