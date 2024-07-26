# # # class Node:
# # #     def __init__(self, x, y, w, h):
# # #         self.x = x
# # #         self.y = y
# # #         self.w = w
# # #         self.h = h
# # #         self.left = None
# # #         self.right = None

# # # def setup():
# # #     global img, root
# # #     size(800, 600)
# # #     img = loadImage("./example.bmp")
# # #     img.loadPixels()
# # #     root = Node(0, 0, img.width, img.height)
# # #     box_test(root, 0)

# # # def draw():
# # #     background(255)
# # #     image(img, 0, 0)
# # #     noFill()
# # #     stroke(255, 0, 0)
# # #     draw_tree(root)

# # # def box_test(node, depth):
# # #     if depth >= 5 or node.w <= 2 or node.h <= 2:
# # #         return

# # #     found_one = False
# # #     for y in range(node.y, node.y + node.h):
# # #         for x in range(node.x, node.x + node.w):
# # #             if img.pixels[y * img.width + x] == color(0):
# # #                 found_one = True
# # #                 break
# # #         if found_one:
# # #             break

# # #     if not found_one:
# # #         return

# # #     mid_x = node.x + node.w // 2
# # #     mid_y = node.y + node.h // 2

# # #     node.left = Node(node.x, node.y, node.w // 2, node.h // 2)
# # #     box_test(node.left, depth + 1)

# # #     node.right = Node(mid_x, node.y, node.w - node.w // 2, node.h // 2)
# # #     box_test(node.right, depth + 1)

# # #     bottom_left = Node(node.x, mid_y, node.w // 2, node.h - node.h // 2)
# # #     box_test(bottom_left, depth + 1)

# # #     bottom_right = Node(mid_x, mid_y, node.w - node.w // 2, node.h - node.h // 2)
# # #     box_test(bottom_right, depth + 1)

# # # def draw_tree(node):
# # #     if node is None:
# # #         return
    
# # #     rect(node.x, node.y, node.w, node.h)
# # #     draw_tree(node.left)
# # #     draw_tree(node.right) 

# # class Node:
# #     def __init__(self, x, y, w, h):
# #         self.x = x
# #         self.y = y
# #         self.w = w
# #         self.h = h
# #         self.children = []

# # class BinaryTree:
# #     def __init__(self):
# #         self.root = None

# #     def add_node(self, node):
# #         if not self.root:
# #             self.root = node
# #         else:
# #             self._add_recursive(self.root, node)

# #     def _add_recursive(self, current, new_node):
# #         if not current.children:
# #             current.children.append(new_node)
# #         else:
# #             self._add_recursive(current.children[-1], new_node)

# # tree = BinaryTree()
# # img = None
# # max_recursion_depth = 5

# # def setup():
# #     global img
# #     size(800, 600)
# #     img = loadImage("example.bmp")
# #     img.loadPixels()
# #     box_test(0, 0, img.width, img.height, 0)

# # def draw():
# #     background(255)
# #     if img:
# #         image(img, 0, 0)
# #     draw_tree(tree.root)
# #     display_tooltip()

# # def box_test(x, y, w, h, depth):
# #     if depth >= max_recursion_depth or w <= 2 or h <= 2:
# #         node = Node(x, y, w, h)
# #         tree.add_node(node)
# #         return

# #     found_one = False
# #     for i in range(x, x + w):
# #         for j in range(y, y + h):
# #             if img.pixels[j * img.width + i] == color(0):
# #                 found_one = True
# #                 break
# #         if found_one:
# #             break

# #     if not found_one:
# #         node = Node(x, y, w, h)
# #         tree.add_node(node)
# #     else:
# #         half_w = w // 2
# #         half_h = h // 2
# #         box_test(x, y, half_w, half_h, depth + 1)
# #         box_test(x + half_w, y, half_w, half_h, depth + 1)
# #         box_test(x, y + half_h, half_w, half_h, depth + 1)
# #         box_test(x + half_w, y + half_h, half_w, half_h, depth + 1)

# # def draw_tree(node):
# #     if node:
# #         noFill()
# #         stroke(0)
# #         rect(node.x, node.y, node.w, node.h)
# #         for child in node.children:
# #             draw_tree(child)

# # def display_tooltip():
# #     mx, my = mouseX, mouseY
# #     current = tree.root
# #     path = ""
# #     highlight_node = None

# #     while current and current.children:
# #         half_w = current.w // 2
# #         half_h = current.h // 2
        
# #         if mx < current.x + half_w and my < current.y + half_h:
# #             path += "00"
# #             current = current.children[0] if current.children else None
# #         elif mx >= current.x + half_w and my < current.y + half_h:
# #             path += "10"
# #             current = current.children[1] if len(current.children) > 1 else None
# #         elif mx < current.x + half_w and my >= current.y + half_h:
# #             path += "01"
# #             current = current.children[2] if len(current.children) > 2 else None
# #         else:
# #             path += "11"
# #             current = current.children[3] if len(current.children) > 3 else None

# #         if current and not current.children:
# #             highlight_node = current

# #     if highlight_node:
# #         stroke(255, 0, 0)
# #         noFill()
# #         rect(highlight_node.x, highlight_node.y, highlight_node.w, highlight_node.h)

# #     fill(0)
# #     text("Quadrant: " + path, 10, height - 20)
# class BinaryTreeNode:
#     def __init__(self, x, y, w, h):
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, node):
#         if not self.root:
#             self.root = node
#         else:
#             self._insert_recursive(self.root, node)

#     def _insert_recursive(self, current, node):
#         if node.x < current.x:
#             if current.left is None:
#                 current.left = node
#             else:
#                 self._insert_recursive(current.left, node)
#         else:
#             if current.right is None:
#                 current.right = node
#             else:
#                 self._insert_recursive(current.right, node)

# tree = BinaryTree()
# img = None
# max_recursion_depth = 5

# def setup():
#     global img
#     size(200, 200)
#     noStroke()
#     img = loadImage("example.bmp")
#     box_test(0, 0, width, height, 0)

# def box_test(x, y, w, h, depth):
#     if depth >= max_recursion_depth or w <= 2 or h <= 2:
#         tree.insert(BinaryTreeNode(x, y, w, h))
#         return

#     found_one = False
#     for i in range(x, x + w):
#         for j in range(y, y + h):
#             if brightness(img.get(i, j)) > 0:
#                 found_one = True
#                 break
#         if found_one:
#             break

#     if not found_one:
#         tree.insert(BinaryTreeNode(x, y, w, h))
#     else:
#         new_w = w // 2
#         new_h = h // 2
#         box_test(x, y, new_w, new_h, depth + 1)
#         box_test(x + new_w, y, new_w, new_h, depth + 1)
#         box_test(x, y + new_h, new_w, new_h, depth + 1)
#         box_test(x + new_w, y + new_h, new_w, new_h, depth + 1)

# def draw():
#     background(255)
#     image(img, 0, 0)
#     display_quadrant()

# def display_quadrant():
#     x, y = mouseX, mouseY
#     current_x, current_y = 0, 0
#     current_w, current_h = width, height
#     binary_path = ""
#     depth = 0

#     while depth < max_recursion_depth and current_w > 2 and current_h > 2:
#         mid_x = current_x + current_w // 2
#         mid_y = current_y + current_h // 2

#         if x < mid_x and y < mid_y:
#             binary_path += "00"
#             current_w //= 2
#             current_h //= 2
#         elif x >= mid_x and y < mid_y:
#             binary_path += "10"
#             current_x = mid_x
#             current_w //= 2
#             current_h //= 2
#         elif x < mid_x and y >= mid_y:
#             binary_path += "01"
#             current_y = mid_y
#             current_w //= 2
#             current_h //= 2
#         else:
#             binary_path += "11"
#             current_x = mid_x
#             current_y = mid_y
#             current_w //= 2
#             current_h //= 2

#         depth += 1

#     stroke(255, 0, 0)
#     noFill()
#     rect(current_x, current_y, current_w, current_h)
#     fill(0)
#     text("Quadrant: " + binary_path, 10, height - 20)

# def mousePressed():
#     save("output.png")

class Node:
    def __init__(self, x, y, w, h, depth):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.depth = depth
        self.children = []
        self.binary = ''

def setup():
    global img, root, max_depth
    size(200, 200)
    # noStroke()
    img = loadImage("example2.bmp")
    max_depth = 8
    root = create_tree(0, 0, width, height, 0)

def draw():
    background(0)
    if img:
        image(img, 0, 0)
    display_tree(root)
    display_tooltip()

def create_tree(x, y, w, h, depth):
    node = Node(x, y, w, h, depth)
    if depth == max_depth or w <= 2 or h <= 2:
        return node
    
    found_one = False
    for i in range(x, x + w):
        for j in range(y, y + h):
            if red(img.get(i, j)) > 0:
                found_one = True
                break
        if found_one:
            break
    
    if not found_one:
        return node
    
    half_w = w // 2
    half_h = h // 2
    node.children = [
        create_tree(x, y, half_w, half_h, depth + 1),
        create_tree(x + half_w, y, half_w, half_h, depth + 1),
        create_tree(x, y + half_h, half_w, half_h, depth + 1),
        create_tree(x + half_w, y + half_h, half_w, half_h, depth + 1)
    ]
    return node

def display_tree(node):
    if not node.children:
        fill(0,0,0,150)
        rect(node.x, node.y, node.w, node.h)
    else:
        for child in node.children:
            display_tree(child)

def display_tooltip():
    binary = get_quadrant_binary(root, '')
    if binary:
        push()
        fill(255,0,0)
        text("Quadrant: " + binary, 10, height - 20)
        pop()
        highlight_quadrant(root, binary)
        

def get_quadrant_binary(node, current_binary):
    if not node.children:
        return current_binary if point_in_rect(mouseX, mouseY, node) else None
    
    for i, child in enumerate(node.children):
        result = get_quadrant_binary(child, current_binary + str(i))
        if result:
            return result
    return None

def highlight_quadrant(node, binary):
    if not binary:
        return
    
    if len(binary) == 1:
        stroke(255, 0, 0)
        # noFill()
        rect(node.x, node.y, node.w, node.h)
        noStroke()
        return
    
    index = int(binary[0])
    highlight_quadrant(node.children[index], binary[1:])

def point_in_rect(px, py, node):
    return (px >= node.x and px < node.x + node.w and
            py >= node.y and py < node.y + node.h)
