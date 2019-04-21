from rest_framework import serializers

from .models import Topic, Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Post


class TopicSerializer(serializers.ModelSerializer):
    posts = PostSerializer(read_only=True, many=True)

    class Meta:
        fields = '__all__'
        model = Topic
