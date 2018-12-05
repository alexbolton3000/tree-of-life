from collections import OrderedDict
import json


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

from api import models
from api import parse_file


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

@api_view(['GET', 'POST'])
def parse_data(request):
    tree = parse_file.get_carnivora()
    print(tree)
    return Response({'tree': str(tree)})
    
@api_view(['GET', 'POST'])
def delete_all(request):
    animals = models.Animal.objects.all()
    count = len(list(animals))
    animals.delete()
    return Response({'msg': f'Deleted {count}'})


@api_view(['GET', 'POST'])
def tree_data(request):
    root = models.Animal.objects.filter(pk=7122).first()
    print(root)
    print(dir(root))
    serialized_tree = TreeSerializer().serialize_tree(root)
    # print(tree)
    return Response(serialized_tree)
    


class TreeSerializer:
    nodes = None
    links = None

    def __init__(self):
        self.nodes = OrderedDict()
        self.links = []


    def serialize_tree(self, current_node):
        self.traverse_tree(current_node)

        # Format 
        data = dict(nodes=self.nodes_to_list(), links=self.links)
        return data

    def traverse_tree(self, current_node):
        if not self.nodes:
            # Must be root node
            self.nodes[current_node.pk] = self.node_format(current_node)

        # Add children to nodes
        children = current_node.get_children()
        for child in children:
            self.nodes[child.pk] = (self.node_format(child))
        
        # Add links to children
        current_node_index = self.node_index(current_node)
        for child in children:
            self.links.append(
                dict(
                    source=current_node_index, 
                    target=self.node_index(child),
                    value=1
                )
            )
            
        for child in children:
            self.traverse_tree(child)

    def nodes_to_list(self):
        l = []
        for k, v in self.nodes.items():
            l.append(v)
        return l

    def node_index(self, node):
        return list(self.nodes.keys()).index(node.pk)

    def node_format(self, node):
        return dict(name=node.display_name, group=2, pk=node.pk)











