from rest_framework import routers
from .views import *
from django.urls import path, include


router = routers.SimpleRouter()
router.register('contacts', ContactsGenericView, basename='ContactsApi')
router.register('notes', ContactsGenericView, basename='NotesApi')
router.register('posts', ContactsGenericView, basename='PostsApi')
router.register('products', ContactsGenericView, basename='ProductsApi')


urlpatterns = [
    path('', include(router.urls)),
]
