class brnode(object):
    """docstring for brnode"""
    def __init__(self, color=None, key=None, left=None, right=None, parent=None):
       self.color   = color
       self.key     = key
       self.left    = left
       self.right   = right
       self.parent  = parent

class brtree(object):
    nil = brnode("black", "nil", None, None, None)
    """docstring for brtree"""
    def __init__(self):
        self.root = self.nil

    def left_rotate(x):
        if x == self.nil or x.right == self.nil:
            return
        x.right = y.left

        if x.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == T.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.p = y

    def right_rotate(x):
        if x == self.nil or x.left == self.nil:
            return
        y = x.left

        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.p = y


    def insert(x):
        
        pass

    def insert_fixup(x):
        pass

    def delete(x):
        pass
        