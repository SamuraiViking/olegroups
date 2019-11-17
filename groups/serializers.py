from rest_framework import serializers
from groups.models import Group, Person, Membership

class PersonSerializer(serializers.ModelSerializer):
    group_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Person
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    # members = serializers.StringRelatedField(many=True)
    members = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'

class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = '__all__'
