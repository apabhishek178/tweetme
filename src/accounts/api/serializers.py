from django.contrib.auth import get_user_model
from rest_framework import serializers

user = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    class Meta:
        model = user
        fields = [
            'username',
            'first_name',
            'last_name',
            'follower_count'
        ]

    def get_follower_count(self,obj):
        print(obj.username)
        return 0
