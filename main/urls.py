from django.urls import path 
from .views import print_request
urlpatterns = [
 path('api/grabtoken' , print_request )
    
]