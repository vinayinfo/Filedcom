from audio.models import AudioBook, Podcast, Song
from rest_framework import viewsets
import datetime
from rest_framework.decorators import action
from rest_framework.response import Response
from audio.serializers import AudioBookSerializer, PodcastSerializer, SongSerializer


class AudioViewSet(viewsets.ViewSet):
    audiofiletype = {"song": Song, "audiobook": AudioBook, "podcast": Podcast}
    audioserializers = {"song": SongSerializer, "audiobook": AudioBookSerializer, "podcast": PodcastSerializer}
    http_method_names = ['get', 'put', 'post', 'delete']

    def create_audio(self, request, *args, **kwargs):
        data = request.data
        type = data.get("audioFileType", None)
        audio_type = self.audiofiletype.get(type)
        if type and audio_type:
            metadata = data.get("audioFileMetadata")
            # check duration time and upload time
            if metadata["duration_time"] <= 0:
                metadata["duration_time"] = 0
            metadata["uploaded_time"] = datetime.datetime.utcnow()
            if type == "podcast":
                participent = metadata.get("participents", None)
                if (
                        participent is None
                        or len(participent) > 10
                        or any(i for i in participent if len(i) > 100)
                ):
                    return Response("The request is invalid: 400 bad request", status=400)
            try:
                audio_type.objects.create(**metadata)
                return Response("200 ok", status=200)
            except:
                pass
        return Response("The request is invalid: 400 bad request", status=400)

    def delete_audio(self, request, *args, **kwargs):
        audio_file_type, audio_file_id = kwargs.get('audioFileType'), kwargs.get('audioFileID')
        audio_file_obj = self.audiofiletype.get(audio_file_type)
        if audio_file_obj:
            try:
                audio_obj = audio_file_obj.objects.get(id=audio_file_id)
                audio_obj.delete()
                return Response("200 ok", status=200)
            except:
                pass
        return Response("The request is invalid: 400 bad request", status=400)

    def get_audio(self, request, *args, **kwargs):
        audio_file_type, audio_file_id =  kwargs.get('audioFileType'), kwargs.get('audioFileID')
        audio_file_obj = self.audiofiletype.get(audio_file_type)
        audioserializers = self.audioserializers.get(audio_file_type)
        if audio_file_obj:
            try:
                if audio_file_id:
                    data = audioserializers(audio_file_obj.objects.get(id=audio_file_id)).data
                else:
                    data = audioserializers(audio_file_obj.objects.all(), many=True).data
                return Response(data=data, status=200)
            except:
                pass
        return Response(data="The request is invalid: 400 bad request", status=400)

    def update_audio(self, request, *args, **kwargs):
        audio_file_type, audio_file_id = kwargs.get('audioFileType'), kwargs.get('audioFileID')
        request_data = request.data
        audio_file_obj = self.audiofiletype.get(audio_file_type)
        metadata = request_data.get("audioFileMetadata")
        if audio_file_obj and metadata:
            try:
                metadata["uploaded_time"] = datetime.datetime.utcnow()
                audio_file_obj.objects.filter(id=audio_file_id).update(**metadata)
                return Response("200 ok", status=200)
            except:
                pass
        return Response("The request is invalid: 400 bad request", status=400)
