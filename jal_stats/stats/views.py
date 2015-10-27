# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets  # , serializers
from .models import Datapoint, Activity
from .serializers import ActivitySerializer, DatapointSerializer

# Create your views here.


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    # def get_queryset(self):
    #     return self.request.user.activity_set.all()


class DatapointViewSet(viewsets.ModelViewSet):
    serializer_class = DatapointSerializer

    def get_queryset(self):
        activity = get_object_or_404(Activity, pk=self.kwargs['activity_pk'])
        return Datapoint.objects.all().filter(
            # user=self.request.user,
            activity=activity)

    def get_serializer_context(self):
        context = super().get_serializer_context().copy()
        activity = get_object_or_404(Activity, pk=self.kwargs['activity_pk'])
        context['activity'] = activity
        return context

    # def perform_create(self, serializer):
    #     serializers.save(user=self.request.user)
