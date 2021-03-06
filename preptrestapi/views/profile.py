""" View module for handling requests about users """
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
# TODO: put following on separate lines??
from preptrestapi.models import Profile, Member, Water, Food
from django.contrib.auth.models import User
from .user import UserSerializer
from .member import MemberSerializer
from .water import WaterSerializer
from .food import FoodSerializer


class ProfileWithRelatedDataSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for user profile"""

    user = UserSerializer()
    members = MemberSerializer(many=True)
    waters = WaterSerializer(many=True)
    foods = FoodSerializer(many=True)

    class Meta:
        model = Profile
        url = serializers.HyperlinkedIdentityField(
            view_name='profiledata', lookup_field='id')
        fields = ('id', 'url', 'user', 'user_id',
                  'water_goal', 'food_goal', 'members', 'waters', 'foods')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for user profile"""

    user = UserSerializer()

    class Meta:
        model = Profile
        url = serializers.HyperlinkedIdentityField(
            view_name='profile', lookup_field='id')
        fields = ('id', 'url', 'user', 'user_id',
                  'water_goal', 'food_goal')


class ProfileViewSet(ViewSet):
    """Profile for users"""

    # TODO: THIS DETAIL VIEW CONTAINS RELATED DATA // CREATE SEPARATE DETAIL FOR SIMPLE PROFILE VIEWING/EDITING
    def retrieve(self, request, pk=None):
        """Handle GET requests for single User Profile instance

        Args:
            request ([type]): [description]
            pk ([type], optional): [description]. Defaults to None.
        """
        try:
            profile = Profile.objects.get(pk=pk)
            profile.members = Member.objects.filter(profile_id=profile.id)
            profile.waters = Water.objects.filter(profile_id=profile.id)
            profile.foods = Food.objects.filter(profile_id=profile.id)
            serializer = ProfileSerializer(
                profile, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """
        Handle PUT Operations
        Returns:
            Response -- Empty body with 204 status code
        """
        profile = Profile.objects.get(pk=pk)
        profile.water_goal = request.data['water_goal']
        profile.food_goal = request.data['food_goal']
        profile.save()

        user = User.objects.get(pk=profile.user_id)
        user.username = request.data['username']
        user.email = request.data['email']
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        """ Handle get requests to user profile resource"""
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            profiles, many=True, context={'request': request})
        return Response(serializer.data)


class ProfileDataViewSet(ViewSet):
    """Profile for users"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single User Profile instance

        Args:
            request ([type]): [description]
            pk ([type], optional): [description]. Defaults to None.
        """
        try:
            profile = Profile.objects.get(pk=pk)
            profile.members = Member.objects.filter(profile_id=profile.id)
            profile.waters = Water.objects.filter(profile_id=profile.id)
            profile.foods = Food.objects.filter(profile_id=profile.id)
            serializer = ProfileWithRelatedDataSerializer(
                profile, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    # def list(self, request):
    #     """ Handle get requests to user profile resource"""
    #     profiles = Profile.objects.all()
    #     serializer = ProfileSerializer(
    #         profiles, many=True, context={'request': request})
    #     return Response(serializer.data)
