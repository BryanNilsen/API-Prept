""" View module for handling requests about users """
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = User
        url = serializers.HyperlinkedIdentityField(
            view_name='user', lookup_field='id')
        fields = ('id', 'first_name', 'last_name', 'email',
                  'last_login', 'date_joined', 'username')


class UserViewSet(ViewSet):
    """User view set"""
    serializer_class = UserSerializer
    user = User.objects.all()

# class UserViewSet(ModelViewSet):
#     """User view set"""
#     queryset = User.objects.all()
