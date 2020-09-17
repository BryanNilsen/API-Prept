""" View module for handling requests about users """
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from preptrestapi.models import Water


class WaterSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Water items"""

    class Meta:
        model = Water
        url = serializers.HyperlinkedIdentityField(
            view_name='water', lookup_field='id')
        fields = ('id', 'url', 'profile_id', 'name', 'quantity', 'ounces',
                  'container')


class WaterViewSet(ViewSet):
    """Water resource"""

    def create(self, request):
        """
        Handle POST Operations
        Returns:
            Response -- JSON serialized Water instance
        """
        newwater = Water()
        newwater.name = request.data["name"]
        newwater.quantity = request.data["quantity"]
        newwater.ounces = request.data["ounces"]
        newwater.container = request.data["container"]
        newwater.profile_id = request.data["profile_id"]
        newwater.save()

        serializer = WaterSerializer(newwater, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single water item instance

        Args:
            request ([type]): [description]
            pk ([type], optional): [description]. Defaults to None.
        """
        try:
            water = Water.objects.get(pk=pk)
            serializer = WaterSerializer(
                water, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """ Handle get requests to water resource"""
        waters = Water.objects.all()
        serializer = WaterSerializer(
            waters, many=True, context={'request': request})
        return Response(serializer.data)
