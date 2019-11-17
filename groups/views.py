from rest_framework import viewsets
from .serializers import GroupSerializer, PersonSerializer, MembershipSerializer
from .models import Person, Group, Membership
from django.http import HttpResponse
from django.views import View

class GroupView(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class MembershipView(viewsets.ModelViewSet):
    serializer_class = MembershipSerializer
    queryset = Membership.objects.all()


