""" View module for handling requests about users """
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from preptrestapi.models import Profile
from .user import UserSerializer


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for user profile"""

    user = UserSerializer()

    class Meta:
        model = Profile
        url = serializers.HyperlinkedIdentityField(
            view_name='profile', lookup_field='id')
        fields = ('id', 'user', 'user_id', 'water_goal', 'food_goal')


class ProfileViewSet(ViewSet):
    """Profile for users"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single User Profile instance

        Args:
            request ([type]): [description]
            pk ([type], optional): [description]. Defaults to None.
        """
        try:
            profile = Profile.objects.get(pk=pk)
            serializer = ProfileSerializer(
                profile, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """ Handle get requests to user profile resource"""
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            profiles, many=True, context={'request': request})
        return Response(serializer.data)
