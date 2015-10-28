# from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, permissions  # , serializers
from .models import Stat, Activity
# from .permissions import IsAPIUser
from .serializers import ActivitySerializer, ActivityListSerializer, StatSerializer

# Create your views here.


# class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
#     permission_classes = (permissions.IsAuthenticated,
#                           IsAPIUser)


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    # def get_queryset(self):
    #     return self.request.user.activity_set.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ActivitySerializer
        else:
            return ActivityListSerializer


class StatViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = StatSerializer

    def get_queryset(self):
        activity = get_object_or_404(Activity, pk=self.kwargs['activity_pk'])
        return Stat.objects.all().filter(
            # user=self.request.user,
            activity=activity)

    def get_serializer_context(self):
        context = super().get_serializer_context().copy()
        activity = get_object_or_404(Activity, pk=self.kwargs['activity_pk'])
        context['activity'] = activity
        return context

    # def perform_create(self, serializer):
    #     serializers.save(user=self.request.user)
