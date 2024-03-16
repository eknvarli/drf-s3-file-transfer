from rest_framework import serializers
from transfer.models import File
from django.core.files.storage import default_storage



class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id','name','file','uploaded_at')

    def save(self):
        file_obj = self.validated_data['file']
        file_name = file_obj.name
        file_path = f'files/{file_name}'

        with default_storage.open(file_path, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        self.validated_data['file'] = file_path
        return super().save()