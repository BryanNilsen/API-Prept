""" View module for handling requests about users """
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
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

    def create(self, request):
        """
        Handle POST Operations
        Returns:
            Response -- JSON serialized Water instance
        """
        newmember = Member()
        newmember.name = request.data["name"]
        newmember.gender = request.data["gender"]
        newmember.height = request.data["height"]
        newmember.weight = request.data["weight"]
        newmember.dob = request.data["dob"]
        newmember.profile_id = request.data["profile_id"]
        newmember.save()

        serializer = MemberSerializer(newmember, context={'request': request})
        return Response(serializer.data)

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

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single member
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            member = Member.objects.get(pk=pk)
            member.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Member.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
