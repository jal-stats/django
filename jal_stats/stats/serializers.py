# from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Activity, Stat


class StatAddSerializer(serializers.HyperlinkedModelSerializer):
    model = Stat
    activity_id = serializers.PrimaryKeyRelatedField(many=False,
                                                     read_only=True,
                                                     source='activity')

    class Meta:
        model = Stat
        fields = ('id', 'activity_id', 'reps', 'date')

    def create(self, validated_data):
        # activity = get_object_or_404(Activity, pk=self.context['activity_id'])
        validated_data['activity_id'] = self.context['activity_id']
        stat = Stat.objects.create(**validated_data)
        return stat


# class StatSerializer(StatAddSerializer):
#
#     class Meta:
#         model = Stat
#         fields = tuple(list(StatAddSerializer.Meta.fields) + ['activity'])


class ActivitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Activity
        fields = ('id', 'full_description', 'units', 'url')


class ActivityListSerializer(ActivitySerializer):
    stats = StatAddSerializer(many=True, read_only=True)

    class Meta:
        model = Activity
        fields = tuple(list(ActivitySerializer.Meta.fields) + ['stats'])


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'activities')
