from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from api.models import Animal, Animal

class AnimalAdmin(TreeAdmin):
    form = movenodeform_factory(Animal)

admin.site.register(Animal, AnimalAdmin)
