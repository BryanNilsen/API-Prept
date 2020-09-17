""" View module for handling requests about users """
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from preptrestapi.models import Food, Profile


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Food items"""

    class Meta:
        model = Food
        url = serializers.HyperlinkedIdentityField(
            view_name='food', lookup_field='id')
        fields = ('id', 'profile_id', 'name', 'brand', 'quantity', 'ounces',
                  'servings', 'calories_per_serving', 'container', 'expiration_date')


class FoodViewSet(ViewSet):
    """Food resource"""

    def create(self, request):
        """
        Handle POST Operations
        Returns:
            Response -- JSON serialized Food instance
        """
        newfood = Food()
        newfood.name = request.data["name"]
        newfood.brand = request.data["brand"]
        newfood.quantity = request.data["quantity"]
        newfood.ounces = request.data["ounces"]
        newfood.servings = request.data["servings"]
        newfood.calories_per_serving = request.data["calories_per_serving"]
        newfood.container = request.data["container"]
        newfood.expiration_date = request.data["expiration_date"]
        newfood.profile_id = request.data["profile_id"]
        newfood.save()

        serializer = FoodSerializer(newfood, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single food item instance

        Args:
            request ([type]): [description]
            pk ([type], optional): [description]. Defaults to None.
        """
        try:
            food = Food.objects.get(pk=pk)
            serializer = FoodSerializer(
                food, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """ Handle get requests to food resource"""
        foods = Food.objects.all()
        serializer = FoodSerializer(
            foods, many=True, context={'request': request})
        return Response(serializer.data)
