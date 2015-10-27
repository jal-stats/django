from rest_framework import serializers
from .models import Activity, Datapoint


class ActivitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Activity
        fields = ('id', 'full_description', 'units', 'url')


class DatapointSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Datapoint
        fields = ('id', 'activity', 'reps', 'date')

    def create(self, validated_data):
        validated_data['activity'] = self.context['activity']
        datapoint = Datapoint.objects.create(**validated_data)
        return datapoint
