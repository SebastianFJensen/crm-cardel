from django.core.files.storage import Storage
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from django.conf import settings

print ("loaded!") 

class AzureStorage(Storage):
    def __init__(self, connection_string=None, container_name=None, *args, **kwargs):
        if not connection_string:
            connection_string = settings.AZURE_CONNECTION_STRING
        if not container_name:
            container_name = settings.AZURE_CONTAINER_NAME

        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_client = self.blob_service_client.get_container_client(container_name)
        self.container_exists = self.container_client.exists()

    def _open(self, name, mode='rb'):
        if not self.container_exists:
            self.container_client.create_container()

        blob_client = self.container_client.get_blob_client(name)
        stream = blob_client.download_blob().readall()
        return stream

    def _save(self, name, content):
        if not self.container_exists:
            self.container_client.create_container()

        blob_client = self.container_client.get_blob_client(name)
        blob_client.upload_blob(content, overwrite=True)

    def exists(self, name):
        blob_client = self.container_client.get_blob_client(name)
        return blob_client.exists()

    def url(self, name):
        blob_client = self.container_client.get_blob_client(name)
        return blob_client.url