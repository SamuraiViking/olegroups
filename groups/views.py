from rest_framework import viewsets
from .serializers import GroupSerializer, MemberSerializer
from .models import Group, Member

class GroupView(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class MemberView(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


