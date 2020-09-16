""" View module for handling requests about users """
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from preptrestapi.models import Member
# from .profile import ProfileSerializer


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for members"""

    # profile = ProfileSerializer()

    class Meta:
        model = Member
        url = serializers.HyperlinkedIdentityField(
            view_name='member', lookup_field='id')
        fields = ('id', 'profile_id', 'name', 'dob', 'gender',
                  'height', 'weight')


class MemberViewSet(ViewSet):
    """Member resource"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single member instance

        Args:
            request ([type]): [description]
            pk ([type], optional): [description]. Defaults to None.
        """
        try:
            member = Member.objects.get(pk=pk)
            serializer = MemberSerializer(
                member, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """ Handle get requests to member resource"""
        members = Member.objects.all()
        serializer = MemberSerializer(
            members, many=True, context={'request': request})
        return Response(serializer.data)
