# Django rest Framework
from rest_framework import serializers

# Model
from gram.models import *


class ContactsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class NotesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'


class PostsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


class ProductsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
