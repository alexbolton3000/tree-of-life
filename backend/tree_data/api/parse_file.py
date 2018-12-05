
import os

from django.conf import settings
from dendropy import Tree, TaxonNamespace

from api.models import Animal


def file_name(name):
    return os.path.join(settings.DATASET_DIR, f'{name}.tre')


def tree_from_file(name):
    # From a file-like object
    d_tree = Tree.get(
        file=open(file_name(name), 'r'),
        schema="newick",
        tree_offset=0)
    return d_tree

# class AnimalNodeCreator:
#     @staticmethod
#     def new_node(d_node):
#         node = Animal(name=d_node.label)
#         return node
        

def traverse_tree(current_node, d_node):
    if not d_node.child_nodes():
        print(" END 0000000000000000000000000")
        print(d_node)
    for d_child in d_node.child_nodes():
        # print(d_child.label)
        child = current_node.add_child(name=get_name(d_child))
        # print(child)
        child.save()
        traverse_tree(child, d_child)
        child.save()
    return current_node 


def get_carnivora():
    d_tree = tree_from_file('carnivora')
    d_node_root = d_tree.seed_node
    
    print(d_node_root)
    print(d_node_root.label)
    # node = Animal(name=d_node_root.label)
    node = Animal.add_root(name=get_name(d_node_root))
    # node.save()
    node.add_child(name='the child')
    tree = traverse_tree(node, d_node_root)

    return tree

def get_name(d_node):
    return str(d_node.taxon.label) if d_node.taxon else 'NOTHING'



# print(t2)
# print(dir(t2))
# print(t2.as_ascii_plot())
# print(t2.calc_node_ages())
# print(t2.calc_node_root_distances())

# print('=====================root========================')
# root = t2.seed_node
# print(root)
# print(dir(root))
# print(root.label)
# print('-------------')
# print(root.child_nodes())

# print('==-=====================')

# print(t2.postorder_node_iter())

# for node in t2.postorder_node_iter():
#     print(node)
#     print(node.taxon)

# node = list(t2.postorder_node_iter())[0]
# print(node)
# parent = node.parent_node

# print('-----------------------')
# print(parent.child_nodes())










