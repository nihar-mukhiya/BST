# author : NIHAR MUKHIYA
# date : 18/09/2018
# description : implementation of various operations of BST such as
#               insertion, deletion, max-min value, parent-of-a-node, inorder, preorder, postorder
#               in python


import  sys
class Node(object):
    def __init__(self, val):
        self.rc = None
        self.lc = None
        self.val = val

    def insert(self, val):
        if(self.val):
            if(val<self.val):
                if(self.lc is None):
                    self.lc = Node(val)
                else:
                    self.lc.insert(val)
            elif(val>self.val):
                if(self.rc is None):
                    self.rc = Node(val)
                else:
                    self.rc.insert(val)
            else:
                self.val = val

    def minValue(self, node):
        current = node
        while(current.lc is not None):
            current = current.lc
        return current

    def findParent(self, val):
        parent = None
        while True:
            if(self.val is None):
                return (None, None)
            if(self.val == val):
                return (parent, self)
            if(self.val < val):
                parent, self = self, self.rc
            else:
                parent, self = self, self.lc

    def deleteNode(self, val):
        parent, node = self.findParent(val)
        # if node has no children
        if(node.lc is None and node.rc is None):
            if(parent):
                if(parent.lc is node):
                    parent.lc = None
                else:
                    parent.rc = None

            # if node with no children is root itself
            else:
                self.val = None
            del node
        # if node has one child
        else:
            if(node.lc is None):
                t = node.rc
                if (parent):
                    if (parent.lc is node):
                        parent.lc = t
                    else:
                        parent.rc = t
                    del node
                # if node with one child that is deleted is root itself
                else:
                    self.lc = t.lc
                    self.rc = t.rc
                    self.val = t.val

            elif(node.rc is None):
                t = node.lc
                if (parent):
                    if (parent.lc is node):
                        parent.lc = t
                    else:
                        parent.rc = t
                    del node
                # if node with one child that is deleted is root itself
                else:
                    self.lc = t.lc
                    self.rc = t.rc
                    self.val = t.val
        try:
            node
            temp = self.minValue(node.rc)
            p1, n1 = self.findParent(temp.val)
            node.val = temp.val
            if(p1.lc is n1):
                p1.lc = None
            else:
                p1.rc = None
        except:
            print("node deleted")

        """
        # if node has two children
        parent = node
        successor = node.rc
        while(successor.lc):
            node = successor
            successor = successor.lc
        parent.val = successor.val
        node.lc = None
        if(parent.lc == successor):
            parent.lc = successor.rc
        else:
            parent.lc = successor.rc
        """

    def inorder(self):
        if(self.val):
            if(self.lc):
                self.lc.inorder()
            print(self.val)
            if(self.rc):
                self.rc.inorder()
        else:
            print("Tree is Empty")

    def preorder(self):
        print(self.val)
        if (self.lc):
            self.lc.preorder()
        if (self.rc):
            self.rc.preorder()

    def postorder(self):
        if (self.lc):
            self.lc.postorder()
        if (self.rc):
            self.rc.postorder()
        print(self.val)



a = int(input("enter root"))
root = Node(a)



while(1):
    z = input("Enter your choice\n 1. Insert\n2.smallest element\n 3. Inorder\n 4. Preorder\n 5. Postorder\n 6.Delete\n7. Exit\n")
    if (z == '1'):
        b = int(input("enter the number of elements to be inserted"))
        while (b > 0):
            c = int(input("enter elements: "))
            root.insert(c)
            b -= 1

    elif(z == '2'):
        y = root.minValue(root)
        print("The smallest element in BST is: " +str(y)+ "/n")

    elif (z == '3'):
        print("INORDER is: ")
        root.inorder()

    elif(z== '4'):
        print("PREORDER is: ")
        root.preorder()

    elif(z=='5'):
        print("POSTORDER is: ")
        root.postorder()

    elif(z == '6'):
        g = int(input("enter element to be deleted: "))

        v = root.deleteNode(g)


    elif(z=='7'):
        sys.exit()



    else:
        print("wrong input!!")