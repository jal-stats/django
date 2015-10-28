# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Activity, Stat


class StatSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Stat
        fields = ('id', 'activity', 'reps', 'date')

    def create(self, validated_data):
        validated_data['activity'] = self.context['activity']
        stat = Stat.objects.create(**validated_data)
        return stat

# 
# class StatSerializer(StatSerializer):
#
#     class Meta:
#         model = Stat
#         fields = tuple(list(StatAddSerializer.Meta.fields) + ['activity'])


class ActivitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Activity
        fields = ('id', 'full_description', 'units', 'url')


class ActivityListSerializer(ActivitySerializer):
    stats = StatSerializer(many=True, read_only=True)

    class Meta:
        model = Activity
        fields = tuple(list(ActivitySerializer.Meta.fields) + ['stats'])


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'activities')
