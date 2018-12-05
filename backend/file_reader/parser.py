
from dendropy import Tree, TaxonNamespace

import os

EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), './')

print(EXAMPLE_DIR)

from nexus import NexusReader
n = NexusReader()
n.read_file(os.path.join(EXAMPLE_DIR, 'carnivora.nex'))

print(n)
print(dir(n))
print('============================================')
print(n.blocks)
print(n.trees)
# for tree in n.trees:
#   print(tree)

print(n.trees[0])
print(dir(n.trees[0]))
# for taxa in n.taxa:
#   print(taxa)


# print(n.trees)
# print(n.trees)
# print(n.trees)
# print(n.trees)



# print(data)

# print(n.data.nchar)

# print(n.data.ntaxa)
# print(n.data)

print('====================================')

# From a file-like object
t2 = Tree.get(file=open(os.path.join(EXAMPLE_DIR, './carnivora.tre'), 'r'),
                schema="newick",
                tree_offset=0)

print(t2)
print(dir(t2))
print(t2.as_ascii_plot())
print(t2.calc_node_ages())
print(t2.calc_node_root_distances())

print('=====================root========================')
root = t2.seed_node
print(root)
print(dir(root))
print(root.label)
print('-------------')
print(root.child_nodes())

print('==-=====================')

print(t2.postorder_node_iter())

for node in t2.postorder_node_iter():
    print(node)
    print(node.taxon)
    print(dir(node.taxon))
    taxon = node.taxon 
    print('taxon......................')
    print(taxon.annotations)
    print(taxon.clone)
    print(taxon.comments)
    print(taxon.copy_annotations_from)
    print(taxon.deep_copy_annotations_from)
    print(taxon.description)
    print(taxon.has_annotations)
    print(taxon.label)
    print(taxon.lower_cased_label)
    print(taxon.taxon_namespace_scoped_copy)

node = list(t2.postorder_node_iter())[0]
print(node)
parent = node.parent_node

print('-----------------------')
print(parent.child_nodes())










