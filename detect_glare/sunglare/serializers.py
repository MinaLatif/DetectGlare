from rest_framework import serializers
from .models import Post


# setting up the serialization function for the specific input parameters

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'lat',
            'lon',
            'epoch',
            'orientation'
        )
