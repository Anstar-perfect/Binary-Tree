tree =[None]*10

def ensure_capacity(index):
    if index >= len(tree):
        new_size = max(index+1,len(tree)*2)
        tree.extend([None]*(new_size-len(tree)))

def root(key):
    if tree[0] is not None:
        print("Tree has a root already")
    else:
        tree[0] =key

def set_left(key,parent):
    child_index = 2*parent+1
    if parent>= len(tree) or tree[parent] is None:
        print(f"Cannot set left child for parent {parent} as it does not exist")   
    else:
        ensure_capacity(child_index)
        tree[child_index] = key

def set_right(key,parent):
    child_index = 2*parent+2
    if parent>= len(tree) or tree[parent] is None:
        print(f"Cannot set right child for parent {parent} as it does not exist")   
    else:
        ensure_capacity(child_index)
        tree[child_index] = key

def print_tree():
    for i,value in enumerate(tree):
        if value is not None:
            print(f"{value} ",end='')
        else:
            print("None ",end='') 
    print()

root('A')
set_left('B',0)
set_right('C',0)    
set_left('D',1)
set_right('E',1)    
set_left('F',2)
set_right('G',2)
set_left('H',3)
set_right('I',3)

print_tree()

def print_tree_visually(index,indent=0):
    if index < len(tree) and tree[0] is not None:
        print_tree_visually(2*index+2,indent+4)
        print(" "*indent + str(tree[index]))
        print_tree_visually(2*index+1,indent+4)

print("Visual Representation of the tree:")
print_tree_visually(0)