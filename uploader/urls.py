from django.urls import path
from .views import upload_file, home


urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('', home, name='home'),
]
