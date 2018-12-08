import os
import string

from django.db import models
from django.conf import settings
from treebeard.mp_tree import MP_Node

from api import image_manager

import requests 

class Animal(MP_Node):
    # Basic

    # Names
    name = models.CharField(max_length=1000, default='NONE')
    display_name = models.CharField(max_length=1000, blank=True, null=True)

    # pic = models.ForeignKey('PhyloPic', on_delete=models.CASCADE)
    # scientific_name = models.CharField(max_length=1000, blank=True, null=True)
    # phylopic_name = models.CharField(max_length=1000, blank=True, null=True)
    # wiki_name = models.CharField(max_length=1000, blank=True, null=True)

    # # Time
    # # In M.Y.A.
    # birth = models.IntegerField(blank=True, null=True)
    # extinction = models.IntegerField(blank=True, null=True)

    # # Admin
    # created_date_2 = models.DateTimeField(auto_now_add=True)
    # modified_date_2 = models.DateTimeField(auto_now=True)
    
    node_order_by = ['name']
    def __unicode__(self):
        return 'Category: %s' % self.name

    def __str__(self):
        return f'<{str(self.name)} * {str(self.display_name)} ({self.pk}) Animal>'

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = 'NO NAME'
        if not self.display_name:
            self.display_name = string.capwords(self.name)
        super(Animal, self).save(*args, **kwargs)

    # @property 
    # def local_file_uri(self):
    #     return os.path.join(settings.SVG_DIR, self.image_name)

    @property
    def image_name(self):
        return f'{self.name.replace(" ", "_")}-{self.pk}.svg'

    @property
    def image_uri(self):
        return f'{settings.STATIC_URL}{self.image_name}'

    @property
    def full_image_uri(self):
        if self.name == 'NOTHING':
            return None 
        try:
            file_path = os.path.join(settings.SVG_DIR, self.image_name)
            fh = open(file_path, 'r')
            print("Image found")
            return f'{settings.LOCAL_DOMAIN}{self.image_uri}'
        except FileNotFoundError:        
            return None 


    def download_image(self):
        print("")
        print("DOWNLOAD IMAGE")
        print(self.name)
        if self.name == "NOTHING":
            return None
        image_urls = []
        file_path = os.path.join(settings.SVG_DIR, self.image_name)
        try:
            fh = open(file_path, 'r')
            print("Image found")
        except FileNotFoundError:
            # Get most image urls
            image_urls = image_manager.search_image(self.name)
            try:
                # Download the image
                r = requests.get(image_urls[0], allow_redirects=True)
                # Save image to disk
                open(file_path, 'wb').write(r.content)
                print('>>>>>>>>>>>>>>>>>>>>>>>>>> Saved file')
            except IndexError as e:
                print('CANT DOWNLOAD')
                print(self.name)
                return None
                # raise e
       
        return self.full_image_uri
       
        # phylo_pic = PhyloPic(animal=self)

# class PhyloPic(models.Model):
#     # animal = models.ForeignKey(Animal, on_delete=models.CASCADE)


#     @property 
#     def file_name(self):
#         return f'{settings.DATASET_DIR}{self.animal.pk}.{self.animal.name}.svg'

#     def __str__(self):
#         return f'<{self.file_name} PhyloPic>'


#     # @property 
#     # def name(self):
#     #     return 

#     def download_image(self):
#         image_id = image_manager.search_image(self.name)
#         image_url = image_manager.phylopic_get_image_url(image_id)
        
#         phylo_pic = PhyloPic(animal=self)


# def save_image(url, ):
#     new_file_name = 
#     r = requests.get(url, allow_redirects=True)
#     open('google.ico', 'wb').write(r.content)
    



