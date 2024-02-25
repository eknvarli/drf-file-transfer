from rest_framework import viewsets
from .models import File
from .serializers import FileSerializer

# Create your views here.
class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer