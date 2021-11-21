class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None

class Binary_tree:

    def __init__(self,root = None):
        self.root = root
    def pre_order(self):

            value_list = []
            
            def pre_order_inside(root):

                value_list.append(root.value)

                if root.left: 
                    pre_order_inside(root.left)

                if root.right :
                    pre_order_inside(root.right)
            if self.root:
                pre_order_inside(self.root)
            return value_list
    def in_order(self):
        
            value_list = []
            def in_order_inside(root):
                if root.left: 
                    in_order_inside(root.left)

                value_list.append(root.value)

                if root.right :
                    in_order_inside(root.right)
            if self.root:
                in_order_inside(self.root)
            return value_list
    def post_order(self):

        value_list = []

        def post_order_inside(root):
            if root.left: 
                post_order_inside(root.left)

            if root.right :
                post_order_inside(root.right)
            
            value_list.append(root.value)
        if self.root:
            post_order_inside(self.root)
        return value_list
    def max(self):
        max_num = 0
        list_of_item = self.post_order()
        for i in list_of_item:
            if max_num < i:
                max_num = i
        return max_num
    def max_globle(self):
        self.max_num = 0
        def walk_inside_tree(root):
            if root.left: 
                walk_inside_tree(root.left)

            if root.right :
                walk_inside_tree(root.right)
            if root.value > self.max_num:
                self.max_num = root.value
        if self.root:
            walk_inside_tree(self.root)
        return self.max_num


class Binary_search_tree():
    def __init__(self):
        self.root = None
        self.current = None
    def add(self,value):
        def rec_add(value):
            if self.current.value == value : 
                raise Exception("already exist")
            if self.current.value > value : 
                
                if self.current.left:
                    self.current = self.current.left
                    rec_add(value)  
                else:
                    self.current.left = Node(value)

            if self.current.value < value :
            
                if self.current.right:
                    self.current = self.current.right
                    rec_add(value)
                else:
                    self.current.right = Node(value)

        
        if not self.root:
            self.root = Node(value)
            return self.root
        else:
            self.current = self.root
            rec_add(value)

    def contain(self,value):
        if self.root:
            self.current = self.root
        else:
            raise Exception("Empty tree")
        def contain_rec():

            if self.current:
                if self.current.value < value:
                    self.current = self.current.right
                    contain_rec()

            if self.current:   
                if self.current.value > value:
                    self.current = self.current.left
                    contain_rec()

            if self.current:
                if self.current.value == value:
                    return True
            else :
                return False

        return contain_rec()

     
      
            



first_n =Node(1)
second_n = Node(2)
third_n = Node(3)
first_n.left = second_n
first_n.right = third_n
second_n.left=Node(4)
second_n.right = Node(5)
third_n.left = Node(6)
third_n.right = Node(7)
binary_tree=Binary_tree(first_n)
# binary_tree.pre_order()
# binary_tree.in_order()
# binary_tree.post_order()
print(binary_tree.max_globle())
# binary_search_tree=Binary_search_tree()
# binary_tree=Binary_tree(binary_search_tree.add(5))
# binary_search_tree.add(7)
# binary_search_tree.add(3)
# binary_tree.in_order()
# a = binary_search_tree.contain()
# print(a)