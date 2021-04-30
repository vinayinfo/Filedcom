from django.urls import include, path

from audio.views import AudioViewSet

urlpatterns = [
    path("create/", AudioViewSet.as_view({"post": "create_audio"})),
    path(
        "<str:audioFileType>/<int:audioFileID>/",
        AudioViewSet.as_view({"get": "get_audio", "put": "update_audio", "delete": "delete_audio"}),
    ),
    path(
        "<str:audioFileType>/",
        AudioViewSet.as_view(
            {
                "get": "get_audio",
            }
        ),
    ),
]
