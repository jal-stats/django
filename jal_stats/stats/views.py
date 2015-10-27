# from django.shortcuts import render
from rest_framework import viewsets
from .models import Datapoint, Activity
from .serializers import ActivitySerializer, DatapointSerializer

# Create your views here.


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):
        return self.request.user.activity_set.all()


class DatapointViewSet(viewsets.ModelViewSet):
    serializer_class = DatapointSerializer

    def get_queryset(self):
        return Datapoint.objects.all().filter(
            # user=self.request.user,
            activity=self.request.query_params['activity'])
