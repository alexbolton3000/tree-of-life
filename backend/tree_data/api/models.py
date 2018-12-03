from django.db import models




# Model plan
# 
# 
# NAME FIELDS:
display_name
scientific_name
phylopic_name
wiki_name
# name (default ot display name)
# 
# TIME
# birth
# extinction
# 
# RESOURCES
# phylopic image - CLASS
# other images
# 
# TREE STUFF
# parent 
# child
# 
# 
# 



class Animal(models.Model):
    # Basic


   	# Names
   	name = models.CharField(max_length=1000)
	display_name = models.CharField(max_length=1000)
	scientific_name = models.CharField(max_length=1000)
	phylopic_name = models.CharField(max_length=1000)
	wiki_name = models.CharField(max_length=1000)

   	# Time
   	# In M.Y.A.
   	birth = models.IntegerField()
   	extinction = models.IntegerField()

   	# Tree
   	parent = models.ForeignKey(Animal)
   	# , on_delete=models.CASCADE
   	child = models.ForeignKey(Animal)

   	# Admin
    created_date_2 = models.DateTimeField(auto_now_add=True)
    modified_date_2 = models.DateTimeField(auto_now=True)







