from rest_framework import serializers

from audio.models import AudioBook, Podcast, Song


class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = "__all__"


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"
