import string

from django.db import models

from treebeard.mp_tree import MP_Node


class Animal(MP_Node):
    # Basic

    # Names
    name = models.CharField(max_length=1000)
    display_name = models.CharField(max_length=1000, blank=True, null=True)
    scientific_name = models.CharField(max_length=1000, blank=True, null=True)
    phylopic_name = models.CharField(max_length=1000, blank=True, null=True)
    wiki_name = models.CharField(max_length=1000, blank=True, null=True)

    # Time
    # In M.Y.A.
    birth = models.IntegerField(blank=True, null=True)
    extinction = models.IntegerField(blank=True, null=True)

    node_order_by = ['name']
    def __unicode__(self):
        return 'Category: %s' % self.name

    # Admin
    created_date_2 = models.DateTimeField(auto_now_add=True)
    modified_date_2 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.display_name)} ({self.pk})'

    def save(self, *args, **kwargs):
        print(self)
        if not self.display_name:
            self.display_name = string.capwords(self.name)
        super(Animal, self).save(*args, **kwargs)
