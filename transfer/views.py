from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from transfer.models import File
from transfer.serializers import FileSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(detail=True, methods=['GET'])
    def download(self, request, pk=None):
        file = get_object_or_404(File, pk=pk)
        file_path = file.file.path
        with open(file_path, 'rb') as file_content:
            response = Response(file_content, content_type='application/force-download')
            response['Content-Disposition'] = f'attachment; filename={file.name}'

            return response