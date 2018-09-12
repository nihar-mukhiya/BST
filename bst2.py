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

    def deleteNode(self, val):

        if self is None:
            return None

        elif(self.lc is None and self.rc is None):
            self = None
            return self
        if(val < self.val):
            self.lc = self.lc.deleteNode(val)

        elif(val > self.val):
            self.rc = self.rc.deleteNode(val)

        else:

            if(self.lc is None):
                temp = self.rc
                self = None
                return temp

            elif(self.rc is None):
                temp = self.lc
                self = None
                return temp

            temp = self.minValue(self.rc)

            self.val = temp.val

            self.rc = self.deleteNode(self.rc, temp.val)
        return self


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