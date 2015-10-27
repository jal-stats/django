from rest_framework import serializers
from .models import Activity, Datapoint


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'user', 'full_description', 'units', 'url')


class DatapointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Datapoint
        fields = ('id', 'user', 'activity', 'reps', 'timestamp', 'url')
