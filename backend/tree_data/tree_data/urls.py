"""tree_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import rest_framework
from django.contrib import admin
from django.urls import path
from api import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', views.hello_world),
    path('parse_data/', views.parse_data),
    path('delete/', views.delete_all),
    path('tree_data/', views.tree_data),
    path('search_image/', views.search_image),
    path('search_image', views.search_image),
    path('node/<int:node_pk>/', views.get_node),
    path('node/<int:node_pk>', views.get_node),
    # path(r'^api-auth/', rest_framework.urls, name='api-auth-name'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
