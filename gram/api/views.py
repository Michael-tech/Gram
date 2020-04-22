#Dajngo rest Framwkor
from rest_framework.viewsets import ModelViewSet


#Models
from gram.models import *

#Serializers
from .serializers import *

class ContactsGenericView(ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsModelSerializer

class NotesGenericView(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesModelSerializer

class PostsGenericView(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsModelSerializer

class ProductsGenericView(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsModelSerializer
